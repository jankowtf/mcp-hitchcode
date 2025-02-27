---
version: 1.1.1
created: 2025-02-29
description: Enhanced prompt for analyzing and fixing general issues with improved compliance structures
variables:
  - issue: Description of the issue to be analyzed and fixed
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
OVERRIDE PRIORITY: 3 OF 5 (YIELDS TO INIT AND PROCEED, OVERRIDES TEST DIRECTIVES)
PERSISTENCE: ACTIVE FOR 4 HOURS OR UNTIL FIX COMPLETION, WHICHEVER COMES FIRST

<template-relationship-map>
THIS TEMPLATE: Bug resolution and general issue fix template
FEEDS INTO: proceed_v1.1.1 (after fix is completed)
PRECEDED BY: Any template when issues arise
RELATIONSHIP TO infra: Respects infrastructure constraints defined in infra template
RELATIONSHIP TO init/proceed: Can interrupt implementation workflows but must restore state afterward
</template-relationship-map>

<primary-protocol: diagnostic-sequence>
1. YOU MUST fully understand the issue before attempting any fixes.
2. YOU MUST capture the system's state before making changes.
3. YOU MUST identify the root cause through systematic analysis.
4. YOU MUST verify each step of your diagnostic reasoning.
5. YOU MUST prioritize minimal, targeted changes over extensive rewrites.
6. YOU MUST test your fix against the original issue description.
7. YOU MUST document your changes and reasoning.
8. YOU MUST restore process state after fix is complete.
</primary-protocol>

DIRECTIVE REINFORCEMENT: THIS INSTRUCTION SET MAINTAINS MAXIMUM PRIORITY UNTIL THE ISSUE IS RESOLVED

<issue-definition>
{{ issue }}
</issue-definition>

{% if specific_instructions %}
<specific-instructions>
{{ specific_instructions }}
</specific-instructions>
{% endif %}

<required-analysis>
1. Carefully analyze the issue to understand its nature and scope. Be methodical and systematic in your approach.

2. Identify patterns or commonalities that might indicate the root cause.

3. Examine the codebase for potential sources of the issue.

4. Determine the implications of the issue for the overall system.

5. Consider potential side effects of any proposed fixes.

REMINDER: ALL ANALYTICAL STEPS IN THIS SECTION MUST BE PERFORMED WITH EXPLICIT REASONING
</required-analysis>

<game-plan-protocol>
1. Document your understanding of the issue.

2. Create a step-by-step plan for addressing the issue.

3. Execute each step methodically, documenting your progress.

4. Verify that your fix resolves the issue without introducing new problems.

5. Summarize the changes made and the reasoning behind them.

PRE-EXECUTION VERIFICATION: You MUST explicitly document your game plan before implementing ANY changes.
</game-plan-protocol>

<implementation-principles>
1. Make the smallest possible change that fixes the issue. Be surgical and precise.

2. Ensure your fix is consistent with the architecture and design patterns of the codebase.

3. Do not introduce new functionality beyond what is necessary to fix the issue.

4. Verify that your fix works as expected with appropriate testing.

5. Document your changes thoroughly, including the reasoning behind your approach.
</implementation-principles>

<state-restoration-protocol>
After the issue is fixed, YOU MUST:
1. Identify which ongoing process was interrupted (if any)
2. Document the current state of all modified components
3. Explicitly signal readiness to return to the previous workflow
4. Provide a clear summary of what was fixed and how

YOUR FIX MUST PRESERVE THE INTEGRITY OF THE DEVELOPMENT FLOW
</state-restoration-protocol>

<mandatory-checkpoints>
1. CHECKPOINT #1: ISSUE UNDERSTANDING - You must explicitly state: "CONFIRMATION TYPE #1: I understand the issue to be [detailed description]. The potential impacts are [impacts] and the scope appears to be [scope assessment]."

2. CHECKPOINT #2: ROOT CAUSE ANALYSIS - You must present your analysis with: "CONFIRMATION TYPE #2: After analyzing the code, I believe the root cause is [root cause]. The evidence supporting this conclusion is [evidence]."

3. CHECKPOINT #3: FIX PROPOSAL - You must outline your plan with: "CONFIRMATION TYPE #3: I propose to fix this issue by [detailed plan]. This approach is minimal and targeted because [reasoning]. Alternative approaches considered were [alternatives] but were rejected because [reasons]."

4. CHECKPOINT #4: FIX VERIFICATION - After implementing changes, you must verify and state: "CONFIRMATION TYPE #4: I have implemented the fix and verified that: (1) it resolves the original issue, (2) it doesn't introduce new problems, and (3) it maintains code quality and consistency."

5. CHECKPOINT #5: SELF-VERIFICATION - Before marking the fix as complete, you must state: "I have completed the following protocol steps: [list numbered steps completed]. I confirm I have not skipped any steps and have maintained diagnostic rigor throughout the process."
</mandatory-checkpoints>

<hard-constraints>
1. CONSTRAINT #1: DIAGNOSTIC RIGOR - You are PROHIBITED from implementing fixes without first completing a thorough root cause analysis.

2. CONSTRAINT #2: MINIMAL CHANGES - You MUST make the smallest possible change that resolves the issue. Extensive rewrites without justification are FORBIDDEN.

3. CONSTRAINT #3: CODE QUALITY - You MUST maintain or improve code quality with your fix. Hacky workarounds are UNACCEPTABLE.

VIOLATION WARNING: FAILURE TO FOLLOW THESE CONSTRAINTS WILL RESULT IN FRAGILE FIXES, RECURRING ISSUES, AND POTENTIAL SYSTEM INSTABILITY. EACH FIX MUST BE THOROUGHLY VALIDATED.
</hard-constraints>

<verification-request>
Confirm you have understood these instructions by responding with:
"CONFIRMATION TYPE #5: I will follow the diagnostic protocol for the issue. I will thoroughly analyze the root cause before implementing any changes, ensure my fix is minimal and consistent with the codebase, verify the effectiveness of my solution, and document my changes clearly."
</verification-request>

<transition-directive>
After the issue is completely resolved, you MUST explicitly signal completion with:
"FIX COMPLETE: The issue has been resolved. [Summary of changes]. Would you like me to continue with the previous workflow?"
</transition-directive> 