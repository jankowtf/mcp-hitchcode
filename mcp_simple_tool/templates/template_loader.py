"""
Template loader for MCP Simple Tool.

This module provides functions to load and render templates from the package.
"""

import functools
import os
from typing import Any, Dict

from jinja2 import Environment, FileSystemLoader, select_autoescape

# Cache for template content to avoid repeated file I/O
_template_cache: Dict[str, str] = {}


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


def render_prompt_template(template_name: str, **kwargs: Any) -> str:
    """
    Render a prompt template with the given variables.

    Args:
        template_name: The name of the prompt template (without the .md extension).
        **kwargs: The variables to pass to the template.

    Returns:
        str: The rendered prompt template.

    Raises:
        FileNotFoundError: If the template file does not exist.
        jinja2.exceptions.TemplateError: If there is an error rendering the template.
    """
    template_path = f"prompts/{template_name}.md"
    return render_template(template_path, **kwargs)
