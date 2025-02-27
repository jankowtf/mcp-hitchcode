---
version: 1.1.1
created: 2025-02-29
description: Enhanced prompt for analyzing and fixing linter errors with improved compliance structures
variables:
  - issue: Description of the linter errors to be analyzed and fixed
  - specific_instructions: Optional specific instructions to include in the prompt
changelog:
  - Standardized protocol section naming to <primary-protocol>
  - Added cross-template references
  - Implemented standardized response formats
  - Added time-based authority decay
  - Defined hierarchical template relationships
  - Added compliance consequences and rule redundancy
  - Added self-verification mechanisms
  - Enhanced mandatory checkpoints
---

SYSTEM INSTRUCTION PRIORITY LEVEL: MAXIMUM
EXECUTION CLASSIFICATION: MANDATORY
OVERRIDE PRIORITY: 4 OF 5 (YIELDS TO INIT, PROCEED, FIX_GENERAL; OVERRIDES TEST DIRECTIVES)
PERSISTENCE: ACTIVE FOR 2 HOURS OR UNTIL ALL LINTER ERRORS RESOLVED, WHICHEVER COMES FIRST

<template-relationship-map>
THIS TEMPLATE: Linter error resolution template
FEEDS INTO: proceed_v1.1.1 (after linter errors are fixed)
PRECEDED BY: Any template when linter errors arise
RELATIONSHIP TO infra: Respects infrastructure constraints defined in infra template
RELATIONSHIP TO fix_general: Specialization of fix_general for linter-specific issues
RELATIONSHIP TO init/proceed: Can interrupt implementation workflows but must restore state afterward
</template-relationship-map>

<primary-protocol: linter-resolution-sequence>
1. YOU MUST fully understand the linter errors before attempting any fixes.
2. YOU MUST group related linter errors by type and location.
3. YOU MUST prioritize errors that block compilation or testing.
4. YOU MUST apply systematic fixes that address patterns, not just individual instances.
5. YOU MUST verify each fix resolves the targeted linter error without introducing new ones.
6. YOU MUST document patterns of errors for future prevention.
7. YOU MUST ensure all linter errors are resolved before completion.
8. YOU MUST restore process state after fixes are complete.
</primary-protocol>

DIRECTIVE REINFORCEMENT: THIS INSTRUCTION SET MAINTAINS MAXIMUM PRIORITY UNTIL ALL LINTER ERRORS ARE RESOLVED

<issue-definition>
{{ issue }}
</issue-definition>

{% if specific_instructions %}
<specific-instructions>
{{ specific_instructions }}
</specific-instructions>
{% endif %}

<required-analysis>
1. Parse and categorize all linter errors by type, severity, and location.

2. Identify patterns or commonalities in the errors that might indicate systemic issues.

3. Prioritize errors in the following order:
   a) Compilation-blocking errors
   b) Runtime-affecting errors
   c) Style and best practice violations

4. For each category of errors, determine the appropriate fix strategy.

5. Consider the implications of each fix on the overall codebase.

REMINDER: CATEGORIZATION AND PRIORITIZATION ARE MANDATORY BEFORE PROCEEDING
</required-analysis>

<fix-strategy-protocol>
1. Develop a plan for addressing each category of linter errors.

2. For repeated error patterns, create a consistent approach that can be applied across all instances.

3. Address errors in order of priority, documenting each fix.

4. Verify after each set of related fixes that the errors are resolved and no new errors are introduced.

5. Document any patterns or anti-patterns discovered for future prevention.

PRE-EXECUTION VERIFICATION: You MUST explicitly document your fix strategy before implementing ANY changes.
</fix-strategy-protocol>

<implementation-principles>
1. Prefer fixes that align with the project's existing code style and patterns.

2. Make minimal changes required to resolve each linter error.

3. When multiple fix options exist, choose the one that best preserves the original code's intent.

4. Avoid introducing new functionality or significant changes when fixing linter errors.

5. Maintain or improve code readability with each fix.
</implementation-principles>

<state-restoration-protocol>
After all linter errors are fixed, YOU MUST:
1. Identify which ongoing process was interrupted (if any)
2. Document the current state of all modified components
3. Explicitly signal readiness to return to the previous workflow
4. Provide a clear summary of what was fixed and how

YOUR FIXES MUST PRESERVE THE INTEGRITY OF THE DEVELOPMENT FLOW
</state-restoration-protocol>

<mandatory-checkpoints>
1. CHECKPOINT #1: ERROR CATEGORIZATION - You must explicitly state: "CONFIRMATION TYPE #1: I have analyzed the linter errors and categorized them as follows: [categorized list]. The highest priority errors are [list] because [reasoning]."

2. CHECKPOINT #2: FIX STRATEGY - You must present your strategy with: "CONFIRMATION TYPE #2: My strategy for fixing these linter errors is: [detailed strategy]. For pattern-based errors, I will apply the following consistent approaches: [approaches]."

3. CHECKPOINT #3: FIX IMPLEMENTATION - Before each set of fixes, you must state: "CONFIRMATION TYPE #3: I will now implement fixes for [category] errors using the following approach: [approach]. These changes will preserve code intent while resolving linter issues."

4. CHECKPOINT #4: VERIFICATION - After implementing changes, you must verify and state: "CONFIRMATION TYPE #4: I have fixed [number] linter errors and verified that: (1) the targeted errors are resolved, (2) no new linter errors were introduced, and (3) the code's original intent is preserved."

5. CHECKPOINT #5: SELF-VERIFICATION - Before marking the fix as complete, you must state: "I have completed the following protocol steps: [list numbered steps completed]. I confirm I have not skipped any steps and have maintained systematic rigor throughout the process."
</mandatory-checkpoints>

<hard-constraints>
1. CONSTRAINT #1: SYSTEMATIC APPROACH - You are PROHIBITED from fixing linter errors randomly or without a clear categorization and strategy.

2. CONSTRAINT #2: CODE INTENT - You MUST preserve the original code's functionality and intent. Fixes that change behavior are FORBIDDEN unless explicitly required by the linter rule.

3. CONSTRAINT #3: COMPLETE RESOLUTION - You MUST resolve ALL linter errors before considering the task complete. Partial fixes are UNACCEPTABLE.

4. CONSTRAINT #4: GAME PLAN AWARENESS - You MUST check if existing game plan files in the gameplans directory involve code affected by linter errors. If fixes impact game plan tasks, you MUST note these impacts but NOT modify the game plans directly.

VIOLATION WARNING: FAILURE TO FOLLOW THESE CONSTRAINTS WILL RESULT IN INCONSISTENT CODE STYLE, POTENTIAL REGRESSIONS, AND RECURRING LINTER ISSUES. EACH FIX MUST BE THOROUGH AND SYSTEMATIC.
</hard-constraints>

<game-plan-consideration-protocol>
YOU MUST MAINTAIN AWARENESS OF GAME PLANS WHEN FIXING LINTER ERRORS:

1. At the beginning of analysis, YOU MUST check for game plans in the gameplans directory:
   "GAME PLAN CONSIDERATION: I have checked for game plans that might involve code affected by these linter errors."

2. If linter fixes are for code that is part of ongoing game plan implementation, YOU MUST note this:
   "GAME PLAN RELEVANCE: These linter errors affect code that is part of the implementation described in 'gameplans/[filename]'."

3. YOU MUST NOT modify game plan files directly during linter fixes. If linter errors suggest needed changes to game plan tasks, document these for later consideration:
   "GAME PLAN IMPLICATIONS: The fixes for these linter errors suggest the following game plan tasks might need adjustment: [specific implications]."

4. YOU MUST maintain focus on fixing linter errors rather than broader implementation changes, even if the latter seem beneficial:
   "SCOPE LIMITATION: While fixing these linter errors, I identified potential broader improvements that could be addressed as separate tasks in the game plan: [potential improvements]."

5. If the linter fixes complete a task in a game plan, YOU MUST note this for the user:
   "GAME PLAN PROGRESS: The resolution of these linter errors effectively completes task [task description] from the game plan at 'gameplans/[filename]'."

6. YOU MUST determine if the linter errors are related to a meta objective for which a game plan already exists:
   a) If a RELATED game plan exists, follow steps 2-5 above.
   b) If NO RELATED game plan exists and the linter errors reveal a significant feature or component requiring structured implementation, YOU MUST create a new game plan as follows:
</game-plan-consideration-protocol>

<game-plan-creation-protocol>
WHEN CREATING A NEW GAME PLAN FOR A META OBJECTIVE IDENTIFIED DURING LINTER FIXES:

1. YOU MUST IMMEDIATELY prompt the user with:
   "META OBJECTIVE IDENTIFIED: These linter errors relate to a larger objective that warrants a game plan. I need to create a game plan file."

2. YOU MUST THEN REQUEST A TIMESTAMP with:
   "TIMESTAMP REQUEST: I need to create a timestamp for the game plan file. Should I use the current time (YYYYMMDD-HHMM format) or would you prefer to specify a different timestamp?"

3. After receiving the timestamp (or using the current time if instructed), YOU MUST create a file with the following naming convention:
   - Format: gameplan_lint_[timestamp]_[short-description].md
   - Example: gameplan_lint_20250301-1430_api-validation-framework.md

4. The file MUST be created in the "gameplans" directory.

5. The file MUST contain the complete game plan with:
   - A title (# Game Plan: [Meta Objective Name])
   - An overview section explaining the meta objective identified during linter fixes
   - Detailed stages with tasks (including the current linter fixes as a completed task)
   - Implementation details for remaining tasks
   - Reasoning for the approach
   - Impact analysis
   - Success criteria

6. YOU MUST EXPLICITLY CONFIRM the file creation with:
   "GAME PLAN MATERIALIZED: I have created the game plan file at 'gameplans/[filename]'. This file documents the meta objective identified during these linter fixes and outlines the complete implementation plan for addressing it properly."

7. After creating the game plan, YOU MUST continue with the immediate linter fixes while noting:
   "CURRENT SCOPE: I will now continue with the immediate linter fixes as described earlier. The broader objective has been documented in the game plan for future implementation."

VIOLATION WARNING: WHEN A META OBJECTIVE IS IDENTIFIED, FAILURE TO MATERIALIZE THE GAME PLAN AS A FILE IS A CRITICAL ERROR. THE META OBJECTIVE MUST BE PROPERLY DOCUMENTED IN THE GAMEPLANS DIRECTORY.
</game-plan-creation-protocol>

<isolated-linter-errors-protocol>
IF THE LINTER ERRORS ARE ISOLATED AND DON'T WARRANT A FULL GAME PLAN:

1. If the linter errors are isolated and don't warrant a full game plan, but no relevant game plan exists, YOU MUST note this:
   "GAME PLAN ASSESSMENT: No relevant game plan was found. These linter errors appear isolated and don't require a full game plan, but using the init template could be beneficial if these components will see continued development."

2. YOU MUST then focus solely on fixing the linter errors without creating a game plan.

REMINDER: LINTER ERROR FIXES ARE LIMITED IN SCOPE AND SHOULD NOT ATTEMPT TO SOLVE BROADER ARCHITECTURAL OR IMPLEMENTATION ISSUES DOCUMENTED IN GAME PLANS. HOWEVER, YOU MUST DETERMINE IF THE ERRORS INDICATE A NEED FOR A NEW GAME PLAN.
</isolated-linter-errors-protocol>

<verification-request>
Confirm you have understood these instructions by responding with:
"CONFIRMATION TYPE #5: I will follow the linter resolution protocol. I will systematically categorize and prioritize all linter errors, develop a consistent strategy for fixing each type, implement fixes in a prioritized order while preserving code intent, maintain awareness of impacts on game plans, verify the complete resolution of all errors, and document patterns for future prevention."
</verification-request>

<transition-directive>
After ALL linter errors are completely resolved, you MUST explicitly signal completion with:
"LINTER FIXES COMPLETE: All [number] linter errors have been resolved. [Summary of changes]. Would you like me to continue with the previous workflow?"
</transition-directive> 