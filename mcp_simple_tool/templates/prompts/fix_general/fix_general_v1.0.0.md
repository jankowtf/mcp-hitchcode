---
version: 1.1.0
created: 2025-02-26
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

Issue: {{ issue }}

<your-task>
Do a step by step root cause analysis for the given issue(s). Then synthesize the necessary changes to fix the issue(s).

For the root cause analysis:
1. Identify the symptoms and their impact
2. Trace through the code execution path
3. Identify potential failure points
4. Determine the underlying cause
</your-task>

<your-agency>
Decide if this is related to a previous error and/or fix:
Case 1: If so, then use the respective game plan document and update it by adding stages. 

Case 2: If not, then create a new task-based (including checkboxes) game plan with stages. Use filename structure `gameplan_fix_<yyyymmdd-hhmm>_<id>.md` in directory @gameplans. IMPORTANT: Please ask me for the concrete timestamp to use and let me verify the ID before creating the game plan doc.

Make sure you also add your reasoning and top-level details/references on how to implement the fix(es) to the respective tasks in the game plan.

Also make sure you present me a management summary of your approach and the stages in the chat.
</your-agency>

<your-maxim-of-action>
1. Always choose the most straightforward implementation option. Be surgical and laser focused.

2. Make absolutely (!) sure you do not break existing code. Always (!) verify this by explicitly (!) reason about this aspect before proposing a code change. Always present your explicit reasoning on this.

3. Always (!) reconsider if the codebase actually works by double checking explicitly for logical flaws or forgotten code alignment. Always (!) present your explicit reasoning on this
</your-maxim-of-action>

{% if specific_instructions %}
<specific-instructions>
{{ specific_instructions }}
</specific-instructions>
{% endif %}

You never just proceed with implementing stages of the game plan, you always ask
for my confirmation for this 

THIS IS THE ACTUAL PROMPT FOR GUIDING YOUR NEXT STEPS.