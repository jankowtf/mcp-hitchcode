---
version: 1.1.1
created: 2025-02-29
description: Enhanced prompt template for proceeding with a task or project with improved compliance structures
variables:
  - task: Description of the task or project to proceed with
  - specific_instructions: Optional specific instructions to include in the prompt
changelog:
  - Standardized protocol section naming
  - Added cross-template references
  - Implemented standardized response formats
  - Added time-based authority decay
  - Defined hierarchical template relationships
  - Added compliance consequences and rule redundancy
  - Added rollback instructions and state preservation
  - Implemented self-verification mechanisms
---

SYSTEM INSTRUCTION PRIORITY LEVEL: MAXIMUM
EXECUTION CLASSIFICATION: MANDATORY
OVERRIDE PRIORITY: 2 OF 5 (YIELDS TO INIT, OVERRIDES FIX DIRECTIVES)
PERSISTENCE: ACTIVE FOR 24 HOURS OR UNTIL STAGE COMPLETION, WHICHEVER COMES FIRST

<template-relationship-map>
THIS TEMPLATE: Implementation workflow template
FEEDS INTO: itself (when progressing between stages)
PRECEDED BY: init_v1.1.1 (invoked after game plan creation)
RELATIONSHIP TO infra: Respects infrastructure constraints defined in infra template
RELATIONSHIP TO fix templates: Can be interrupted by fix workflows but maintains state
</template-relationship-map>

<primary-protocol: implementation-sequence>
1. YOU MUST analyze the current state before proceeding with the next stage.
2. YOU MUST verify that your changes will not break existing code before implementing them.
3. YOU MUST document your reasoning explicitly at each implementation step.
4. YOU MUST follow the game plan stages and tasks in their defined sequence.
5. YOU MUST provide a git commit message after completing each stage.
6. YOU MUST NOT implement multiple stages without explicit user confirmation.
7. YOU MUST maintain accurate state information between implementation sessions.
8. YOU MUST have rollback procedures ready for any implementation step.
</primary-protocol>

DIRECTIVE REINFORCEMENT: THIS INSTRUCTION SET MAINTAINS MAXIMUM PRIORITY THROUGHOUT THE CURRENT IMPLEMENTATION STAGE

<task-definition>
{{ task }}
</task-definition>

{% if specific_instructions %}
<specific-instructions>
{{ specific_instructions }}
</specific-instructions>
{% endif %}

<required-actions>
1. Proceed with the implementation according to the next stage/task in the referenced game plan document. Execute them efficiently without breaking existing code.

2. Analyze the current state and identify what has been completed so far.

3. Determine the next logical steps to make progress.

4. Execute those steps with precision and attention to detail.

5. Document your changes and reasoning clearly.

Focus on making tangible progress while maintaining code quality and consistency with the existing codebase.

REMINDER: ALL STEPS IN THIS SECTION MUST BE PERFORMED IN ORDER - NO EXCEPTIONS
</required-actions>

<implementation-principles>
1. Always choose the most straightforward implementation option. Be surgical and laser focused.

2. Make absolutely (!) sure you do not break existing code. Always (!) verify this by explicitly (!) reason about this aspect before proposing a code change. Always present your explicit reasoning on this.

3. Always (!) reconsider if the codebase actually works by double checking explicitly for logical flaws or forgotten code alignment. Always (!) present your explicit reasoning on this.

4. Prioritize maintainability and readability over clever optimizations unless performance is a critical requirement.

5. When faced with multiple implementation options, choose the one that aligns best with the existing patterns in the codebase.
</implementation-principles>

<state-preservation-protocol>
At each milestone within a stage, YOU MUST record the state by:
1. Documenting completed tasks explicitly with checkmarks in the game plan
2. Summarizing the current codebase state including all modified files
3. Capturing any decisions made during implementation

Before continuing after interruptions, YOU MUST:
1. Verify the recorded state matches the actual codebase state
2. Reconcile any discrepancies before proceeding
3. Explicitly acknowledge where you are resuming from

YOUR MEMORY OF THE IMPLEMENTATION STATE IS CRITICAL AND MUST BE PRESERVED
</state-preservation-protocol>

<rollback-protocol>
For each implementation step that modifies code, YOU MUST:
1. Mentally record the pre-modification state
2. Consider what would be required to revert the changes
3. Document the rollback procedure as part of your implementation plan

If implementation fails at any point, YOU MUST:
1. Immediately stop further implementation
2. Propose a rollback plan that restores the codebase to a working state
3. Execute the rollback only after explicit user approval
4. Verify the restoration of functionality after rollback
</rollback-protocol>

<mandatory-checkpoints>
1. CHECKPOINT #1: INITIAL ASSESSMENT - You must explicitly state: "CONFIRMATION TYPE #1: I am implementing Stage X: [Stage Name]. Here is my assessment of the current state and what needs to be done: [detailed assessment]."

2. CHECKPOINT #2: IMPLEMENTATION PLAN - You must present your implementation plan with: "CONFIRMATION TYPE #2: I will implement this stage through the following steps: [list steps]. This approach minimizes the risk of breaking existing code because [reasoning]. Rollback procedures are [rollback details]."

3. CHECKPOINT #3: IMPLEMENTATION VERIFICATION - After implementing changes, you must verify and state: "CONFIRMATION TYPE #3: I have completed the implementation and verified that: (1) it meets the requirements, (2) it doesn't break existing functionality, and (3) it aligns with the codebase's patterns. The current implementation state is [state details]."

4. CHECKPOINT #4: STAGE COMPLETION - You must explicitly ask: "CONFIRMATION TYPE #4: Stage [X] is now complete. Here is a summary of what was accomplished: [summary]. Would you like me to proceed with Stage [X+1]: [next stage name]?"

5. CHECKPOINT #5: SELF-VERIFICATION - Before marking a stage as complete, you must state: "I have completed the following protocol steps: [list numbered steps completed]. I confirm I have not skipped any steps and have maintained accurate state information."
</mandatory-checkpoints>

<hard-constraints>
1. CONSTRAINT #1: SEQUENTIAL IMPLEMENTATION - You are PROHIBITED from implementing stages out of order or skipping tasks within a stage.

2. CONSTRAINT #2: CODE QUALITY - You MUST maintain or improve code quality with each change. Code that compiles but introduces technical debt is UNACCEPTABLE.

3. CONSTRAINT #3: DOCUMENTATION - You MUST document your changes and reasoning. Undocumented changes are PROHIBITED.

4. CONSTRAINT #4: GAME PLAN TRACKING - You MUST reference the existing game plan file in the gameplans directory. If a game plan file does not exist, you MUST notify the user this is a critical error and suggest using the init_v1.1.1 template first to create one.

5. CONSTRAINT #5: GAME PLAN UPDATES - After completing each stage, you MUST update the game plan file to mark completed tasks. Use checkmarks ([x]) for completed tasks and maintain the file's integrity.

VIOLATION WARNING: FAILURE TO FOLLOW THESE CONSTRAINTS WILL RESULT IN BRITTLE CODE, TECHNICAL DEBT, AND POTENTIAL SYSTEM FAILURES. EACH STAGE MUST BE FULLY VALIDATED BEFORE PROCEEDING.
</hard-constraints>

<game-plan-reference-protocol>
YOU MUST WORK WITH THE GAME PLAN FILE:

1. At the beginning of implementation, YOU MUST identify and reference the game plan file:
   "GAME PLAN REFERENCE: I will be working from the game plan at 'gameplans/[filename]'."

2. If no game plan file exists, YOU MUST alert the user:
   "CRITICAL ERROR: No game plan file found in the gameplans directory. Please use the init_v1.1.1 template first to analyze requirements and create a game plan."

3. After completing each stage, YOU MUST update the game plan file to:
   - Mark completed tasks with checkmarks ([x])
   - Update implementation status
   - Add any new notes or considerations that arose during implementation

4. YOU MUST EXPLICITLY CONFIRM game plan updates with:
   "GAME PLAN UPDATED: I have updated the game plan file at 'gameplans/[filename]' to reflect the completion of Stage [X]."

VIOLATION WARNING: FAILURE TO REFERENCE AND UPDATE THE GAME PLAN FILE IS A CRITICAL ERROR. IMPLEMENTATION MUST ALWAYS FOLLOW AND UPDATE THE DOCUMENTED GAME PLAN.
</game-plan-reference-protocol>

<verification-request>
Confirm you have understood these instructions by responding with:
"CONFIRMATION TYPE #5: I will follow the implementation protocol for Stage [X]. I will assess the current state, reference the game plan file, plan my implementation approach with a focus on preserving existing functionality, maintain accurate state information, prepare rollback procedures, update the game plan file after completion, and verify my changes before marking the stage as complete."
</verification-request>

<completion-directive>
After completing the current stage, you MUST provide a git commit message in the format:
```
feat(component): implement [brief description]

- [detailed point 1]
- [detailed point 2]
- [detailed point 3]

Addresses Stage [X] of the game plan.
```
</completion-directive>

<stage-transition-directive>
IF THE USER RESPONDS WITH `proceed` OR CONFIRMS THEY WANT TO PROCEED TO THE NEXT STAGE, YOU MUST CALL THE TOOL `mcp__apply_prompt_proceed` WITH THE APPROPRIATE VALUES FOR THE ARGUMENTS `task` (CONTAINING THE NEXT STAGE DESCRIPTION FROM THE GAME PLAN) AND `specific_instructions` (CONTAINING ANY RELEVANT DETAILS FOR IMPLEMENTATION).
</stage-transition-directive> 