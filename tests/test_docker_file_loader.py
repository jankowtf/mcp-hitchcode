"""
Test the Docker file loader functionality.
"""

import pytest

from mcp_hitchcode.templates import (
    docker_compose,
    docker_file,
    render_prompt_template,
)


def test_docker_file_loading():
    """Test loading a Dockerfile."""
    # Load a Dockerfile
    content = docker_file("python/Dockerfile")

    # Check that the content is not empty
    assert content
    assert "FROM python" in content
    assert "WORKDIR /app" in content


def test_docker_compose_loading():
    """Test loading a docker-compose.yml file."""
    # Load a docker-compose.yml file
    content = docker_compose("multi-container/docker-compose.yml")

    # Check that the content is not empty
    assert content
    assert "version: '3.8'" in content
    assert "services:" in content
    assert "postgres_data:" in content


def test_docker_template_rendering():
    """Test rendering a template with Docker file content."""
    # Render a template with Docker file content
    rendered = render_prompt_template(
        "docker",
        "1.0.0",
        docker_file_path="python/Dockerfile",
        docker_compose_path="multi-container/docker-compose.yml",
    )

    # Check that the rendered template contains the Docker file content
    assert "FROM python" in rendered
    assert "WORKDIR /app" in rendered
    assert "version: '3.8'" in rendered
    assert "services:" in rendered
    assert "postgres_data:" in rendered


def test_nonexistent_docker_file():
    """Test loading a nonexistent Docker file."""
    # Try to load a nonexistent Docker file
    with pytest.raises(FileNotFoundError):
        docker_file("nonexistent/Dockerfile")


def test_nonexistent_docker_compose():
    """Test loading a nonexistent docker-compose.yml file."""
    # Try to load a nonexistent docker-compose.yml file
    with pytest.raises(FileNotFoundError):
        docker_compose("nonexistent/docker-compose.yml")
