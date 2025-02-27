#!/usr/bin/env python3
"""
Test script to verify that the server.py functions work correctly with the updated template names.
"""

import asyncio

from mcp_simple_tool.server import (
    get_prompt_change,
    get_prompt_fix,
    get_prompt_fix_linter,
    get_prompt_initial,
    get_prompt_proceed,
    get_prompt_unit_tests,
)


async def test_server_functions():
    """Test all server.py functions that use templates."""
    print("Testing server.py functions with the updated template names...")

    # Test get_prompt_initial
    print("\nTesting get_prompt_initial...")
    result = await get_prompt_initial("Test project", "Test specific instructions")
    print(f"Result type: {type(result)}")
    print(f"First 100 characters: {result[0].text[:100]}...")

    # Test get_prompt_proceed
    print("\nTesting get_prompt_proceed...")
    result = await get_prompt_proceed("Test task", "Test specific instructions")
    print(f"Result type: {type(result)}")
    print(f"First 100 characters: {result[0].text[:100]}...")

    # Test get_prompt_change
    print("\nTesting get_prompt_change...")
    result = await get_prompt_change(
        "Test change request", "Test specific instructions"
    )
    print(f"Result type: {type(result)}")
    print(f"First 100 characters: {result[0].text[:100]}...")

    # Test get_prompt_fix
    print("\nTesting get_prompt_fix...")
    result = await get_prompt_fix("Test issue", "Test specific instructions")
    print(f"Result type: {type(result)}")
    print(f"First 100 characters: {result[0].text[:100]}...")

    # Test get_prompt_fix_linter
    print("\nTesting get_prompt_fix_linter...")
    result = await get_prompt_fix_linter("Test issue", "Test specific instructions")
    print(f"Result type: {type(result)}")
    print(f"First 100 characters: {result[0].text[:100]}...")

    # Test get_prompt_unit_tests
    print("\nTesting get_prompt_unit_tests...")
    result = await get_prompt_unit_tests(
        "def test(): pass", "Test specific instructions"
    )
    print(f"Result type: {type(result)}")
    print(f"First 100 characters: {result[0].text[:100]}...")

    print("\nAll tests completed successfully!")


if __name__ == "__main__":
    asyncio.run(test_server_functions())
