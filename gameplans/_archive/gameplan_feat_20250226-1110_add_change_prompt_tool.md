# Game Plan: Add `apply_prompt_change` Tool

**Date**: 2025-02-26
**Time**: 11:10
**ID**: add_change_prompt_tool

## Overview

This game plan outlines the implementation of a new tool called `apply_prompt_change` for systematically handling change requests in our MCP server. The tool will provide a prompt template similar to the existing ones (initial_prompt, proceed_prompt, fix_prompt) but specifically designed for change requests.

## Stages

### Stage 1: Create the prompt template ✅

- [x] Create directory structure for the change_prompt template
- [x] Create template file with version 1.0.0 with appropriate YAML front matter and content
- [x] Ensure template follows the same structure as existing templates

**Implementation Details:**
- Create directory `mcp_hitchcode/templates/prompts/change_prompt`
- Create file `1.0.0.md` with YAML front matter including version, creation date, description, and variables
- Template content should include sections for task description, agency instructions, and maxims of action
- Variables should include `change_request` and `specific_instructions`

### Stage 2: Implement the server-side function ✅

- [x] Add a new async function `apply_prompt_change` to handle the tool
- [x] Ensure it follows the same pattern as existing prompt functions

**Implementation Details:**
- Add function `apply_prompt_change` to `server.py` with parameters for change_request, specific_instructions, and version
- Function should call `render_prompt_template` with appropriate parameters
- Add proper docstring and type hints

### Stage 3: Register the tool ✅

- [x] Add the tool to the list of available tools in the `list_tools` function
- [x] Add handling for the tool in the `fetch_tool` function

**Implementation Details:**
- Add new `types.Tool` entry in the `list_tools` function with appropriate name, description, and input schema
- Add condition in the `fetch_tool` function to handle the "apply_prompt_change" tool name
- Ensure proper error handling for missing required arguments

### Stage 4: Test the implementation ✅

- [x] Test the tool to ensure it works as expected

**Implementation Details:**
- Test the tool with various inputs to ensure it renders the template correctly
- Verify error handling for missing required arguments

## Reasoning

The implementation follows the pattern established by the existing prompt tools (initial_prompt, proceed_prompt, fix_prompt). By maintaining consistency with the existing code structure, we ensure that the new tool integrates seamlessly with the rest of the codebase.

The change_prompt template will provide a structured approach to handling change requests, which will help users systematically plan and implement changes to their projects. 