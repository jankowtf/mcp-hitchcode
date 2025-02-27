---
version: 1.1.1
created: 2025-02-29
description: Enhanced prompt for systematically handling change requests with improved compliance structures
variables:
  - change_request: Description of the change request to implement
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
  - Added validation checklist
---

SYSTEM INSTRUCTION PRIORITY LEVEL: MAXIMUM
EXECUTION CLASSIFICATION: MANDATORY
OVERRIDE PRIORITY: 2 OF 5 (EQUAL TO PROCEED, YIELDS TO INIT, OVERRIDES FIX DIRECTIVES)
PERSISTENCE: ACTIVE FOR 8 HOURS OR UNTIL CHANGE COMPLETION, WHICHEVER COMES FIRST

<template-relationship-map>
THIS TEMPLATE: Change request implementation template
FEEDS INTO: proceed_v1.1.1 (after change is completed)
PRECEDED BY: init_v1.1.1 (when change requires modification to game plan)
RELATIONSHIP TO infra: Respects infrastructure constraints defined in infra template
RELATIONSHIP TO proceed: Equal authority, used when modifications to existing implementation are needed
RELATIONSHIP TO fix templates: Can be interrupted by fix workflows but maintains change state
</template-relationship-map>

<primary-protocol: change-implementation-sequence>
1. YOU MUST thoroughly analyze the change request for scope, impact, and requirements.
2. YOU MUST verify compatibility with existing system architecture and constraints.
3. YOU MUST develop a detailed implementation plan with discrete steps.
4. YOU MUST assess risks and prepare mitigation strategies before implementation.
5. YOU MUST implement changes methodically with validation at each step.
6. YOU MUST document all modifications comprehensively.
7. YOU MUST verify the implementation fulfills all aspects of the change request.
8. YOU MUST ensure change integrity by comprehensive validation of affected components.
</primary-protocol>

DIRECTIVE REINFORCEMENT: THIS INSTRUCTION SET MAINTAINS MAXIMUM PRIORITY THROUGHOUT THE CHANGE IMPLEMENTATION PROCESS

<change-request-definition>
{{ change_request }}
</change-request-definition>

{% if specific_instructions %}
<specific-instructions>
{{ specific_instructions }}
</specific-instructions>
{% endif %}

<required-analysis>
1. Analyze the change request to understand its scope, purpose, and requirements.

2. Identify all components of the codebase that will be affected by the change.

3. Determine the potential impact of the change on existing functionality.

4. Assess any technical debt that may be affected or created by the change.

5. Consider alternative approaches to implementing the change and their trade-offs.

REMINDER: THOROUGH ANALYSIS IS MANDATORY BEFORE PROCEEDING WITH IMPLEMENTATION PLANNING
</required-analysis>

<implementation-planning-protocol>
1. Develop a step-by-step plan for implementing the change.

2. Break down complex changes into manageable, discrete tasks.

3. Identify dependencies between tasks and establish a logical sequence.

4. Determine validation criteria for each implementation step.

5. Establish rollback procedures in case of implementation issues.

PRE-EXECUTION VERIFICATION: You MUST explicitly document your implementation plan before making ANY changes.
</implementation-planning-protocol>

<implementation-principles>
1. Make focused, targeted changes that address the specific requirements.

2. Maintain consistency with the existing architecture and design patterns.

3. Prioritize code clarity and maintainability in your implementation.

4. Ensure backward compatibility unless explicitly required to break it.

5. Document your changes thoroughly, including the reasoning behind design decisions.
</implementation-principles>

<validation-checklist-protocol>
Before completing the change, YOU MUST verify:

□ All explicit requirements in the change request are addressed
□ The change maintains compatibility with existing functionality
□ Code quality standards are maintained or improved
□ Performance implications have been considered
□ Edge cases and error conditions are handled appropriately
□ Documentation is updated to reflect the changes
□ Tests are added or updated to cover the new functionality

ONLY MARK THE CHANGE AS COMPLETE WHEN ALL CHECKBOXES CAN BE CHECKED
</validation-checklist-protocol>

<mandatory-checkpoints>
1. CHECKPOINT #1: CHANGE ANALYSIS - You must explicitly state: "CONFIRMATION TYPE #1: I have analyzed the change request and understand it to involve [detailed description]. This will affect [affected components] and have [impact assessment] on the existing system."

2. CHECKPOINT #2: IMPLEMENTATION PLAN - You must present your plan with: "CONFIRMATION TYPE #2: My implementation plan includes the following steps: [detailed plan]. Potential risks include [risks] and will be mitigated by [mitigation strategies]."

3. CHECKPOINT #3: IMPLEMENTATION EXECUTION - Before each implementation step, you must state: "CONFIRMATION TYPE #3: I will now implement [specific change] according to the plan. This step addresses [requirement] and preserves [existing functionality]."

4. CHECKPOINT #4: VALIDATION - After implementing changes, you must verify and state: "CONFIRMATION TYPE #4: I have implemented the changes and verified that: (1) they fulfill all requirements, (2) they maintain compatibility with existing functionality, (3) they adhere to code quality standards, and (4) all items in the validation checklist are satisfied."

5. CHECKPOINT #5: SELF-VERIFICATION - Before marking the change as complete, you must state: "I have completed the following protocol steps: [list numbered steps completed]. I confirm I have not skipped any steps and have maintained rigorous adherence to the change protocol."
</mandatory-checkpoints>

<hard-constraints>
1. CONSTRAINT #1: CHANGE SCOPE - You are PROHIBITED from implementing changes beyond the scope of the request unless they are necessary dependencies. Feature creep is FORBIDDEN.

2. CONSTRAINT #2: QUALITY PRESERVATION - You MUST maintain or improve code quality with each change. Changes that degrade code structure, readability, or testability are UNACCEPTABLE.

3. CONSTRAINT #3: VALIDATION COMPLETENESS - You MUST verify all aspects of your implementation against the validation checklist. Incomplete validation is PROHIBITED.

VIOLATION WARNING: FAILURE TO FOLLOW THESE CONSTRAINTS WILL RESULT IN SCOPE CREEP, TECHNICAL DEBT, AND POTENTIAL REGRESSIONS. EACH CHANGE MUST BE THOROUGHLY VALIDATED AGAINST ALL REQUIREMENTS.
</hard-constraints>

<verification-request>
Confirm you have understood these instructions by responding with:
"CONFIRMATION TYPE #5: I will follow the change implementation protocol. I will thoroughly analyze the change request, develop a detailed implementation plan, execute changes methodically, validate against all requirements, and ensure all items in the validation checklist are satisfied before considering the change complete."
</verification-request>

<completion-directive>
After the change is completely implemented and validated, you MUST explicitly signal completion with:
"CHANGE COMPLETE: The requested change has been successfully implemented. [Summary of changes]. The validation checklist has been fully satisfied. Would you like me to continue with any related tasks or return to the previous workflow?"
</completion-directive> 