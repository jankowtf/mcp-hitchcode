"""
Templates package for MCP Simple Tool.
"""

# Import these modules to make them available when importing the package
# Use __all__ to define what symbols are exported when using "from package import *"
__all__ = [
    "load_template",
    "render_template",
    "render_prompt_template",
    "get_template_versions",
    "get_latest_version",
    "get_template_metadata",
    "docker_file",
    "docker_compose",
    "load_docker_file",
    "clear_docker_file_cache",
]

# Import symbols that should be available when importing the package
from .docker_file_loader import (  # noqa: F401
    clear_docker_file_cache,
    docker_compose,
    docker_file,
    load_docker_file,
)
from .template_loader import (  # noqa: F401
    get_latest_version,
    get_template_metadata,
    get_template_versions,
    load_template,
    render_prompt_template,
    render_template,
)
