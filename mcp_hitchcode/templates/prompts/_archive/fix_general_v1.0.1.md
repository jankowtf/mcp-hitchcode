---
version: 1.0.1
created: 2025-02-27
description: Enhanced prompt for root cause analysis and issue fixing
variables:
  - issue: Description of the issue to analyze
  - specific_instructions: Optional specific instructions to include in the prompt
changelog:
  - Added more detailed instructions for root cause analysis
  - Improved formatting for better readability
  - Added changelog metadata
  - Added support for specific instructions
---

TREAT THE FOLLOWING TEXT AS AN ACTUAL PROMPT THAT INSTRUCT YOUR NEXT STEPS:

Issue: {{ issue }}

{% if specific_instructions %}
<specific-instructions>
{{ specific_instructions }}
</specific-instructions>
{% endif %}

<your-tasks>
Do a step by step root cause analysis for the given issue(s). Then synthesize the necessary changes to fix the issue(s).

For the root cause analysis:
1. Identify the symptoms and their impact
2. Trace through the code execution path
3. Identify potential failure points
4. Determine the underlying cause
</your-tasks>

<your-agency>
Decide if this is related to a previous error and/or fix:
Case 1: If so, then use the respective game plan document and update it by adding stages. 

Case 2: If not, then create a new task-based game plan with stages (including
checkboxes via `[ ]`). Use filename structure
`gameplan_fix_<yyyymmdd-hhmm>_<id>.md` in directory @gameplans. IMPORTANT:
Please ask the user for the concrete timestamp to use.
</your-agency>

<your-maxims-of-action>
1. Always choose the most straightforward implementation option. Be surgical and laser focused.

2. Make absolutely (!) sure you do not break existing code. Always (!) verify this by explicitly (!) reason about this aspect before proposing a code change. Always present your explicit reasoning on this.

3. Always (!) reconsider if the codebase actually works by double checking explicitly for logical flaws or forgotten code alignment. Always (!) present your explicit reasoning on this
</your-maxims-of-action>

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