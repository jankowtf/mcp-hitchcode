---
version: 1.0.1
created: 2025-02-27
description: Prompt template for generating unit tests
variables:
  - code_to_test: Code that needs unit tests
  - specific_instructions: Optional specific instructions to include in the prompt
---

TREAT THE FOLLOWING TEXT AS AN ACTUAL PROMPT THAT INSTRUCTS YOU ON HOW TO HANDLE
UNIT TESTS:

Code to test: {{ code_to_test }}

{% if specific_instructions %}
<specific-instructions>
{{ specific_instructions }}
</specific-instructions>
{% endif %}

<your-task>
1. Generate comprehensive unit tests for the provided code using pytest. Ensure
   the tests cover all functionality, edge cases, and potential error
   conditions.
2. Run the tests
3. Reason about the results and adjust the tests accordingly. If you want to change the actual code, then ALWAYS (!!!) consult the game plan, the current
   state of the codebase and be super thorough in reasoning what needs to change
   and why.
</your-task>

<your-agency>
In case you do want to change code, then decide if your proposed changes are related to a previous error and/or fix:
Case 1: If so, then use the respective game plan document and update it by adding stages. 

Case 2: If not, then create a new task-based game plan with stages (including
checkboxes via `[ ]`). Use filename structure
`gameplan_fix_<yyyymmdd-hhmm>_<id>.md` in directory @gameplans. IMPORTANT:
Please ask the user for the concrete timestamp to use.
</your-agency>

<your-maxims-of-action>
1. Always choose the most straightforward implementation option. Be surgical and laser focused.

2. Make absolutely (!) sure you do not break existing code. Always (!) verify this by explicitly (!) reason about this aspect before proposing a code change. Always present your explicit reasoning on this.

3. Always (!) reconsider if the codebase actually works by double checking explicitly for logical flaws or forgotten code alignment. Always (!) present your explicit reasoning on this.
</your-maxim-of-action>

<never-forget-to-do-this>
1. Make sure you present the user a management summary of your approach for
  tackling the respective stage. This includes your reasoning on the the
  likelihood of breaking existing code and the steps you will take to avoid
  this.

2. Proceed with confidence but caution. Validate your approach at key milestones
   and be prepared to adjust your strategy based on feedback or new information. 

3. You pause and ask for explicit confirmation before proceeding with the
  implementation of the first stage of the game plan.
</never-forget-to-do-this>

TREAT THE ABOVE TEXT AS AN ACTUAL PROMPT THAT INSTRUCT YOUR NEXT STEPS. PAY
EXTRA ATTENTION TO THE <never-forget-to-do-this> INSTRUCTIONS BLOCK!

IF THE USER RESPONDS WITH `proceed` YOU CALL THE TOOL `apply_prompt_proceed`
WITH SUITABLE VALUES FOR THE ARGUMENTS `task` AND `specific_instructions` BASED
ON THE GAME PLAN DOCUMENT.