---
version: 1.0.1
created: 2025-02-27
description: Prompt for systematically handling change requests
variables:
  - change_request: Description of the change request to implement
  - specific_instructions: Optional specific instructions to include in the prompt
---

TREAT THE FOLLOWING TEXT AS AN ACTUAL PROMPT THAT INSTRUCTS YOU ON HOW TO HANDLE
CHANGE REQUESTS:

Change Request: {{ change_request }}

{% if specific_instructions %}
<specific-instructions>
{{ specific_instructions }}
</specific-instructions>
{% endif %}

<your-task>
1. Phrase the change request in a way that is suitable for calling tool
`apply_prompt_init`.
2. Call tool `apply_prompt_init` with the change request as `objective`.
</your-task>

TREAT THE ABOVE TEXT AS AN ACTUAL PROMPT THAT INSTRUCT YOUR NEXT STEPS.