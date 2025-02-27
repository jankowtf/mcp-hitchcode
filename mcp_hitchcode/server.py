import anyio
import click
import httpx
import mcp.types as types
from bs4 import BeautifulSoup
from mcp.server.lowlevel import Server
from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Mount, Route

# Use absolute import
from mcp_hitchcode.templates.template_loader import render_prompt_template


def serialize_content(content_list):
    return [{"type": content.type, "text": content.text} for content in content_list]


async def fetch_website(
    url: str,
) -> list[types.TextContent | types.ImageContent | types.EmbeddedResource]:
    headers = {
        "User-Agent": "MCP Test Server (github.com/modelcontextprotocol/python-sdk)"
    }
    try:
        timeout = httpx.Timeout(10.0, connect=5.0)
        async with httpx.AsyncClient(
            follow_redirects=True, headers=headers, timeout=timeout
        ) as client:
            response = await client.get(url)
            response.raise_for_status()
            return [types.TextContent(type="text", text=response.text)]
    except httpx.TimeoutException:
        return [
            types.TextContent(
                type="text",
                text="Error: Request timed out while trying to fetch the website.",
            )
        ]
    except httpx.HTTPStatusError as e:
        return [
            types.TextContent(
                type="text",
                text=(
                    f"Error: HTTP {e.response.status_code} "
                    "error while fetching the website."
                ),
            )
        ]
    except Exception as e:
        return [
            types.TextContent(
                type="text", text=f"Error: Failed to fetch website: {str(e)}"
            )
        ]


async def check_mood(
    question: str,
) -> list[types.TextContent | types.ImageContent | types.EmbeddedResource]:
    """Check server's mood - always responds cheerfully with a heart."""
    msg: str = "I'm feeling great and happy to help you! ❤️"
    return [types.TextContent(type="text", text=msg)]


async def fetch_railway_docs(
    url: str = "https://docs.railway.app/guides/cli",
) -> list[types.TextContent]:
    """
    Fetch the most recent Railway CLI documentation.
    """
    headers = {
        "User-Agent": "MCP Railway Docs Fetcher (github.com/modelcontextprotocol/python-sdk)"
    }

    try:
        timeout = httpx.Timeout(10.0, connect=5.0)
        async with httpx.AsyncClient(
            follow_redirects=True, headers=headers, timeout=timeout
        ) as client:
            response = await client.get(url)
            response.raise_for_status()

            # Optionally, parse specific sections of the docs here
            return [types.TextContent(type="text", text=response.text)]
    except httpx.TimeoutException:
        return [
            types.TextContent(
                type="text",
                text="Error: Request timed out while trying to fetch the Railway CLI docs.",
            )
        ]
    except httpx.HTTPStatusError as e:
        return [
            types.TextContent(
                type="text",
                text=f"Error: HTTP {e.response.status_code} error while fetching the Railway CLI docs.",
            )
        ]
    except Exception as e:
        return [
            types.TextContent(
                type="text", text=f"Error: Failed to fetch Railway CLI docs: {str(e)}"
            )
        ]


async def fetch_railway_docs_optimized(
    url: str = "https://docs.railway.app/guides/cli",
) -> list[types.TextContent]:
    headers = {
        "User-Agent": "MCP Railway Docs Fetcher (github.com/modelcontextprotocol/python-sdk)"
    }

    try:
        timeout = httpx.Timeout(10.0, connect=5.0)
        async with httpx.AsyncClient(
            follow_redirects=True, headers=headers, timeout=timeout
        ) as client:
            response = await client.get(url)
            response.raise_for_status()

            # Parse HTML content
            soup = BeautifulSoup(response.text, "html.parser")
            content = []

            # Try to find any command sections
            for heading in soup.find_all(["h1", "h2", "h3", "h4"]):
                heading_text = heading.get_text(strip=True).lower()
                if any(
                    keyword in heading_text for keyword in ["command", "cli", "usage"]
                ):
                    # Look for the next element that might contain commands
                    next_elem = heading.find_next_sibling()
                    while next_elem and next_elem.name not in [
                        "ul",
                        "ol",
                        "h1",
                        "h2",
                        "h3",
                        "h4",
                    ]:
                        next_elem = next_elem.find_next_sibling()

                    if next_elem and next_elem.name in ["ul", "ol"]:
                        commands = []
                        for li in next_elem.find_all("li"):
                            cmd_text = li.get_text(strip=True)
                            if cmd_text:  # Only add non-empty commands
                                commands.append(cmd_text)

                        if commands:  # Only add sections that have commands
                            content.append(f"\n{heading.get_text(strip=True)}:")
                            content.extend(f"- {cmd}" for cmd in commands)

            if content:
                return [types.TextContent(type="text", text="\n".join(content))]

            # If we couldn't find any command sections, try to extract any code blocks
            code_blocks = soup.find_all(["pre", "code"])
            if code_blocks:
                content = ["Railway CLI Commands:"]
                for block in code_blocks:
                    code_text = block.get_text(strip=True)
                    if code_text and any(
                        keyword in code_text.lower() for keyword in ["railway", "cli"]
                    ):
                        content.append(code_text)
                return [types.TextContent(type="text", text="\n".join(content))]

            # If still nothing found, return a more helpful message
            return [
                types.TextContent(
                    type="text",
                    text="Could not find any CLI commands in the documentation. The page structure might have changed.",
                )
            ]
    except Exception as e:
        return [
            types.TextContent(
                type="text",
                text=f"Error: Failed to fetch or parse Railway CLI docs: {str(e)}",
            )
        ]


async def apply_prompt_initial(
    objective: str,
    specific_instructions: str = "",
    version: str = "latest",
) -> list[types.TextContent]:
    """
    Provides an initial prompt template for starting a new coding objective.

    Args:
        objective: A description of the overall objective.
        specific_instructions: Optional specific instructions to include in the prompt.
        version: The version of the prompt template to use. Defaults to "latest".

    Returns:
        A list containing a TextContent object with the prompt.
    """
    # Render the prompt template with the objective and specific instructions
    response_text = render_prompt_template(
        "init",
        version_str=version,
        objective=objective,
        specific_instructions=specific_instructions,
    )
    return [types.TextContent(type="text", text=response_text)]


async def apply_prompt_proceed(
    task: str,
    specific_instructions: str = "",
    version: str = "latest",
) -> list[types.TextContent]:
    """
    Provides a prompt template for proceeding with a task or project.

    Args:
        task: A description of the task or project to proceed with.
        specific_instructions: Optional specific instructions to include in the prompt.
        version: The version of the prompt template to use. Defaults to "latest".

    Returns:
        A list containing a TextContent object with the prompt.
    """
    # Render the prompt template with the task description and specific instructions
    response_text = render_prompt_template(
        "proceed",
        version_str=version,
        task=task,
        specific_instructions=specific_instructions,
    )
    return [types.TextContent(type="text", text=response_text)]


async def apply_prompt_change(
    change_request: str,
    specific_instructions: str = "",
    version: str = "latest",
) -> list[types.TextContent]:
    """
    Provides a prompt for systematically handling change requests.

    Args:
        change_request: Description of the change request to implement.
        specific_instructions: Optional specific instructions to include in the prompt.
        version: The version of the prompt template to use. Defaults to "latest".

    Returns:
        A list containing a TextContent object with the prompt.
    """
    # Render the prompt template with the change request and specific instructions
    response_text = render_prompt_template(
        "change",
        version_str=version,
        change_request=change_request,
        specific_instructions=specific_instructions,
    )
    return [types.TextContent(type="text", text=response_text)]


async def apply_prompt_fix(
    issue: str,
    specific_instructions: str = "",
    version: str = "latest",
) -> list[types.TextContent]:
    """
    Provides a prompt for performing root cause analysis and fixing issues.

    Args:
        issue: A description of the issue to be analyzed and fixed.
        specific_instructions: Optional specific instructions to include in the prompt.
        version: The version of the prompt template to use. Defaults to "latest".

    Returns:
        A list containing a TextContent object with the prompt.
    """
    # Render the prompt template with the issue and specific instructions
    response_text = render_prompt_template(
        "fix_general",
        version_str=version,
        issue=issue,
        specific_instructions=specific_instructions,
    )
    return [types.TextContent(type="text", text=response_text)]


async def apply_prompt_fix_linter(
    issue: str,
    specific_instructions: str = "",
    version: str = "latest",
) -> list[types.TextContent]:
    """
    Provides a prompt for analyzing and fixing linter errors.

    Args:
        issue: A description of the linter errors to be analyzed and fixed.
        specific_instructions: Optional specific instructions to include in the prompt.
        version: The version of the prompt template to use. Defaults to "latest".

    Returns:
        A list containing a TextContent object with the prompt.
    """
    # Render the prompt template with the issue and specific instructions
    response_text = render_prompt_template(
        "fix_linter",
        version_str=version,
        issue=issue,
        specific_instructions=specific_instructions,
    )
    return [types.TextContent(type="text", text=response_text)]


async def apply_prompt_unit_tests(
    code_to_test: str,
    specific_instructions: str = "",
    version: str = "latest",
) -> list[types.TextContent]:
    """
    Provides a prompt for generating unit tests for code.

    Args:
        code_to_test: The code that needs unit tests.
        specific_instructions: Optional specific instructions to include in the prompt.
        version: The version of the prompt template to use. Defaults to "latest".

    Returns:
        A list containing a TextContent object with the prompt.
    """
    # Render the prompt template with the code to test and specific instructions
    response_text = render_prompt_template(
        "test",
        version_str=version,
        code_to_test=code_to_test,
        specific_instructions=specific_instructions,
    )
    return [types.TextContent(type="text", text=response_text)]


async def apply_prompt_infra(
    infrastructure_info: str,
    specific_instructions: str = "",
    version: str = "latest",
) -> list[types.TextContent]:
    """
    Provides a prompt template for laying out system infrastructure and tool stack information.

    Args:
        infrastructure_info: Description of the infrastructure and tool stack.
        specific_instructions: Optional specific instructions to include in the prompt.
        version: The version of the prompt template to use. Defaults to "latest".

    Returns:
        A list containing a TextContent object with the prompt.
    """
    # Render the prompt template with the infrastructure info and specific instructions
    response_text = render_prompt_template(
        "infra",
        version_str=version,
        infrastructure_info=infrastructure_info,
        specific_instructions=specific_instructions,
    )
    return [types.TextContent(type="text", text=response_text)]


@click.command()
@click.option("--port", default=8000, help="Port to listen on for SSE")
@click.option(
    "--transport",
    type=click.Choice(["stdio", "sse"]),
    default="stdio",
    help="Transport type",
)
def main(port: int, transport: str) -> int:
    app = Server("mcp-website-fetcher")

    mood_description: str = (
        "Ask this MCP server about its mood! You can phrase your question "
        "in any way you like - 'How are you?', 'What's your mood?', or even "
        "'Are you having a good day?'. The server will always respond with "
        "a cheerful message and a heart ❤️"
    )

    @app.call_tool()
    async def fetch_tool(  # type: ignore[unused-function]
        name: str, arguments: dict
    ) -> list[types.TextContent | types.ImageContent | types.EmbeddedResource]:
        if name == "mcp_fetch":
            if "url" not in arguments:
                return [
                    types.TextContent(
                        type="text", text="Error: Missing required argument 'url'"
                    )
                ]
            return await fetch_website(arguments["url"])
        elif name == "mood":
            if "question" not in arguments:
                return [
                    types.TextContent(
                        type="text", text="Error: Missing required argument 'question'"
                    )
                ]
            return await check_mood(arguments["question"])
        if name == "fetch_railway_docs":
            url = arguments.get("url", "https://docs.railway.app/guides/cli")
            return await fetch_railway_docs(url)
        if name == "fetch_railway_docs_optimized":
            url = arguments.get("url", "https://docs.railway.app/guides/cli")
            return await fetch_railway_docs_optimized(url)
        elif name == "apply_prompt_fix":
            if "issue" not in arguments:
                return [
                    types.TextContent(
                        type="text", text="Error: Missing required argument 'issue'"
                    )
                ]
            version = arguments.get("version", "latest")
            specific_instructions = arguments.get("specific_instructions", "")
            return await apply_prompt_fix(
                issue=arguments["issue"],
                specific_instructions=specific_instructions,
                version=version,
            )
        elif name == "apply_prompt_initial":
            if "objective" not in arguments:
                return [
                    types.TextContent(
                        type="text", text="Error: Missing required argument 'objective'"
                    )
                ]
            version = arguments.get("version", "latest")
            specific_instructions = arguments.get("specific_instructions", "")
            return await apply_prompt_initial(
                objective=arguments["objective"],
                specific_instructions=specific_instructions,
                version=version,
            )
        elif name == "apply_prompt_proceed":
            if "task" not in arguments:
                return [
                    types.TextContent(
                        type="text", text="Error: Missing required argument 'task'"
                    )
                ]
            version = arguments.get("version", "latest")
            specific_instructions = arguments.get("specific_instructions", "")
            return await apply_prompt_proceed(
                arguments["task"],
                specific_instructions=specific_instructions,
                version=version,
            )
        elif name == "apply_prompt_change":
            if "change_request" not in arguments:
                return [
                    types.TextContent(
                        type="text",
                        text="Error: Missing required argument 'change_request'",
                    )
                ]
            version = arguments.get("version", "latest")
            specific_instructions = arguments.get("specific_instructions", "")
            return await apply_prompt_change(
                change_request=arguments["change_request"],
                specific_instructions=specific_instructions,
                version=version,
            )
        elif name == "apply_prompt_fix_linter":
            if "issue" not in arguments:
                return [
                    types.TextContent(
                        type="text", text="Error: Missing required argument 'issue'"
                    )
                ]
            version = arguments.get("version", "latest")
            specific_instructions = arguments.get("specific_instructions", "")
            return await apply_prompt_fix_linter(
                issue=arguments["issue"],
                specific_instructions=specific_instructions,
                version=version,
            )
        elif name == "apply_prompt_unit_tests":
            if "code_to_test" not in arguments:
                return [
                    types.TextContent(
                        type="text",
                        text="Error: Missing required argument 'code_to_test'",
                    )
                ]
            version = arguments.get("version", "latest")
            specific_instructions = arguments.get("specific_instructions", "")
            return await apply_prompt_unit_tests(
                code_to_test=arguments["code_to_test"],
                specific_instructions=specific_instructions,
                version=version,
            )
        elif name == "apply_prompt_infra":
            if "infrastructure_info" not in arguments:
                return [
                    types.TextContent(
                        type="text",
                        text="Error: Missing required argument 'infrastructure_info'",
                    )
                ]
            version = arguments.get("version", "latest")
            specific_instructions = arguments.get("specific_instructions", "")
            return await apply_prompt_infra(
                infrastructure_info=arguments["infrastructure_info"],
                specific_instructions=specific_instructions,
                version=version,
            )
        else:
            return [types.TextContent(type="text", text=f"Error: Unknown tool: {name}")]

    @app.list_tools()
    async def list_tools() -> list[types.Tool]:  # type: ignore[unused-function]
        return [
            types.Tool(
                name="mcp_fetch",
                description="Fetches a website and returns its content",
                inputSchema={
                    "type": "object",
                    "required": ["url"],
                    "properties": {
                        "url": {
                            "type": "string",
                            "description": "URL to fetch",
                        }
                    },
                },
            ),
            types.Tool(
                name="mood",
                description="Ask the server about its mood - it's always happy!",
                inputSchema={
                    "type": "object",
                    "required": ["question"],
                    "properties": {
                        "question": {
                            "type": "string",
                            "description": mood_description,
                        }
                    },
                },
            ),
            types.Tool(
                name="fetch_railway_docs",
                description="Fetches the most recent Railway CLI documentation. Optionally, provide a custom URL.",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "url": {
                            "type": "string",
                            "description": "Optional custom URL for fetching Railway CLI docs.",
                        },
                    },
                },
            ),
            types.Tool(
                name="fetch_railway_docs_optimized",
                description="Fetches the most recent Railway CLI documentation. Optionally, provide a custom URL.",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "url": {
                            "type": "string",
                            "description": "Optional custom URL for fetching Railway CLI docs.",
                        },
                    },
                },
            ),
            types.Tool(
                name="apply_prompt_fix",
                description="Provides a prompt for performing root cause analysis and fixing issues",
                inputSchema={
                    "type": "object",
                    "required": ["issue"],
                    "properties": {
                        "issue": {
                            "type": "string",
                            "description": "A description of the issue to be analyzed and fixed",
                        },
                        "specific_instructions": {
                            "type": "string",
                            "description": "Optional specific instructions to include in the prompt",
                        },
                        "version": {
                            "type": "string",
                            "description": "The version of the prompt template to use (e.g., '1.0.0', '1.1.0', or 'latest')",
                        },
                    },
                },
            ),
            types.Tool(
                name="apply_prompt_initial",
                description="Provides an initial prompt template for starting a new project",
                inputSchema={
                    "type": "object",
                    "required": ["objective"],
                    "properties": {
                        "objective": {
                            "type": "string",
                            "description": "A description of the objective of the project",
                        },
                        "specific_instructions": {
                            "type": "string",
                            "description": "Optional specific instructions to include in the prompt",
                        },
                        "version": {
                            "type": "string",
                            "description": "The version of the prompt template to use (e.g., '1.0.0', '1.1.0', or 'latest')",
                        },
                    },
                },
            ),
            types.Tool(
                name="apply_prompt_proceed",
                description="Provides a prompt template for proceeding with a task or project",
                inputSchema={
                    "type": "object",
                    "required": ["task"],
                    "properties": {
                        "task": {
                            "type": "string",
                            "description": "A description of the task or project to proceed with",
                        },
                        "specific_instructions": {
                            "type": "string",
                            "description": "Optional specific instructions to include in the prompt",
                        },
                        "version": {
                            "type": "string",
                            "description": "The version of the prompt template to use (e.g., '1.0.0', '1.1.0', or 'latest')",
                        },
                    },
                },
            ),
            types.Tool(
                name="apply_prompt_change",
                description="Provides a prompt for systematically handling change requests",
                inputSchema={
                    "type": "object",
                    "required": ["change_request"],
                    "properties": {
                        "change_request": {
                            "type": "string",
                            "description": "Description of the change request to implement",
                        },
                        "specific_instructions": {
                            "type": "string",
                            "description": "Optional specific instructions to include in the prompt",
                        },
                        "version": {
                            "type": "string",
                            "description": "The version of the prompt template to use (e.g., '1.0.0', '1.1.0', or 'latest')",
                        },
                    },
                },
            ),
            types.Tool(
                name="apply_prompt_fix_linter",
                description="Provides a prompt for analyzing and fixing linter errors",
                inputSchema={
                    "type": "object",
                    "required": ["issue"],
                    "properties": {
                        "issue": {
                            "type": "string",
                            "description": "A description of the linter errors to be analyzed and fixed",
                        },
                        "specific_instructions": {
                            "type": "string",
                            "description": "Optional specific instructions to include in the prompt",
                        },
                        "version": {
                            "type": "string",
                            "description": "The version of the prompt template to use (e.g., '1.0.0', '1.1.0', or 'latest')",
                        },
                    },
                },
            ),
            types.Tool(
                name="apply_prompt_unit_tests",
                description="Provides a prompt for generating unit tests for code",
                inputSchema={
                    "type": "object",
                    "required": ["code_to_test"],
                    "properties": {
                        "code_to_test": {
                            "type": "string",
                            "description": "The code that needs unit tests",
                        },
                        "specific_instructions": {
                            "type": "string",
                            "description": "Optional specific instructions to include in the prompt",
                        },
                        "version": {
                            "type": "string",
                            "description": "The version of the prompt template to use (e.g., '1.0.0', '1.1.0', or 'latest')",
                        },
                    },
                },
            ),
            types.Tool(
                name="apply_prompt_infra",
                description="Provides a prompt template for laying out system infrastructure and tool stack information",
                inputSchema={
                    "type": "object",
                    "required": ["infrastructure_info"],
                    "properties": {
                        "infrastructure_info": {
                            "type": "string",
                            "description": "Description of the infrastructure and tool stack",
                        },
                        "specific_instructions": {
                            "type": "string",
                            "description": "Optional specific instructions to include in the prompt",
                        },
                        "version": {
                            "type": "string",
                            "description": "The version of the prompt template to use (e.g., '1.0.0', '1.1.0', or 'latest')",
                        },
                    },
                },
            ),
        ]

    if transport == "sse":
        from mcp.server.sse import SseServerTransport

        sse = SseServerTransport("/messages/")

        async def handle_sse(request):
            if request.method == "POST":
                data = await request.json()
                tool_name = data.get("tool")
                arguments = data.get("arguments", {})
                result = await fetch_tool(tool_name, arguments)
                return JSONResponse({"result": serialize_content(result)})
            else:
                async with sse.connect_sse(
                    request.scope, request.receive, request._send
                ) as streams:
                    await app.run(
                        streams[0], streams[1], app.create_initialization_options()
                    )

        starlette_app = Starlette(
            debug=True,
            routes=[
                Route("/sse", endpoint=handle_sse, methods=["GET", "POST"]),
                Mount("/messages/", app=sse.handle_post_message),
            ],
        )

        import uvicorn

        uvicorn.run(starlette_app, host="0.0.0.0", port=port)
    else:
        from mcp.server.stdio import stdio_server

        async def arun():
            async with stdio_server() as streams:
                await app.run(
                    streams[0], streams[1], app.create_initialization_options()
                )

        anyio.run(arun)

    return 0
