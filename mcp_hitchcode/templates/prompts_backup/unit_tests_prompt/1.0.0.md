---
version: 1.0.0
created: 2025-02-27
description: Prompt template for generating unit tests
variables:
  - code_to_test: Code that needs unit tests
  - specific_instructions: Optional specific instructions to include in the prompt
---

Code to test: {{ code_to_test }}

<your-task>
Generate comprehensive unit tests for the provided code using pytest. Ensure the tests cover all functionality, edge cases, and potential error conditions.
</your-task>

<your-agency>
Run the test suite pls

Always choose the most straightforward implementation option for fixes that might arise.

Make sure you stick to the referenced game plan and update it accordingly once you implemented/finished a task
</your-agency>

<your-maxim-of-action>
1. Always choose the most straightforward implementation option. Be surgical and laser focused.

2. Make absolutely (!) sure you do not break existing code. Always (!) verify this by explicitly (!) reason about this aspect before proposing a code change. Always present your explicit reasoning on this.

3. Always (!) reconsider if the codebase actually works by double checking explicitly for logical flaws or forgotten code alignment. Always (!) present your explicit reasoning on this.
</your-maxim-of-action>

{% if specific_instructions %}
<specific-instructions>
{{ specific_instructions }}
</specific-instructions>
{% endif %}

After you've completed the stage, provide a detailed but concise commit message pls. 