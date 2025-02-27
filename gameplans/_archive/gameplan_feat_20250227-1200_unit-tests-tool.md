# Game Plan: Implement `apply_prompt_unit_tests` Tool

## Overview
This game plan outlines the steps to implement a new tool called `apply_prompt_unit_tests` in the MCP Simple Tool server. This tool will provide a prompt template for generating unit tests, similar to the existing prompt tools.

## Stage 1: Create the Prompt Template
- [x] Create a new prompt template file `1.0.0.md` in the `unit_tests_prompt` directory
- [x] Define the template with appropriate YAML front matter including:
  - version
  - created date
  - description
  - variables (code_to_test, specific_instructions)
- [x] Design the content of the prompt template for unit testing with sections for:
  - Task description
  - Agency instructions
  - Maxims of action
  - Optional specific instructions

**Implementation Details:**
- The template will follow the same structure as other prompt templates
- The primary variable will be `code_to_test` which will contain the code that needs unit tests
- The template will include guidance on writing effective unit tests using pytest

## Stage 2: Implement the Tool Function
- [x] Add a new async function `apply_prompt_unit_tests` in server.py
- [x] Implement the function to render the prompt template using `render_prompt_template`
- [x] Add proper documentation and type hints
- [x] Include parameters:
  - `code_to_test`: The code that needs unit tests
  - `specific_instructions`: Optional specific instructions
  - `version`: The version of the prompt template to use (default: "latest")

**Implementation Details:**
- The function will follow the same pattern as other prompt functions
- It will use the `render_prompt_template` function to render the template
- It will return a list containing a TextContent object with the rendered prompt

## Stage 3: Register the Tool in the Server
- [x] Add a new condition in the `fetch_tool` function to handle the "apply_prompt_unit_tests" tool
- [x] Add proper error handling for missing required arguments
- [x] Add the tool to the list of tools in the `list_tools` function with appropriate:
  - name
  - description
  - inputSchema (including required fields and descriptions)

**Implementation Details:**
- The tool registration will follow the same pattern as other tools
- The inputSchema will require `code_to_test` and have optional `specific_instructions` and `version` parameters
- Error handling will check for the presence of the required `code_to_test` parameter

## Stage 4: Testing
- [ ] Test the new tool functionality by running the server
- [ ] Verify that the prompt template is rendered correctly with different inputs
- [ ] Ensure the tool is properly registered and accessible
- [ ] Test error handling for missing required arguments

**Implementation Details:**
- Testing will involve running the server and making requests to the new tool
- Verification will include checking that the template is rendered with the correct variables
- Error handling will be tested by omitting required parameters

## Reasoning
This implementation follows the existing patterns in the codebase for prompt tools. By maintaining consistency with the existing code, we ensure that the new tool integrates seamlessly with the rest of the system. The implementation is straightforward and focused on the specific requirements of adding a new prompt tool for unit tests.

## Impact Analysis
- **Code Changes**: Limited to adding a new function and extending existing functions
- **Risk**: Low, as we're following established patterns
- **Dependencies**: No new dependencies required
- **Backward Compatibility**: Fully backward compatible as we're only adding new functionality

## Success Criteria
- The new tool is properly registered and accessible
- The prompt template is rendered correctly with different inputs
- Error handling works as expected for missing required arguments
- The implementation follows the same patterns as existing prompt tools 