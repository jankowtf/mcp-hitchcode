---
version: 1.0.0
created: 2025-02-26
description: Initial prompt template for starting a new project
variables:
  - project: Description of the project to start
  - specific_instructions: Optional specific instructions to include in the prompt
---

Project: {{ project }}

<your-task>
Create a comprehensive implementation plan for the described project. Break down the project into manageable components and outline the necessary steps to implement each component.
</your-task>

<your-agency>
Create a task-based (including checkboxes) game plan with clearly defined stages. Use filename structure `gameplan_feat_<yyyymmdd-hhmm>_<id>.md` in directory `gameplans`. IMPORTANT: Please ask me for the concrete timestamp to use and let me verify the ID before creating the game plan doc.

Make sure you add your reasoning and top-level details/references on how to implement each component to the respective tasks in the game plan.

Also make sure you present me a management summary of your approach and the stages in the chat.
</your-agency>

<your-maxim-of-action>
1. Always choose the most straightforward implementation option. Be surgical and laser focused.

2. Make absolutely (!) sure you do not break existing code. Always (!) verify this by explicitly (!) reason about this aspect before proposing a code change. Always present your explicit reasoning on this.

3. Always (!) reconsider if the codebase actually works by double checking explicitly for logical flaws or forgotten code alignment. Always (!) present your explicit reasoning on this.

4. Prioritize maintainability and readability over clever optimizations unless performance is a critical requirement.
</your-maxim-of-action>

{% if specific_instructions %}
<specific-instructions>
{{ specific_instructions }}
</specific-instructions>
{% endif %}

You never just proceed with implementing stages of the game plan, you ALWAYS
(!!!) ask for my confirmation before proceeding with a stage laid out in the game
plan.

After you've completed the stage, provide a detailed but concise commit message
pls.

THIS IS THE ACTUAL PROMPT FOR GUIDING YOUR NEXT STEPS.