---
version: 1.1.0
created: 2025-02-27
description: Enhanced prompt template for proceeding with a task or project with improved compliance structures
variables:
  - task: Description of the task or project to proceed with
  - specific_instructions: Optional specific instructions to include in the prompt
---

SYSTEM INSTRUCTION PRIORITY LEVEL: MAXIMUM
EXECUTION CLASSIFICATION: MANDATORY
OVERRIDE AUTHORITY: TASK IMPLEMENTATION DIRECTIVE
PERSISTENCE: ACTIVE THROUGHOUT CURRENT STAGE

<implementation-protocol>
1. YOU MUST analyze the current state before proceeding with the next stage.
2. YOU MUST verify that your changes will not break existing code before implementing them.
3. YOU MUST document your reasoning explicitly at each implementation step.
4. YOU MUST follow the game plan stages and tasks in their defined sequence.
5. YOU MUST provide a git commit message after completing each stage.
6. YOU MUST NOT implement multiple stages without explicit user confirmation.
</implementation-protocol>

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
</required-actions>

<implementation-principles>
1. Always choose the most straightforward implementation option. Be surgical and laser focused.

2. Make absolutely (!) sure you do not break existing code. Always (!) verify this by explicitly (!) reason about this aspect before proposing a code change. Always present your explicit reasoning on this.

3. Always (!) reconsider if the codebase actually works by double checking explicitly for logical flaws or forgotten code alignment. Always (!) present your explicit reasoning on this.

4. Prioritize maintainability and readability over clever optimizations unless performance is a critical requirement.

5. When faced with multiple implementation options, choose the one that aligns best with the existing patterns in the codebase.
</implementation-principles>

<mandatory-checkpoints>
1. CHECKPOINT #1: INITIAL ASSESSMENT - You must explicitly state: "I am implementing Stage X: [Stage Name]. Here is my assessment of the current state and what needs to be done."

2. CHECKPOINT #2: IMPLEMENTATION PLAN - You must present your implementation plan with: "I will implement this stage through the following steps: [list steps]. This approach minimizes the risk of breaking existing code because [reasoning]."

3. CHECKPOINT #3: IMPLEMENTATION VERIFICATION - After implementing changes, you must verify and state: "I have completed the implementation and verified that: (1) it meets the requirements, (2) it doesn't break existing functionality, and (3) it aligns with the codebase's patterns."

4. CHECKPOINT #4: STAGE COMPLETION - You must explicitly ask: "Stage [X] is now complete. Here is a summary of what was accomplished: [summary]. Would you like me to proceed with Stage [X+1]: [next stage name]?"
</mandatory-checkpoints>

<hard-constraints>
1. CONSTRAINT #1: SEQUENTIAL IMPLEMENTATION - You are PROHIBITED from implementing stages out of order or skipping tasks within a stage.

2. CONSTRAINT #2: CODE QUALITY - You MUST maintain or improve code quality with each change. Code that compiles but introduces technical debt is UNACCEPTABLE.

3. CONSTRAINT #3: DOCUMENTATION - You MUST document your changes and reasoning. Undocumented changes are PROHIBITED.
</hard-constraints>

<verification-request>
Confirm you have understood these instructions by responding with:
"I will follow the implementation protocol for Stage [X]. I will assess the current state, plan my implementation approach with a focus on preserving existing functionality, and verify my changes before marking the stage as complete."
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