# Game Plan: Implementing `apply_prompt_initial` Tool

## Overview
This game plan outlines the steps to implement a new tool called `apply_prompt_initial` in the MCP server. The tool will provide an initial prompt template to the agent, similar to the existing `apply_prompt_fix` tool. This implementation will follow the same pattern as the existing tool, leveraging the template loader mechanism.

## Stage 1: Analysis and Design

- [x] **Task 1.1: Understand the existing template loader mechanism**
  - Review the `template_loader.py` file to understand how templates are loaded and rendered
  - Understand how the `apply_prompt_fix` tool uses the template loader
  - Identify the necessary components for implementing a new template-based tool

- [x] **Task 1.2: Design the `apply_prompt_initial` tool**
  - **Function signature**: The tool will be an async function that returns a list of TextContent
  - **Input parameters**: The tool should accept a project description and optional version parameter
  - **Return value**: The tool will return the rendered prompt template as TextContent

- [x] **Task 1.3: Define the tool schema**
  - **Name**: `apply_prompt_initial`
  - **Description**: "Provides an initial prompt template for starting a new project"
  - **Input Schema**: Will require a "project" parameter to describe the project and an optional "version" parameter

**End of Stage 1**

## Stage 2: Template Creation

- [x] **Task 2.1: Create the template directory structure**
  - Create a new directory `initial_prompt` under `mcp_hitchcode/templates/prompts/`
  - This will follow the same pattern as the existing `fix_prompt` directory

- [x] **Task 2.2: Create the initial template version**
  - Create a file `1.0.0.md` in the new directory
  - Add YAML front matter with version, creation date, description, and variables
  - Implement the template content with Jinja2 variable placeholders

- [x] **Task 2.3: Verify template structure**
  - Ensure the template follows the same structure as existing templates
  - Verify that the YAML front matter is correctly formatted
  - Check that all necessary variables are defined in the front matter

**End of Stage 2**

## Stage 3: Tool Implementation

- [x] **Task 3.1: Implement the `apply_prompt_initial` function**
  - Create an async function that accepts project description and version parameters
  - Use the `render_prompt_template` function to render the template
  - Return the rendered template as TextContent

- [x] **Task 3.2: Register the tool in the `fetch_tool` function**
  - Add a new condition to handle the `apply_prompt_initial` tool
  - Extract the "project" and optional "version" parameters from the arguments
  - Call the implemented function with the extracted parameters

- [x] **Task 3.3: Add the tool to the `list_tools` function**
  - Create a new Tool instance for `apply_prompt_initial`
  - Define the input schema with the required "project" parameter and optional "version" parameter
  - Add a clear description of the tool's purpose

**End of Stage 3**

## Stage 4: Testing and Verification

- [x] **Task 4.1: Test the tool implementation**
  - Verify that the server starts correctly with the new tool
  - Test that the tool appears in the list of available tools
  - Test that the tool returns the expected prompt when called

- [x] **Task 4.2: Verify template rendering**
  - Ensure the template is correctly rendered with the provided project description
  - Verify that the version parameter works correctly
  - Check that the template variables are properly substituted

- [x] **Task 4.3: Final code review**
  - Check for any potential issues or edge cases
  - Ensure the implementation follows the existing code style
  - Verify that no existing functionality is broken

**End of Stage 4**

## Implementation Details

### Technical Approach
1. We'll create a new template directory and file following the existing pattern
2. We'll implement a new async function `apply_prompt_initial` that accepts project and version parameters
3. The function will use the existing `render_prompt_template` function to render the template
4. We'll update the `fetch_tool` function to handle the new tool
5. We'll add the tool to the `list_tools` function with appropriate schema

### Template Structure
The template will follow this structure:
```
---
version: 1.0.0
created: 2025-02-26
description: Initial prompt template for starting a new project
variables:
  - project: Description of the project to start
---

Project: {{ project }}

<template-content>
... Template content will be provided by the user ...
</template-content>
```

### Code Changes
1. Create new template file(s) in `mcp_hitchcode/templates/prompts/initial_prompt/`
2. Add new async function `apply_prompt_initial` in `server.py`
3. Update `fetch_tool` function to handle the new tool
4. Add the tool to the `list_tools` function

### Potential Challenges
1. Ensuring the template is correctly structured and rendered
2. Handling potential edge cases with the project parameter
3. Making sure the tool integrates properly with the existing MCP server 