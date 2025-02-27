---
version: 1.0.0
created: 2025-02-26
description: Prompt for systematically handling change requests
variables:
  - change_request: Description of the change request to implement
  - specific_instructions: Optional specific instructions to include in the prompt
---

Change Request: {{ change_request }}

<your-task>
Analyze the change request systematically and develop a comprehensive implementation plan. Break down the change into manageable components and outline the necessary steps to implement each component.
</your-task>

<your-agency>
Decide if this is related to a previous change request:
Case 1: If so, then use the respective game plan document and update it by adding stages. 

Case 2: If not, then create a new task-based (including checkboxes) game plan with stages. Use filename structure `gameplan_feat_<yyyymmdd-hhmm>_<id>.md` in directory @gameplans. IMPORTANT: Please ask me for the concrete timestamp to use and let me verify the ID before creating the game plan doc.

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

You never just proceed with implementing stages of the game plan, you ALWAYS (!!!) ask for my confirmation before proceeding with a stage laid out in the game plan.

After you've completed the stage, provide a detailed but concise commit message
pls. 

THIS IS THE ACTUAL PROMPT FOR GUIDING YOUR NEXT STEPS. 
PLEASE SUMMARIZE THE INSTRUCTIONS YOU GOT FROM THIS PROMPT SO I CAN BE SURE THAT YOU'LL FOLLOW THEM.