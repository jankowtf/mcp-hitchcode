#!/usr/bin/env python3
"""
Test script to verify that all templates can be loaded and rendered with the new directory names.
"""

from mcp_simple_tool.templates.template_loader import (
    _build_version_registry,
    get_template_versions,
    render_prompt_template,
)


def test_all_templates():
    """Test all templates with the new directory names."""
    print("Testing all templates with the new directory names...")

    # Build the version registry
    _build_version_registry()

    # Test each template
    templates = ["change", "init", "fix_general", "fix_linter", "proceed", "test"]

    for template_name in templates:
        print(f"\nTesting template: {template_name}")

        # Get the versions for the template
        versions = get_template_versions(template_name)
        print(f"Available versions: {versions}")

        if not versions:
            print(f"ERROR: No versions found for template {template_name}")
            continue

        # Render the template with test data
        try:
            rendered = render_prompt_template(
                template_name,
                version_str="latest",
                project="Test project",
                task="Test task",
                issue="Test issue",
                change_request="Test change request",
                code_to_test="def test(): pass",
                specific_instructions="Test specific instructions",
            )
            print(f"Successfully rendered template {template_name}")
            print(f"First 100 characters: {rendered[:100]}...")
        except Exception as e:
            print(f"ERROR rendering template {template_name}: {e}")


if __name__ == "__main__":
    test_all_templates()
