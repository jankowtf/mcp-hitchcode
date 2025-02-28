---
version: 1.0.0
created: 2025-02-26
description: Prompt template for proceeding with a task or project
variables:
  - task: Description of the task or project to proceed with
  - specific_instructions: Optional specific instructions to include in the prompt
---



Task: {{ task }}

<your-task>
Proceed with the implementation according to the next stage/task in the game
plan. Execute them efficiently without breaking existing code.
</your-task>

<your-agency>
Implement the tasks with a methodical approach:
1. Analyze the current state and identify what has been completed so far
2. Determine the next logical steps to make progress
3. Execute those steps with precision and attention to detail
4. Document your changes and reasoning clearly

Focus on making tangible progress while maintaining code quality and consistency with the existing codebase.
</your-agency>

<your-maxim-of-action>
1. Always choose the most straightforward implementation option. Be surgical and laser focused.

2. Make absolutely (!) sure you do not break existing code. Always (!) verify this by explicitly (!) reason about this aspect before proposing a code change. Always present your explicit reasoning on this.

3. Always (!) reconsider if the codebase actually works by double checking explicitly for logical flaws or forgotten code alignment. Always (!) present your explicit reasoning on this.

4. Prioritize maintainability and readability over clever optimizations unless performance is a critical requirement.

5. When faced with multiple implementation options, choose the one that aligns best with the existing patterns in the codebase.
</your-maxim-of-action>

{% if specific_instructions %}
<specific-instructions>
{{ specific_instructions }}
</specific-instructions>
{% endif %}

Proceed with confidence but caution. Validate your approach at key milestones
and be prepared to adjust your strategy based on feedback or new information. 

After you've completed the stage, provide a detailed but concise commit message
pls.

THIS IS THE ACTUAL PROMPT FOR GUIDING YOUR NEXT STEPS.