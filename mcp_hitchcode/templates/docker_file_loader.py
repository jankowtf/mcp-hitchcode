"""
Docker file loader for MCP Simple Tool.

This module provides functions to load Docker files from the templates directory.
"""

import functools
import os
from typing import Dict

# Cache for Docker file content to avoid repeated file I/O
_docker_file_cache: Dict[str, str] = {}


def _get_docker_dir() -> str:
    """
    Get the absolute path to the Docker files directory.

    Returns:
        str: The absolute path to the Docker files directory.
    """
    templates_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(templates_dir, "docker")


def _resolve_docker_file_path(file_path: str) -> str:
    """
    Resolve a Docker file path to an absolute path.

    Args:
        file_path: The path to the Docker file, relative to the Docker files directory.

    Returns:
        str: The absolute path to the Docker file.
    """
    # If the path is already absolute, return it as is
    if os.path.isabs(file_path):
        return file_path

    # Otherwise, resolve it relative to the Docker files directory
    docker_dir = _get_docker_dir()
    return os.path.join(docker_dir, file_path)


@functools.lru_cache(maxsize=32)
def load_docker_file(file_path: str) -> str:
    """
    Load a Docker file from the templates directory.

    Args:
        file_path: The path to the Docker file, relative to the Docker files directory.

    Returns:
        str: The Docker file content.

    Raises:
        FileNotFoundError: If the Docker file does not exist.
    """
    # Check if the Docker file is already cached
    if file_path in _docker_file_cache:
        return _docker_file_cache[file_path]

    # Resolve the Docker file path
    full_path = _resolve_docker_file_path(file_path)

    # Check if the Docker file exists
    if not os.path.isfile(full_path):
        raise FileNotFoundError(f"Docker file not found: {file_path}")

    # Load the Docker file content
    with open(full_path, "r") as f:
        docker_file_content = f.read()

    # Cache the Docker file content
    _docker_file_cache[file_path] = docker_file_content

    return docker_file_content


def docker_file(file_path: str) -> str:
    """
    Load a Dockerfile from the templates directory.

    Args:
        file_path: The path to the Dockerfile, relative to the Docker files directory.

    Returns:
        str: The Dockerfile content.

    Raises:
        FileNotFoundError: If the Dockerfile does not exist.
    """
    return load_docker_file(file_path)


def docker_compose(file_path: str) -> str:
    """
    Load a docker-compose.yml file from the templates directory.

    Args:
        file_path: The path to the docker-compose.yml file, relative to the Docker files directory.

    Returns:
        str: The docker-compose.yml content.

    Raises:
        FileNotFoundError: If the docker-compose.yml file does not exist.
    """
    return load_docker_file(file_path)


def clear_docker_file_cache() -> None:
    """
    Clear the Docker file cache.
    """
    global _docker_file_cache
    _docker_file_cache = {}
