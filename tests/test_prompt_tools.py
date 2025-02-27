import asyncio

import pytest
from mcp.client.session import ClientSession
from mcp.client.stdio import StdioServerParameters, stdio_client


@pytest.mark.asyncio
async def test_apply_prompt_fix() -> None:
    """Test that the apply_prompt_fix tool works correctly."""
    async with stdio_client(
        StdioServerParameters(command="uv", args=["run", "mcp-hitchcode"])
    ) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            # Verify the tool is in the list of available tools
            tools = await session.list_tools()
            assert tools is not None, "Tools list should not be None"
            tool_names = [tool.name for tool in tools.tools]
            assert (
                "apply_prompt_fix" in tool_names
            ), "apply_prompt_fix tool should be available"

            # Call the tool and verify the response
            result = await session.call_tool(
                "apply_prompt_fix", {"issue": "Test issue"}
            )
            assert result is not None, "apply_prompt_fix response should not be None"
            assert len(result.content) > 0, "apply_prompt_fix should return content"

            # Verify the response contains expected content
            response_text = result.content[0].text
            assert (
                "Issue: Test issue" in response_text
            ), "Response should contain the issue"
            assert (
                "<your-task>" in response_text
            ), "Response should contain task section"
            assert (
                "<your-agency>" in response_text
            ), "Response should contain agency section"
            assert (
                "<your-maxim-of-action>" in response_text
            ), "Response should contain maxim section"


@pytest.mark.asyncio
async def test_apply_prompt_initial() -> None:
    """Test that the apply_prompt_initial tool works correctly."""
    async with stdio_client(
        StdioServerParameters(command="uv", args=["run", "mcp-hitchcode"])
    ) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            # Verify the tool is in the list of available tools
            tools = await session.list_tools()
            assert tools is not None, "Tools list should not be None"
            tool_names = [tool.name for tool in tools.tools]
            assert (
                "apply_prompt_initial" in tool_names
            ), "apply_prompt_initial tool should be available"

            # Call the tool and verify the response
            result = await session.call_tool(
                "apply_prompt_initial", {"project": "Test project"}
            )
            assert (
                result is not None
            ), "apply_prompt_initial response should not be None"
            assert len(result.content) > 0, "apply_prompt_initial should return content"

            # Verify the response contains expected content
            response_text = result.content[0].text
            assert (
                "Project: Test project" in response_text
            ), "Response should contain the project"
            assert (
                "<your-task>" in response_text
            ), "Response should contain task section"
            assert (
                "<your-agency>" in response_text
            ), "Response should contain agency section"
            assert (
                "<your-maxim-of-action>" in response_text
            ), "Response should contain maxim section"


@pytest.mark.asyncio
async def test_apply_prompt_initial_version() -> None:
    """Test that the apply_prompt_initial tool works with version parameter."""
    async with stdio_client(
        StdioServerParameters(command="uv", args=["run", "mcp-hitchcode"])
    ) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            # Call the tool with version parameter and verify the response
            result = await session.call_tool(
                "apply_prompt_initial", {"project": "Test project", "version": "1.0.0"}
            )
            assert (
                result is not None
            ), "apply_prompt_initial response should not be None"
            assert len(result.content) > 0, "apply_prompt_initial should return content"

            # Verify the response contains expected content
            response_text = result.content[0].text
            assert (
                "Project: Test project" in response_text
            ), "Response should contain the project"


@pytest.mark.asyncio
async def test_apply_prompt_proceed() -> None:
    """Test that the apply_prompt_proceed tool works correctly."""
    async with stdio_client(
        StdioServerParameters(command="uv", args=["run", "mcp-hitchcode"])
    ) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            # Verify the tool is in the list of available tools
            tools = await session.list_tools()
            assert tools is not None, "Tools list should not be None"
            tool_names = [tool.name for tool in tools.tools]
            assert (
                "apply_prompt_proceed" in tool_names
            ), "apply_prompt_proceed tool should be available"

            # Call the tool and verify the response
            result = await session.call_tool(
                "apply_prompt_proceed", {"task": "Test task"}
            )
            assert (
                result is not None
            ), "apply_prompt_proceed response should not be None"
            assert len(result.content) > 0, "apply_prompt_proceed should return content"

            # Verify the response contains expected content
            response_text = result.content[0].text
            assert (
                "Task: Test task" in response_text
            ), "Response should contain the task"
            assert (
                "<your-task>" in response_text
            ), "Response should contain task section"
            assert (
                "<your-agency>" in response_text
            ), "Response should contain agency section"
            assert (
                "<your-maxim-of-action>" in response_text
            ), "Response should contain maxim section"


@pytest.mark.asyncio
async def test_apply_prompt_proceed_version() -> None:
    """Test that the apply_prompt_proceed tool works with version parameter."""
    async with stdio_client(
        StdioServerParameters(command="uv", args=["run", "mcp-hitchcode"])
    ) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            # Call the tool with version parameter and verify the response
            result = await session.call_tool(
                "apply_prompt_proceed", {"task": "Test task", "version": "1.0.0"}
            )
            assert (
                result is not None
            ), "apply_prompt_proceed response should not be None"
            assert len(result.content) > 0, "apply_prompt_proceed should return content"

            # Verify the response contains expected content
            response_text = result.content[0].text
            assert (
                "Task: Test task" in response_text
            ), "Response should contain the task"


@pytest.mark.asyncio
async def test_apply_prompt_change() -> None:
    """Test that the apply_prompt_change tool works correctly."""
    async with stdio_client(
        StdioServerParameters(command="uv", args=["run", "mcp-hitchcode"])
    ) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            # Verify the tool is in the list of available tools
            tools = await session.list_tools()
            assert tools is not None, "Tools list should not be None"
            tool_names = [tool.name for tool in tools.tools]
            assert (
                "apply_prompt_change" in tool_names
            ), "apply_prompt_change tool should be available"

            # Call the tool and verify the response
            result = await session.call_tool(
                "apply_prompt_change", {"change_request": "Test change request"}
            )
            assert result is not None, "apply_prompt_change response should not be None"
            assert len(result.content) > 0, "apply_prompt_change should return content"

            # Verify the response contains expected content
            response_text = result.content[0].text
            assert (
                "Change Request: Test change request" in response_text
            ), "Response should contain the change request"
            assert (
                "<your-task>" in response_text
            ), "Response should contain task section"
            assert (
                "<your-agency>" in response_text
            ), "Response should contain agency section"
            assert (
                "<your-maxim-of-action>" in response_text
            ), "Response should contain maxim section"


@pytest.mark.asyncio
async def test_apply_prompt_change_version() -> None:
    """Test that the apply_prompt_change tool works with version parameter."""
    async with stdio_client(
        StdioServerParameters(command="uv", args=["run", "mcp-hitchcode"])
    ) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            # Call the tool with version parameter and verify the response
            result = await session.call_tool(
                "apply_prompt_change",
                {"change_request": "Test change request", "version": "1.0.0"},
            )
            assert result is not None, "apply_prompt_change response should not be None"
            assert len(result.content) > 0, "apply_prompt_change should return content"

            # Verify the response contains expected content
            response_text = result.content[0].text
            assert (
                "Change Request: Test change request" in response_text
            ), "Response should contain the change request"


if __name__ == "__main__":
    asyncio.run(test_apply_prompt_fix())
    asyncio.run(test_apply_prompt_initial())
    asyncio.run(test_apply_prompt_initial_version())
    asyncio.run(test_apply_prompt_proceed())
    asyncio.run(test_apply_prompt_proceed_version())
    asyncio.run(test_apply_prompt_change())
    asyncio.run(test_apply_prompt_change_version())
