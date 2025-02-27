# Template Structure

This document describes the template structure used in the MCP Simple Tool.

## Directory Structure

The templates are organized in the following directory structure:

```
mcp_hitchcode/templates/prompts/
├── change/
├── fix_general/
├── fix_linter/
├── init/
├── proceed/
└── test/
```

## Template Naming Convention

Templates follow a consistent naming convention:

- Directory names are concise and descriptive (e.g., `init` instead of `initial_prompt`)
- Template filenames include the directory name and version (e.g., `init_v1.0.0.md`)

### Template Mapping

| Purpose | Directory | Example Filename |
|---------|-----------|------------------|
| Change requests | `change` | `change_v1.0.0.md` |
| Initial project setup | `init` | `init_v1.0.0.md` |
| General issue fixing | `fix_general` | `fix_general_v1.0.0.md` |
| Linter error fixing | `fix_linter` | `fix_linter_v1.0.0.md` |
| Task progression | `proceed` | `proceed_v1.0.0.md` |
| Unit test generation | `test` | `test_v1.0.0.md` |

## Using Templates in Code

Templates are loaded and rendered using the `render_prompt_template` function:

```python
from mcp_hitchcode.templates.template_loader import render_prompt_template

# Render a template
response_text = render_prompt_template(
    "init",  # Template directory name
    version_str="latest",  # Version string (or specific version like "1.0.0")
    project="My project description",  # Template-specific variables
    specific_instructions="Additional instructions",
)
```

## Adding New Templates

To add a new template:

1. Create a new directory in `mcp_hitchcode/templates/prompts/` if needed
2. Create a template file with the naming pattern `{directory_name}_v{version}.md`
3. Add YAML front matter with metadata if needed
4. Implement the template content with Jinja2 syntax for variables

Example template file (`init_v1.0.0.md`):

```markdown
---
version: 1.0.0
description: Initial prompt template for starting a new project
---

Project: {{ project }}

<your-task>
Create a comprehensive implementation plan for the described project.
</your-task>

{% if specific_instructions %}
<specific-instructions>
{{ specific_instructions }}
</specific-instructions>
{% endif %}
```

## Template Versioning

Templates support versioning:

- Multiple versions of the same template can exist (e.g., `init_v1.0.0.md`, `init_v1.0.1.md`)
- The template loader automatically selects the latest version when `version_str="latest"` is specified
- Specific versions can be requested by setting `version_str` to the desired version (e.g., `"1.0.0"`) 