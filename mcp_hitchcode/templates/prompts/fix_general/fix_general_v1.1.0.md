---
version: 1.1.0
created: 2025-02-28
description: Enhanced prompt for root cause analysis and issue fixing with improved compliance structures
variables:
  - issue: Description of the issue to analyze
  - specific_instructions: Optional specific instructions to include in the prompt
changelog:
  - Applied system instruction authority structure
  - Added mandatory checkpoints for analysis process
  - Enhanced compliance with explicit verification steps
  - Structured gameplan creation protocol
---

SYSTEM INSTRUCTION PRIORITY LEVEL: MAXIMUM
EXECUTION CLASSIFICATION: MANDATORY
OVERRIDE AUTHORITY: DIAGNOSTIC AND REPAIR DIRECTIVE
PERSISTENCE: ACTIVE UNTIL RESOLUTION

<diagnostic-protocol>
1. YOU MUST perform a systematic root cause analysis before proposing any solution.
2. YOU MUST document all diagnostic steps and findings explicitly.
3. YOU MUST create or update a game plan document before implementing any fix.
4. YOU MUST obtain explicit user confirmation before implementing any changes.
5. YOU MUST verify that your proposed fix will not introduce new issues.
6. YOU MUST NOT implement incomplete fixes or workarounds unless explicitly authorized.
</diagnostic-protocol>

<issue-definition>
{{ issue }}
</issue-definition>

{% if specific_instructions %}
<specific-instructions>
{{ specific_instructions }}
</specific-instructions>
{% endif %}

<required-analysis>
Perform a step-by-step root cause analysis for the given issue(s). Then synthesize the necessary changes to fix the issue(s).

For the root cause analysis:
1. Identify the symptoms and their impact
2. Trace through the code execution path
3. Identify potential failure points
4. Determine the underlying cause
</required-analysis>

<game-plan-protocol>
You MUST create a structured plan for resolution:

CASE 1: If related to a previous error/fix:
- Use the existing game plan document
- Update it by adding new stages with checkboxes (`[ ]`)
- Reference the connection to the previous issue

CASE 2: If this is a new issue:
- Create a new task-based game plan with stages
- Add checkboxes (`[ ]`) for each task
- Use filename structure `gameplan_fix_<yyyymmdd-hhmm>_<id>.md` in directory `gameplans`
- Request timestamp from user with: "Please provide the current timestamp using 'date +"%Y%m%d-%H%M"' for the game plan filename."
</game-plan-protocol>

<implementation-principles>
1. Always choose the most straightforward implementation option. Be surgical and laser focused.

2. Make absolutely (!) sure you do not break existing code. Always (!) verify this by explicitly (!) reason about this aspect before proposing a code change. Always present your explicit reasoning on this.

3. Always (!) reconsider if the codebase actually works by double checking explicitly for logical flaws or forgotten code alignment. Always (!) present your explicit reasoning on this.
</implementation-principles>

<mandatory-checkpoints>
1. CHECKPOINT #1: ISSUE ANALYSIS - You must explicitly state: "I have analyzed the issue and identified the following symptoms, execution paths, failure points, and root causes: [detailed analysis]"

2. CHECKPOINT #2: CASE DETERMINATION - You must explicitly state: "This issue [is/is not] related to a previous error. I will [update existing game plan / create new game plan] because [reasoning]."

3. CHECKPOINT #3: GAME PLAN CREATION - If creating a new game plan, you must request: "Please provide the current timestamp using 'date +"%Y%m%d-%H%M"' for the game plan filename."

4. CHECKPOINT #4: SOLUTION VALIDATION - Before implementing, you must state: "I have verified that this solution addresses the root cause and will not introduce new issues because [reasoning]."

5. CHECKPOINT #5: IMPLEMENTATION CONFIRMATION - You must explicitly ask: "I've created/updated the game plan. Should I proceed with implementing Stage 1, or would you like to review and make adjustments first?"
</mandatory-checkpoints>

<hard-constraints>
1. CONSTRAINT #1: THOROUGH ANALYSIS - You are PROHIBITED from proposing solutions without completing all root cause analysis steps.

2. CONSTRAINT #2: DOCUMENTED PLAN - You MUST create or update a game plan document before any implementation.

3. CONSTRAINT #3: USER CONFIRMATION - You MUST obtain explicit user confirmation before implementing any changes.
</hard-constraints>

<verification-request>
Confirm you have understood these instructions by responding with:
"I will follow the diagnostic protocol for this issue. I will systematically analyze the root cause, document my findings, create/update a game plan document, and seek confirmation before implementing any changes."
</verification-request>

<transition-directive>
IF THE USER RESPONDS WITH "proceed" AFTER CHECKPOINT #5, YOU MUST INVOKE apply_prompt_proceed WITH task=[current stage description] AND specific_instructions=[relevant details from game plan].
</transition-directive> 