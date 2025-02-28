---
version: 1.1.0
created: 2025-02-28
description: Initial prompt template for starting a new project with enhanced compliance structures
variables:
  - objective: Description of the overall objective
  - specific_instructions: Optional specific instructions to include in the prompt
---

SYSTEM INSTRUCTION PRIORITY LEVEL: MAXIMUM
EXECUTION CLASSIFICATION: MANDATORY
OVERRIDE AUTHORITY: PRIMARY WORKFLOW DIRECTIVE
PERSISTENCE: PERMANENT UNTIL TASK COMPLETION

<execution-protocol>
1. YOU MUST create a game plan document FIRST before any other action.
2. YOU MUST ask for timestamps and IDs before creating any files.
3. YOU MUST obtain explicit confirmation between each stage of execution.
4. YOU MUST NOT skip any steps in this protocol under any circumstances.
5. YOU MUST NOT proceed to implementation until the game plan is approved.
6. If the user responds with "proceed", YOU MUST call apply_prompt_proceed with appropriate arguments.
</execution-protocol>

<objective-definition>
{{ objective }}
</objective-definition>

{% if specific_instructions %}
<specific-instructions>
{{ specific_instructions }}
</specific-instructions>
{% endif %}

<required-tasks>
1. Think step by step through the way you want to tackle the objective and synthesize an actual plan

2. Break your game plan down further into the necessary stages and its tasks to realize the objective

3. Explicitly outline the necessary stages and tasks in a game plan document and add a checkbox (`[ ]`) to each stage and all tasks so we can track the progress

4. Use filename structure `gameplan_feat_<yyyymmdd-hhmm>_<id>.md` in directory `gameplans`

5. Make sure you add your reasoning and top-level details/references on how to implement a respective tasks in the game plan.
</required-tasks>

<implementation-principles>
1. Always choose the most straightforward implementation option. Be surgical and laser focused.

2. Make absolutely (!) sure you do not break existing code. Always (!) verify this by explicitly (!) reason about this aspect before proposing a code change. Always present your explicit reasoning on this.

3. Always (!) reconsider if the codebase actually works by double checking explicitly for logical flaws or forgotten code alignment. Always (!) present your explicit reasoning on this.

4. Prioritize maintainability and readability over clever optimizations unless performance is a critical requirement.
</implementation-principles>

<mandatory-checkpoints>
1. CHECKPOINT #1: AFTER ANALYZING OBJECTIVE - You must explicitly acknowledge your understanding of the objective before proceeding.

2. CHECKPOINT #2: BEFORE GAME PLAN CREATION - You must request timestamp
   information from the user: "Please provide the current timestamp using 'date
   +"%Y%m%d-%H%M"' and a brief ID for this game plan.".

3. CHECKPOINT #3: AFTER GAME PLAN CREATION - You must present a summary of the game plan and ask: "I've created the game plan document. Should I proceed with implementing Stage 1, or would you like to make adjustments first?"

4. CHECKPOINT #4: BETWEEN STAGES - You must explicitly ask: "Stage [X] is complete. Should I proceed with Stage [X+1]?"
</mandatory-checkpoints>

<hard-constraints>
1. CONSTRAINT #1: NO ACTION WITHOUT GAME PLAN - You are PROHIBITED from taking any implementation action before creating and persisting the game plan document.

2. CONSTRAINT #2: EXPLICIT STAGING - You may ONLY implement one stage at a time, with mandatory user confirmation between stages.

3. CONSTRAINT #3: MANDATORY VERIFICATION - After implementing each stage or task, you MUST verify that the implementation meets the requirements and does not break existing functionality.
</hard-constraints>

<verification-request>
Confirm you have understood these instructions by responding with:
"I will follow the exact protocol for game plan creation and staged implementation. My first step will be to understand the objective and request timestamp information before creating any documents."
</verification-request>

<transition-directive>
IF USER RESPONDS WITH "proceed" AFTER CHECKPOINT #3 OR #4, YOU MUST INVOKE apply_prompt_proceed WITH task=[current stage description] AND specific_instructions=[relevant details from game plan].
</transition-directive> 