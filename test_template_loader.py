#!/usr/bin/env python3
"""
Test script for the template loader.

This script tests the template loader's ability to load templates with the new naming pattern.
"""

from mcp_hitchcode.templates.template_loader import (
    _build_version_registry,
    get_template_versions,
    render_prompt_template,
)


def test_template_loader():
    """Test the template loader with the new naming pattern."""
    print("Testing template loader with new naming pattern...")

    # Build the version registry
    _build_version_registry()

    # Get the versions for the test template
    versions = get_template_versions("test_template")
    print(f"Available versions for test_template: {versions}")

    # Render the test template
    rendered = render_prompt_template(
        "test_template",
        version_str="latest",
        test_var="Hello, world!",
    )
    print("\nRendered template:")
    print("=" * 40)
    print(rendered)
    print("=" * 40)

    print("\nTest completed successfully!")


if __name__ == "__main__":
    test_template_loader()
