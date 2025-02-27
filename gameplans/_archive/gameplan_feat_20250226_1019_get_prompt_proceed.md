# Game Plan: Implementing `apply_prompt_proceed` Tool

## Overview
This game plan outlines the steps to implement a new tool called `apply_prompt_proceed` in the MCP server. The tool will provide a prompt template for proceeding with a task or project, similar to the existing `apply_prompt_initial` and `apply_prompt_fix` tools. This implementation will follow the same pattern as the existing tools, leveraging the template loader mechanism.

## Stage 1: Analysis and Design
- [x] **Task 1.1: Understand the existing prompt tools**
  - Review how the `apply_prompt_initial` and `apply_prompt_fix` tools are implemented
  - Understand how the template loader mechanism works
  
- [x] **Task 1.2: Design the `apply_prompt_proceed` tool**
  - **Purpose**: Provide a prompt template for proceeding with a task or project
  - **Name**: `apply_prompt_proceed`
  - **Parameters**:
    - `task`: A description of the task or project to proceed with
    - `version`: The version of the prompt template to use (optional, defaults to "latest")
  - **Return**: A formatted prompt template with the task description

## Stage 2: Implementation
- [x] **Task 2.1: Create the prompt template**
  - Create a new directory `proceed_prompt` in `mcp_hitchcode/templates/prompts/`
  - Create a template file `1.0.0.md` with appropriate YAML front matter and template content
  - The template should include sections for task description, agency, and maxims of action

- [x] **Task 2.2: Implement the `apply_prompt_proceed` function**
  - Add a new async function `apply_prompt_proceed` in `server.py`
  - The function should accept `task` and `version` parameters
  - Use the `render_prompt_template` function to render the template

- [x] **Task 2.3: Update the tool handler**
  - Add a new condition to handle the `apply_prompt_proceed` tool in the `fetch_tool` function
  - Check for the required `task` parameter and handle the optional `version` parameter

- [x] **Task 2.4: Register the tool**
  - Create a new Tool instance for `apply_prompt_proceed` in the `list_tools` function
  - Define the input schema with the required and optional parameters
  - Provide a clear description of the tool's purpose

## Stage 3: Testing and Documentation
- [x] **Task 3.1: Write tests for the new tool**
  - Add a new test function in `tests/test_prompt_tools.py`
  - Test that the tool is available in the tool list
  - Test that the tool returns appropriate content when called
  - Test that the tool handles the version parameter correctly

- [x] **Task 3.2: Update documentation**
  - Document the new tool in any relevant documentation
  - Include examples of how to use the tool

## Implementation Details

### Task 2.1: Create the prompt template
The template should follow the same structure as the existing templates, with YAML front matter and template content. The template should include:
1. A section for the task description
2. A section for agency (what the agent should do)
3. A section for maxims of action (guidelines for the agent)

### Task 2.2: Implement the `apply_prompt_proceed` function
```python
async def apply_prompt_proceed(
    task: str,
    version: str = "latest",
) -> list[types.TextContent]:
    """
    Provides a prompt template for proceeding with a task or project.

    Args:
        task: A description of the task or project to proceed with.
        version: The version of the prompt template to use. Defaults to "latest".

    Returns:
        A list containing a TextContent object with the prompt.
    """
    # Render the prompt template with the task description
    response_text = render_prompt_template(
        "proceed_prompt", version_str=version, task=task
    )
    return [types.TextContent(type="text", text=response_text)]
```

### Task 2.3: Update the tool handler
Add a new condition to the `fetch_tool` function:
```python
elif name == "apply_prompt_proceed":
    if "task" not in arguments:
        return [
            types.TextContent(
                type="text", text="Error: Missing required argument 'task'"
            )
        ]
    version = arguments.get("version", "latest")
    return await apply_prompt_proceed(arguments["task"], version=version)
```

### Task 2.4: Register the tool
Add a new Tool instance to the `list_tools` function:
```python
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
            "version": {
                "type": "string",
                "description": "The version of the prompt template to use (e.g., '1.0.0', '1.1.0', or 'latest')",
            },
        },
    },
), 