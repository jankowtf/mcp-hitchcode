# Game Plan: Implementing Templating System for `get_prompt_fix` Tool

## Overview
This game plan outlines the steps to implement a templating system for the `get_prompt_fix` tool in the MCP server. The goal is to decouple prompt content from the tool implementation by using a best-in-class templating framework and storing templates in separate files.

## Stage 1: Analysis and Design

- [x] **Task 1.1: Research and select the best templating framework**
  - **Options Analysis**:
    - **Jinja2**: Industry standard, powerful, flexible, widely used
    - **Mako**: High performance, similar to Jinja2 but with different syntax
    - **string.Template**: Simple built-in solution, limited features
    - **Pydantic Templates**: Modern, type-safe, but might be overkill
  - **Recommendation**: Jinja2 is the most appropriate choice due to its widespread adoption, excellent documentation, and powerful features

- [x] **Task 1.2: Design the template directory structure**
  - Create a `templates` directory within the `mcp_simple_tool` package
  - Organize templates by tool or functionality
  - Ensure the structure is scalable for future template additions

- [x] **Task 1.3: Choose the template file format**
  - **Options Analysis**:
    - **Markdown (.md)**: Good for text-heavy content, supports formatting
    - **YAML (.yaml)**: Structured, supports complex data, good for parameterization
    - **TOML (.toml)**: More readable than YAML, good for configuration
  - **Recommendation**: Markdown (.md) with Jinja2 templating is ideal for prompt templates as they are primarily text with minimal structured data

- [x] **Task 1.4: Design the template loading mechanism**
  - Create a template loader that finds templates in the package
  - Implement caching to avoid repeated file I/O
  - Design a clean API for rendering templates with variables

**End of Stage 1**

## Stage 2: Implementation

- [x] **Task 2.1: Set up the template directory structure**
  - Create the `templates` directory in the package
  - Add necessary subdirectories for organization
  - Ensure the directory is included in the package distribution

- [x] **Task 2.2: Create the prompt template file**
  - Create a template file for the `get_prompt_fix` tool
  - Convert the existing prompt to the template format
  - Add appropriate variables and placeholders

- [x] **Task 2.3: Implement the template loading mechanism**
  - Create a module for template management
  - Implement functions to load and render templates
  - Add error handling for missing templates

- [x] **Task 2.4: Update the `get_prompt_fix` function**
  - Modify the function to use the template system
  - Pass the issue parameter to the template renderer
  - Ensure the output format remains compatible with the MCP system

**End of Stage 2**

## Stage 3: Testing and Verification

- [x] **Task 3.1: Test the template loading mechanism**
  - Verify that templates are correctly loaded from the package
  - Test error handling for missing or invalid templates
  - Ensure template caching works as expected

- [x] **Task 3.2: Test the `get_prompt_fix` function**
  - Verify that the function correctly renders the template
  - Test with various issue descriptions
  - Ensure the output format is compatible with the MCP system

- [x] **Task 3.3: Verify package distribution**
  - Ensure templates are included when the package is installed
  - Test the system in a clean environment
  - Verify that the package works correctly when installed

**End of Stage 3**

## Implementation Details

### Template Directory Structure
```
mcp_simple_tool/
├── __init__.py
├── __main__.py
├── server.py
└── templates/
    ├── __init__.py
    └── prompts/
        └── fix_prompt.md
```

### Template Loading Mechanism
We'll create a `template_loader.py` module with the following functionality:
- A function to locate and load templates from the package
- A caching mechanism to avoid repeated file I/O
- A render function that applies template variables

### Template Format (Markdown with Jinja2)
The template will use Markdown for content structure with Jinja2 syntax for variable substitution:

```markdown
Issue: {{ issue }}

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

### Dependencies
- Jinja2: For template rendering
- Package resources: For accessing templates within the package

### Potential Challenges
1. Ensuring templates are correctly included in the package distribution
2. Handling template loading errors gracefully
3. Maintaining backward compatibility with the existing MCP system 