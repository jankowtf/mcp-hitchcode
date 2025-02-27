# Game Plan: Implement `apply_prompt_infra` Tool

## Management Summary

This game plan outlines the steps to implement a new tool called `apply_prompt_infra` in the MCP server. The tool will provide a prompt template for laying out system infrastructure and tool stack information, similar to the existing prompt tools. The implementation will follow the same pattern as the existing tools, leveraging the template loader mechanism.

## Stages and Tasks

### Stage 1: Preparation and Design
- [x] **Task 1.1: Review existing prompt tools implementation**
  - Review how the existing prompt tools are implemented
  - Understand the template loading mechanism
- [x] **Task 1.2: Design the `apply_prompt_infra` tool**
  - **Name**: `apply_prompt_infra`
  - **Description**: Provides a prompt template for laying out system infrastructure and tool stack information
  - **Parameters**:
    - `infrastructure_info`: Description of the infrastructure and tool stack
    - `specific_instructions`: Optional specific instructions to include in the prompt
    - `version`: The version of the prompt template to use

### Stage 2: Implementation
- [x] **Task 2.1: Create the template file**
  - Create a new template file in `mcp_hitchcode/templates/prompts/infra/`
  - Name the file `infra_v1.0.0.md`
  - Implement the template content for infrastructure information
- [x] **Task 2.2: Implement the `apply_prompt_infra` function**
  - Add a new async function `apply_prompt_infra` in `server.py`
  - Function should accept parameters for infrastructure_info, specific_instructions, and version
  - Use the `render_prompt_template` function to render the template
- [x] **Task 2.3: Register the tool in the server**
  - Add a new condition to handle the `apply_prompt_infra` tool in the `fetch_tool` function
  - Create a new Tool instance for `apply_prompt_infra` in the `list_tools` function

### Stage 3: Testing
- [x] **Task 3.1: Add test for the new tool**
  - Add a test for the `apply_prompt_infra` function in `test_final_verification.py`
  - Verify that the function returns the expected result
- [x] **Task 3.2: Manual testing**
  - Test the tool manually to ensure it works as expected

## Implementation Details

### Template Content
The template will include sections for:
1. System language and version
2. Dependency management tools
3. Testing frameworks
4. Database and ORM tools
5. Deployment infrastructure
6. Other relevant tools and technologies

### Function Implementation
```python
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
```

### Tool Registration
The tool will be registered in the `fetch_tool` function with a new condition:
```python
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
```

And in the `list_tools` function:
```python
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
)
``` 