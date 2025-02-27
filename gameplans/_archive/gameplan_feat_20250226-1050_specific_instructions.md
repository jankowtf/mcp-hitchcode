# Game Plan: Adding `specific_instructions` to All Prompt Templates

## Overview
This game plan outlines the steps to extend all prompt templates (`proceed_prompt`, `initial_prompt`, and `fix_prompt`) with a `<specific-instructions>` section. This enhancement will allow for customization within the template structure while maintaining clean function signatures. The implementation will follow the existing patterns in the codebase and ensure backward compatibility across all prompt tools.

## Stage 1: Analysis and Design
- [x] **Task 1.1: Analyze current template structures**
  - Review the existing prompt templates structure
  - Identify the appropriate location for the `<specific-instructions>` section in each template
  - Determine how to handle empty specific instructions gracefully

- [x] **Task 1.2: Design the implementation approach**
  - Design the updated function signatures for all `apply_prompt_*` functions
  - Plan how to maintain backward compatibility
  - Determine how to update the templates to include the new section

## Stage 2: Implementation for `apply_prompt_proceed`
- [x] **Task 2.1: Update the `apply_prompt_proceed` function**
  - Add a new optional parameter `specific_instructions` with empty string as default
  - Update the function to pass the new parameter to the template renderer
  - Ensure backward compatibility is maintained

- [x] **Task 2.2: Update the proceed_prompt template**
  - Add the `<specific-instructions>` section to the template
  - Ensure the section is properly formatted and positioned
  - Use Jinja2 templating to include the specific instructions

- [x] **Task 2.3: Update the tool handler for proceed_prompt**
  - Modify the `fetch_tool` function to handle the new parameter
  - Extract the optional `specific_instructions` parameter from arguments
  - Pass the parameter to the `apply_prompt_proceed` function

- [x] **Task 2.4: Update the tool registration for proceed_prompt**
  - Update the tool schema in the `list_tools` function
  - Add the new parameter to the input schema
  - Provide a clear description for the parameter

## Stage 3: Implementation for `apply_prompt_initial`
- [x] **Task 3.1: Update the `apply_prompt_initial` function**
  - Add a new optional parameter `specific_instructions` with empty string as default
  - Update the function to pass the new parameter to the template renderer
  - Ensure backward compatibility is maintained

- [x] **Task 3.2: Update the initial_prompt template**
  - Add the `<specific-instructions>` section to the template
  - Ensure the section is properly formatted and positioned
  - Use Jinja2 templating to include the specific instructions

- [x] **Task 3.3: Update the tool handler for initial_prompt**
  - Modify the `fetch_tool` function to handle the new parameter
  - Extract the optional `specific_instructions` parameter from arguments
  - Pass the parameter to the `apply_prompt_initial` function

- [x] **Task 3.4: Update the tool registration for initial_prompt**
  - Update the tool schema in the `list_tools` function
  - Add the new parameter to the input schema
  - Provide a clear description for the parameter

## Stage 4: Implementation for `apply_prompt_fix`
- [x] **Task 4.1: Update the `apply_prompt_fix` function**
  - Add a new optional parameter `specific_instructions` with empty string as default
  - Update the function to pass the new parameter to the template renderer
  - Ensure backward compatibility is maintained

- [x] **Task 4.2: Update the fix_prompt template**
  - Add the `<specific-instructions>` section to the template
  - Ensure the section is properly formatted and positioned
  - Use Jinja2 templating to include the specific instructions

- [x] **Task 4.3: Update the tool handler for fix_prompt**
  - Modify the `fetch_tool` function to handle the new parameter
  - Extract the optional `specific_instructions` parameter from arguments
  - Pass the parameter to the `apply_prompt_fix` function

- [x] **Task 4.4: Update the tool registration for fix_prompt**
  - Update the tool schema in the `list_tools` function
  - Add the new parameter to the input schema
  - Provide a clear description for the parameter

## Stage 5: Testing and Documentation
- [ ] **Task 5.1: Test the implementations**
  - Test each prompt tool with specific instructions provided
  - Test each prompt tool with empty specific instructions
  - Verify backward compatibility for all tools

- [ ] **Task 5.2: Update documentation**
  - Document the new parameter in all function docstrings
  - Update any relevant documentation

## Implementation Details

### Task 2.1: Update the `apply_prompt_proceed` function
```python
async def apply_prompt_proceed(
    task: str,
    specific_instructions: str = "",  # New optional parameter
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
        "proceed_prompt", 
        version_str=version, 
        task=task,
        specific_instructions=specific_instructions
    )
    return [types.TextContent(type="text", text=response_text)]
```

### Task 3.1: Update the `apply_prompt_initial` function
```python
async def apply_prompt_initial(
    project: str,
    specific_instructions: str = "",  # New optional parameter
    version: str = "latest",
) -> list[types.TextContent]:
    """
    Provides an initial prompt template for starting a new project.

    Args:
        project: A description of the project to start.
        specific_instructions: Optional specific instructions to include in the prompt.
        version: The version of the prompt template to use. Defaults to "latest".

    Returns:
        A list containing a TextContent object with the prompt.
    """
    # Render the prompt template with the project description and specific instructions
    response_text = render_prompt_template(
        "initial_prompt", 
        version_str=version, 
        project=project,
        specific_instructions=specific_instructions
    )
    return [types.TextContent(type="text", text=response_text)]
```

### Task 4.1: Update the `apply_prompt_fix` function
```python
async def apply_prompt_fix(
    issue: str,
    specific_instructions: str = "",  # New optional parameter
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
        "fix_prompt", 
        version_str=version, 
        issue=issue,
        specific_instructions=specific_instructions
    )
    return [types.TextContent(type="text", text=response_text)]
```

### Template Updates
For each template, add the `<specific-instructions>` section:
```markdown
<specific-instructions>
{{ specific_instructions }}
</specific-instructions>
```

### Tool Handler Updates
Update the `fetch_tool` function for each prompt tool:
```python
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
        version=version
    )
elif name == "apply_prompt_initial":
    if "project" not in arguments:
        return [
            types.TextContent(
                type="text", text="Error: Missing required argument 'project'"
            )
        ]
    version = arguments.get("version", "latest")
    specific_instructions = arguments.get("specific_instructions", "")
    return await apply_prompt_initial(
        arguments["project"], 
        specific_instructions=specific_instructions,
        version=version
    )
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
        arguments["issue"], 
        specific_instructions=specific_instructions,
        version=version
    )
```

### Tool Registration Updates
Update the tool schema in the `list_tools` function for each prompt tool:
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
```

Similar updates for the other prompt tools.

## Reasoning
This implementation approach:
1. Maintains backward compatibility by making the new parameter optional with an empty string default
2. Follows the existing patterns in the codebase
3. Keeps the function interfaces clean
4. Makes it obvious in the templates where custom instructions go
5. Leverages the existing templating system without requiring changes to the core functionality
6. Provides a consistent experience across all prompt tools 