#!/usr/bin/env python3
"""
Final verification test script for the template system.

This script performs a comprehensive verification of the template system after
the prompt folder renaming project. It tests:
1. Template loading and version detection
2. Template rendering with various parameters
3. Server functions that use templates
"""

import asyncio
import os
import sys

from mcp_hitchcode.server import (
    apply_prompt_change,
    apply_prompt_fix,
    apply_prompt_fix_linter,
    apply_prompt_infra,
    apply_prompt_initial,
    apply_prompt_proceed,
    apply_prompt_unit_tests,
)
from mcp_hitchcode.templates.template_loader import (
    _build_version_registry,
    get_latest_version,
    get_template_versions,
    render_prompt_template,
)


def print_header(title: str) -> None:
    """Print a section header."""
    print("\n" + "=" * 80)
    print(f" {title} ".center(80, "="))
    print("=" * 80)


def print_subheader(title: str) -> None:
    """Print a subsection header."""
    print("\n" + "-" * 80)
    print(f" {title} ".center(80, "-"))
    print("-" * 80)


def verify_directory_structure() -> bool:
    """Verify the directory structure is correct."""
    print_header("Verifying Directory Structure")

    # Get the absolute path to the templates directory
    # This approach is more reliable than using relative paths
    templates_dir = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "mcp_hitchcode",
        "templates",
        "prompts",
    )

    # If the path doesn't exist, try a different approach
    if not os.path.isdir(templates_dir):
        # Try to find the templates directory relative to the current working directory
        templates_dir = os.path.join(
            os.getcwd(),
            "mcp_hitchcode",
            "templates",
            "prompts",
        )

    print(f"Looking for templates in: {templates_dir}")

    expected_dirs = ["change", "init", "fix_general", "fix_linter", "proceed", "test"]
    old_dirs = [
        "change_prompt",
        "initial_prompt",
        "fix_prompt",
        "fix_linter_prompt",
        "proceed_prompt",
        "unit_tests_prompt",
    ]

    # Check that expected directories exist
    missing_dirs = []
    for dirname in expected_dirs:
        dir_path = os.path.join(templates_dir, dirname)
        if not os.path.isdir(dir_path):
            missing_dirs.append(dirname)
            print(f"❌ Missing directory: {dirname}")
        else:
            print(f"✅ Directory exists: {dirname}")

    # Check that old directories don't exist
    existing_old_dirs = []
    for dirname in old_dirs:
        dir_path = os.path.join(templates_dir, dirname)
        if os.path.isdir(dir_path):
            existing_old_dirs.append(dirname)
            print(f"❌ Old directory still exists: {dirname}")
        else:
            print(f"✅ Old directory removed: {dirname}")

    # Check template files in each directory
    template_files_missing = False
    for dirname in expected_dirs:
        dir_path = os.path.join(templates_dir, dirname)
        if os.path.isdir(dir_path):
            files = os.listdir(dir_path)
            template_files = [f for f in files if f.endswith(".md")]
            if not template_files:
                template_files_missing = True
                print(f"❌ No template files found in {dirname}/")
            else:
                # Check if template files follow the new naming pattern
                valid_pattern = True
                for filename in template_files:
                    if not filename.startswith(f"{dirname}_v"):
                        valid_pattern = False
                        print(f"❌ Invalid filename pattern: {dirname}/{filename}")

                if valid_pattern:
                    print(f"✅ Template files in {dirname}/ follow the correct pattern")
                    for filename in template_files:
                        print(f"   - {filename}")

    success = not missing_dirs and not existing_old_dirs and not template_files_missing
    if success:
        print("\n✅ Directory structure verification passed!")
    else:
        print("\n❌ Directory structure verification failed!")

    return success


def verify_template_loading() -> bool:
    """Verify that templates can be loaded correctly."""
    print_header("Verifying Template Loading")

    # Build the version registry
    _build_version_registry()

    # Test each template directory
    templates = ["change", "init", "fix_general", "fix_linter", "proceed", "test"]
    success = True

    for template_name in templates:
        print_subheader(f"Testing template: {template_name}")

        # Get the versions for the template
        versions = get_template_versions(template_name)
        if not versions:
            print(f"❌ No versions found for template {template_name}")
            success = False
            continue

        print(f"✅ Found versions: {versions}")

        # Get the latest version
        latest = get_latest_version(template_name)
        if not latest:
            print(f"❌ Failed to get latest version for {template_name}")
            success = False
            continue

        print(f"✅ Latest version: {latest}")

        # Try to render the template
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
            print(f"✅ Successfully rendered template {template_name}")
            print(f"First 100 characters: {rendered[:100]}...")
        except Exception as e:
            print(f"❌ Error rendering template {template_name}: {e}")
            success = False

    if success:
        print("\n✅ Template loading verification passed!")
    else:
        print("\n❌ Template loading verification failed!")

    return success


async def verify_server_functions() -> bool:
    """Verify that server functions work correctly."""
    print_header("Verifying Server Functions")

    success = True

    # Test apply_prompt_initial
    print_subheader("Testing apply_prompt_initial")
    try:
        result = await apply_prompt_initial(
            "Test project", "Test specific instructions"
        )
        print(f"✅ apply_prompt_initial returned result of type: {type(result)}")
        print(f"First 100 characters: {result[0].text[:100]}...")
    except Exception as e:
        print(f"❌ Error in apply_prompt_initial: {e}")
        success = False

    # Test apply_prompt_proceed
    print_subheader("Testing apply_prompt_proceed")
    try:
        result = await apply_prompt_proceed("Test task", "Test specific instructions")
        print(f"✅ apply_prompt_proceed returned result of type: {type(result)}")
        print(f"First 100 characters: {result[0].text[:100]}...")
    except Exception as e:
        print(f"❌ Error in apply_prompt_proceed: {e}")
        success = False

    # Test apply_prompt_change
    print_subheader("Testing apply_prompt_change")
    try:
        result = await apply_prompt_change(
            "Test change request", "Test specific instructions"
        )
        print(f"✅ apply_prompt_change returned result of type: {type(result)}")
        print(f"First 100 characters: {result[0].text[:100]}...")
    except Exception as e:
        print(f"❌ Error in apply_prompt_change: {e}")
        success = False

    # Test apply_prompt_fix
    print_subheader("Testing apply_prompt_fix")
    try:
        result = await apply_prompt_fix("Test issue", "Test specific instructions")
        print(f"✅ apply_prompt_fix returned result of type: {type(result)}")
        print(f"First 100 characters: {result[0].text[:100]}...")
    except Exception as e:
        print(f"❌ Error in apply_prompt_fix: {e}")
        success = False

    # Test apply_prompt_fix_linter
    print_subheader("Testing apply_prompt_fix_linter")
    try:
        result = await apply_prompt_fix_linter(
            "Test issue", "Test specific instructions"
        )
        print(f"✅ apply_prompt_fix_linter returned result of type: {type(result)}")
        print(f"First 100 characters: {result[0].text[:100]}...")
    except Exception as e:
        print(f"❌ Error in apply_prompt_fix_linter: {e}")
        success = False

    # Test apply_prompt_unit_tests
    print_subheader("Testing apply_prompt_unit_tests")
    try:
        result = await apply_prompt_unit_tests(
            "def test(): pass", "Test specific instructions"
        )
        print(f"✅ apply_prompt_unit_tests returned result of type: {type(result)}")
        print(f"First 100 characters: {result[0].text[:100]}...")
    except Exception as e:
        print(f"❌ Error in apply_prompt_unit_tests: {e}")
        success = False

    # Test apply_prompt_infra
    print_subheader("Testing apply_prompt_infra")
    try:
        result = await apply_prompt_infra(
            "Python 3.10, Poetry for dependency management, pytest for testing",
            "Test specific instructions",
        )
        print(f"✅ apply_prompt_infra returned result of type: {type(result)}")
        print(f"First 100 characters: {result[0].text[:100]}...")
    except Exception as e:
        print(f"❌ Error in apply_prompt_infra: {e}")
        success = False

    if success:
        print("\n✅ Server functions verification passed!")
    else:
        print("\n❌ Server functions verification failed!")

    return success


async def run_verification() -> bool:
    """Run all verification tests."""
    print_header("FINAL VERIFICATION")
    print("Running comprehensive verification of the template system...")

    # Run all verification tests
    dir_structure_ok = verify_directory_structure()
    template_loading_ok = verify_template_loading()
    server_functions_ok = await verify_server_functions()

    # Final result
    print_header("VERIFICATION RESULTS")
    print(f"Directory Structure: {'✅ PASSED' if dir_structure_ok else '❌ FAILED'}")
    print(f"Template Loading: {'✅ PASSED' if template_loading_ok else '❌ FAILED'}")
    print(f"Server Functions: {'✅ PASSED' if server_functions_ok else '❌ FAILED'}")

    overall_success = dir_structure_ok and template_loading_ok and server_functions_ok

    if overall_success:
        print("\n✅ ALL VERIFICATION TESTS PASSED!")
        print(
            "The template system is working correctly after the prompt folder renaming project."
        )
    else:
        print("\n❌ VERIFICATION FAILED!")
        print("Some tests did not pass. Please check the output above for details.")

    return overall_success


if __name__ == "__main__":
    success = asyncio.run(run_verification())
    sys.exit(0 if success else 1)
