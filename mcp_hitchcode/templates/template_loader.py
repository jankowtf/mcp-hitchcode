"""
Template loader for MCP Simple Tool.

This module provides functions to load and render templates from the package.
"""

import functools
import os
import re
from typing import Any, Dict, List, Optional, Tuple

import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape
from packaging import version

# Cache for template content to avoid repeated file I/O
_template_cache: Dict[str, str] = {}

# Cache for template metadata
_metadata_cache: Dict[str, Dict[str, Any]] = {}

# Cache for template version registry
_version_registry: Dict[str, Dict[str, str]] = {}


def _get_templates_dir() -> str:
    """
    Get the absolute path to the templates directory.

    Returns:
        str: The absolute path to the templates directory.
    """
    # Use importlib.resources to get the path to the templates directory
    # This works even when the package is installed
    return os.path.dirname(os.path.abspath(__file__))


@functools.lru_cache(maxsize=32)
def get_template_env() -> Environment:
    """
    Get the Jinja2 environment for rendering templates.

    Returns:
        Environment: The Jinja2 environment.
    """
    templates_dir = _get_templates_dir()
    return Environment(
        loader=FileSystemLoader(templates_dir),
        autoescape=select_autoescape(["html", "xml"]),
        trim_blocks=True,
        lstrip_blocks=True,
    )


def _parse_template_metadata(content: str) -> Tuple[Dict[str, Any], str]:
    """
    Parse the YAML front matter from a template.

    Args:
        content: The template content.

    Returns:
        Tuple[Dict[str, Any], str]: A tuple containing the metadata and the template content.
    """
    # Check if the template has YAML front matter
    if content.startswith("---"):
        # Find the end of the front matter
        end_index = content.find("---", 3)
        if end_index != -1:
            # Extract the front matter
            front_matter = content[3:end_index].strip()
            # Parse the front matter as YAML
            try:
                metadata = yaml.safe_load(front_matter)
                # Extract the template content
                template_content = content[end_index + 3 :].strip()
                return metadata, template_content
            except yaml.YAMLError:
                # If the front matter is not valid YAML, return empty metadata
                pass

    # If no front matter or invalid YAML, return empty metadata and the original content
    return {}, content


def _build_version_registry() -> None:
    """
    Build the version registry for all templates.
    This scans the templates directory and builds a registry of all available versions.
    """
    global _version_registry

    if _version_registry:
        # Registry already built
        return

    templates_dir = _get_templates_dir()
    prompts_dir = os.path.join(templates_dir, "prompts")

    # Check if the prompts directory exists
    if not os.path.isdir(prompts_dir):
        return

    # Scan the prompts directory for template directories
    for template_name in os.listdir(prompts_dir):
        template_dir = os.path.join(prompts_dir, template_name)

        # Skip if not a directory
        if not os.path.isdir(template_dir):
            continue

        # Initialize the version registry for this template
        _version_registry[template_name] = {}

        # Scan the template directory for version files
        version_files = []
        for filename in os.listdir(template_dir):
            # Check if the filename matches the old version pattern (e.g., 1.0.0.md)
            if re.match(r"^\d+\.\d+\.\d+\.md$", filename):
                version_str = filename[:-3]  # Remove the .md extension
                version_files.append((version_str, filename))
            # Check if the filename matches the new version pattern (e.g., change_v1.0.0.md)
            elif re.match(r"^[a-z_]+_v\d+\.\d+\.\d+\.md$", filename):
                # Extract the version from the filename (e.g., "1.0.0" from "change_v1.0.0.md")
                match = re.search(r"_v(\d+\.\d+\.\d+)\.md$", filename)
                if match:
                    version_str = match.group(1)
                    version_files.append((version_str, filename))

        # Sort the version files by version number (newest first)
        version_files.sort(key=lambda x: version.parse(x[0]), reverse=True)

        # Add the versions to the registry
        for version_str, filename in version_files:
            _version_registry[template_name][version_str] = filename

        # Set the latest version
        if version_files:
            latest_version = version_files[0][0]
            _version_registry[template_name]["latest"] = latest_version


def get_template_versions(template_name: str) -> List[str]:
    """
    Get all available versions for a template.

    Args:
        template_name: The name of the template.

    Returns:
        List[str]: A list of available versions, sorted from newest to oldest.
    """
    _build_version_registry()

    if template_name not in _version_registry:
        return []

    # Get all versions except "latest"
    versions = [v for v in _version_registry[template_name].keys() if v != "latest"]

    # Sort the versions by version number (newest first)
    versions.sort(key=lambda x: version.parse(x), reverse=True)

    return versions


def get_latest_version(template_name: str) -> Optional[str]:
    """
    Get the latest version for a template.

    Args:
        template_name: The name of the template.

    Returns:
        Optional[str]: The latest version, or None if the template does not exist.
    """
    _build_version_registry()

    if template_name not in _version_registry:
        return None

    return _version_registry[template_name].get("latest")


def load_template(template_path: str) -> str:
    """
    Load a template from the package.

    Args:
        template_path: The path to the template, relative to the templates directory.

    Returns:
        str: The template content.

    Raises:
        FileNotFoundError: If the template file does not exist.
    """
    # Check if the template is already cached
    if template_path in _template_cache:
        return _template_cache[template_path]

    # Get the absolute path to the template
    templates_dir = _get_templates_dir()
    full_path = os.path.join(templates_dir, template_path)

    # Check if the template file exists
    if not os.path.isfile(full_path):
        raise FileNotFoundError(f"Template file not found: {template_path}")

    # Load the template content
    with open(full_path, "r") as f:
        template_content = f.read()

    # Cache the template content
    _template_cache[template_path] = template_content

    return template_content


def get_template_metadata(template_path: str) -> Dict[str, Any]:
    """
    Get the metadata for a template.

    Args:
        template_path: The path to the template, relative to the templates directory.

    Returns:
        Dict[str, Any]: The template metadata.

    Raises:
        FileNotFoundError: If the template file does not exist.
    """
    # Check if the metadata is already cached
    if template_path in _metadata_cache:
        return _metadata_cache[template_path]

    # Load the template content
    content = load_template(template_path)

    # Parse the metadata
    metadata, _ = _parse_template_metadata(content)

    # Cache the metadata
    _metadata_cache[template_path] = metadata

    return metadata


def render_template(template_path: str, **kwargs: Any) -> str:
    """
    Render a template with the given variables.

    Args:
        template_path: The path to the template, relative to the templates directory.
        **kwargs: The variables to pass to the template.

    Returns:
        str: The rendered template.

    Raises:
        FileNotFoundError: If the template file does not exist.
        jinja2.exceptions.TemplateError: If there is an error rendering the template.
    """
    env = get_template_env()
    template = env.get_template(template_path)
    return template.render(**kwargs)


def render_prompt_template(
    template_name: str, version_str: str = "latest", **kwargs: Any
) -> str:
    """
    Render a prompt template with the given variables.

    Args:
        template_name: The name of the prompt template.
        version_str: The version of the template to use. Defaults to "latest".
        **kwargs: The variables to pass to the template.

    Returns:
        str: The rendered prompt template.

    Raises:
        FileNotFoundError: If the template file does not exist.
        jinja2.exceptions.TemplateError: If there is an error rendering the template.
        ValueError: If the specified version does not exist.
    """
    _build_version_registry()

    # Check if the template exists
    if template_name not in _version_registry:
        raise FileNotFoundError(f"Template not found: {template_name}")

    # Resolve the version
    if version_str == "latest":
        version_str = _version_registry[template_name].get("latest")
        if not version_str:
            raise ValueError(f"No versions found for template: {template_name}")
    elif version_str not in _version_registry[template_name]:
        # Try to find the closest version
        available_versions = get_template_versions(template_name)
        if not available_versions:
            raise ValueError(f"No versions found for template: {template_name}")

        # Find the highest version that is less than or equal to the requested version
        requested_ver = version.parse(version_str)
        for v in available_versions:
            if version.parse(v) <= requested_ver:
                version_str = v
                break
        else:
            # If no suitable version is found, use the oldest version
            version_str = available_versions[-1]

    # Get the filename from the registry
    filename = _version_registry[template_name][version_str]

    # Build the template path
    template_path = f"prompts/{template_name}/{filename}"

    # Load the template content
    content = load_template(template_path)

    # Parse the metadata and template content
    metadata, template_content = _parse_template_metadata(content)

    # Create a new template with just the content (without the front matter)
    env = get_template_env()
    template = env.from_string(template_content)

    # Render the template
    return template.render(**kwargs)
