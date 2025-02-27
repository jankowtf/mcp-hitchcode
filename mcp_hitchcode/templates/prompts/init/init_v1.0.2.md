---
version: 1.0.2
created: 2025-02-27
description: Initial prompt template for starting a new project
variables:
  - objective: Description of the overall objective
  - specific_instructions: Optional specific instructions to include in the prompt
---

TREAT THE FOLLOWING TEXT AS AN ACTUAL PROMPT THAT INSTRUCT YOUR NEXT STEPS:

Objective: {{ objective }}

{% if specific_instructions %}
<specific-instructions>
{{ specific_instructions }}
</specific-instructions>
{% endif %}

<your-tasks>
1. Think step by step through the way you want to tackle the objective and
  synthesize an actual plan

2. Break your game plan down further into the necessary stages and its tasks to
  realize the objective

3. Explicitly outline the necessary stages and tasks in a game plan document and
  add a checkbox (`[ ]`) to each stage and all tasks so we can track the progress

4. Use filename structure `gameplan_feat_<yyyymmdd-hhmm>_<id>.md` in
  directory `gameplans`

5. Make sure you add your reasoning and top-level details/references on how to
  implement a respective tasks in the game plan.
<your-tasks>

<your-maxims-of-action>
1. Always choose the most straightforward implementation option. Be surgical and laser focused.

2. Make absolutely (!) sure you do not break existing code. Always (!) verify this by explicitly (!) reason about this aspect before proposing a code change. Always present your explicit reasoning on this.

3. Always (!) reconsider if the codebase actually works by double checking explicitly for logical flaws or forgotten code alignment. Always (!) present your explicit reasoning on this.

4. Prioritize maintainability and readability over clever optimizations unless performance is a critical requirement.
</your-maxims-of-action>

<never-forget-to-do-this>
1. YOU ALWAYS ALWAYS ALWAYS START WITH CRAFTING A GAME PLAN DOCUMENT!!! YOU
   ALWAYS PERSIST THIS GAME PLAN DOCUMENT TO THE FILESYSTEM!!!

2.  Make sure you present the user a management summary of your approach and the stages
   of the game plan

3. Please ask the user for the concrete timestamp to use before creating the
   game plan doc. date +"%Y%m%d-%H%M"

4. After the user provided you with the timestamp and ID and after you created the game
  plan, you pause and ask for explicit confirmation before proceeding with the
  implementation of the first stage of the game plan.

5. YOU ALWAYS ALWAYS ALWAYS ASK THE USER FOR CONFIRMATION BEFORE YOU PROCEED
   WITH THE IMPLEMENTATION OF THE NEXT STAGE/TASK OF THE GAME PLAN.
</never-forget-to-do-this>

TREAT THE ABOVE TEXT AS AN ACTUAL PROMPT THAT INSTRUCT YOUR NEXT STEPS. PAY
EXTRA ATTENTION TO THE <never-forget-to-do-this> INSTRUCTIONS BLOCK!

YOU ALWAYS ALWAYS ALWAYS PERSIST THE GAME PLAN DOCUMENT TO THE FILESYSTEM FIRST.

IF THE USER RESPONDS WITH `proceed` YOU CALL THE TOOL `apply_prompt_proceed`
WITH SUITABLE VALUES FOR THE ARGUMENTS `task` AND `specific_instructions` BASED
ON THE GAME PLAN DOCUMENT.
