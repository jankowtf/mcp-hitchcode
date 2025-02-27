# Game Plan: Implementing `apply_prompt_fix` Tool

## Overview
This game plan outlines the steps to implement a new tool called `apply_prompt_fix` in the MCP server. The tool will provide a specific prompt to the agent for performing root cause analysis and fixing issues.

## Stage 1: Analysis and Design

- [x] **Task 1.1: Understand the current MCP server architecture**
  - The server is implemented using the MCP Python SDK
  - Tools are defined as async functions that return content lists
  - Tools are registered using decorators on the Server instance
  - Each tool has a name, description, and input schema

- [x] **Task 1.2: Design the `apply_prompt_fix` tool**
  - **Function signature**: The tool will be an async function that returns a list of TextContent
  - **Input parameters**: The tool should accept issue descriptions or context
  - **Return value**: The tool will return the predefined prompt as TextContent

- [x] **Task 1.3: Define the tool schema**
  - **Name**: `apply_prompt_fix`
  - **Description**: "Provides a prompt for performing root cause analysis and fixing issues"
  - **Input Schema**: Will require an "issue" parameter to describe the problem

**End of Stage 1**

## Stage 2: Implementation

- [x] **Task 2.1: Implement the `apply_prompt_fix` function**
  - Create an async function that returns the predefined prompt
  - Format the prompt as TextContent
  - Ensure the prompt is properly formatted and preserved

- [x] **Task 2.2: Register the tool in the `fetch_tool` function**
  - Add a new condition to handle the `apply_prompt_fix` tool
  - Extract the "issue" parameter from the arguments
  - Call the implemented function with the issue parameter

- [x] **Task 2.3: Add the tool to the `list_tools` function**
  - Create a new Tool instance for `apply_prompt_fix`
  - Define the input schema with the required "issue" parameter
  - Add a clear description of the tool's purpose

**End of Stage 2**

## Stage 3: Testing and Verification

- [x] **Task 3.1: Test the tool implementation**
  - Verify that the server starts correctly with the new tool
  - Test that the tool appears in the list of available tools
  - Test that the tool returns the expected prompt when called

- [x] **Task 3.2: Verify integration with MCP**
  - Ensure the tool can be called through the MCP interface
  - Verify that the prompt is properly formatted in the response

- [x] **Task 3.3: Final code review**
  - Check for any potential issues or edge cases
  - Ensure the implementation follows the existing code style
  - Verify that no existing functionality is broken

**End of Stage 3**

## Implementation Details

### Prompt Content
The tool will return the following prompt:
```
<your-task>
Do a step by step root cause analysis for the given issue(s). Then synthesize the necessary changes to fix the issue(s).
</your-task>

<your-agency>
Decide if this is related to a previous error and/or fix:
Case 1: If so, then use the respective game plan document and update it by adding stages. 

Case 2: If not, then create a new task-based (including checkboxes) game plan with stages. Use filename structure `gameplan_<yyyymmdd-hhmm>_<id>.md` in directory @gameplans. IMPORTANT: Please ask me for the concrete timestamp to use and let me verify the ID before creating the game plan doc.

Make sure you also add your reasoning and top-level details/references on how to implement the fix(es) to the respective tasks in the game plan.

Also make sure you present me a management summary of your approach and the stages in the chat.
</your-agency>

<your-maxim-of-action>
1. Always choose the most straightforward implementation option. Be surgical and laser focused.

2. Make absolutely (!) sure you do not break existing code. Always (!) verify this by explicitly (!) reason about this aspect before proposing a code change. Always present your explicit reasoning on this.

3. Always (!) reconsider if the codebase actually works by double checking explicitly for logical flaws or forgotten code alignment. Always (!) present your explicit reasoning on this
</your-maxim-of-action>

You never just proceed with implementing stages of the game plan, you always ask for my confirmation for this
```

### Technical Approach
1. We'll create a new async function `apply_prompt_fix` that accepts an issue parameter
2. The function will return the predefined prompt as TextContent
3. We'll update the `fetch_tool` function to handle the new tool
4. We'll add the tool to the `list_tools` function with appropriate schema

### Potential Challenges
1. Ensuring the prompt formatting is preserved in the response
2. Making sure the tool integrates properly with the existing MCP server
3. Handling potential edge cases with the issue parameter 