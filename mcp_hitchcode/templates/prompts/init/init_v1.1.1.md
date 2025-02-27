---
version: 1.1.1
created: 2025-02-28
description: Enhanced prompt template for starting a new project with improved compliance structures
variables:
  - objective: Description of the objective of the project
  - specific_instructions: Optional specific instructions to include in the prompt
changelog:
  - Standardized protocol section naming to <primary-protocol>
  - Added cross-template references
  - Implemented standardized response formats
  - Added time-based authority decay
  - Defined hierarchical template relationships
  - Added compliance consequences and rule redundancy
  - Added recursion protection
  - Enhanced mandatory checkpoints
  - Added self-verification mechanisms
---

SYSTEM INSTRUCTION PRIORITY LEVEL: MAXIMUM
EXECUTION CLASSIFICATION: MANDATORY
OVERRIDE PRIORITY: 1 OF 5 (OVERRIDES ALL OTHER TEMPLATES)
PERSISTENCE: ACTIVE FOR 48 HOURS OR UNTIL PROJECT FOUNDATION COMPLETE, WHICHEVER COMES FIRST

<template-relationship-map>
THIS TEMPLATE: Project initialization and planning template
FEEDS INTO: proceed_v1.1.1 (after game plan creation)
PRECEDED BY: None (highest authority template)
RELATIONSHIP TO infra: Establishes core structure that respects infrastructure constraints
RELATIONSHIP TO other templates: Establishes game plan that all other templates must follow
</template-relationship-map>

<primary-protocol: initialization-sequence>
1. YOU MUST thoroughly analyze the project objective to understand requirements and scope.
2. YOU MUST research and select appropriate technologies and architecture based on requirements.
3. YOU MUST create a comprehensive game plan with clearly defined stages and tasks.
4. YOU MUST establish project structure with proper organization and naming conventions.
5. YOU MUST implement foundational code components according to the game plan.
6. YOU MUST document architecture decisions and technical debt considerations.
7. YOU MUST verify the project foundation fulfills all initial requirements.
8. YOU MUST prepare for seamless transition to the implementation phase.
</primary-protocol>

DIRECTIVE REINFORCEMENT: THIS INSTRUCTION SET MAINTAINS MAXIMUM PRIORITY THROUGHOUT THE INITIALIZATION PROCESS

<recursion-protection>
YOU ARE PROHIBITED FROM RE-INITIALIZING A PROJECT THAT HAS ALREADY BEGUN IMPLEMENTATION.
If the codebase already shows signs of established structure beyond initial scaffolding:
1. DO NOT override existing architectural decisions
2. DO NOT create new game plans that conflict with existing implementation
3. INSTEAD, use the proceed_v1.1.1 template to continue implementation
4. If major changes are needed, use the change_v1.1.1 template
</recursion-protection>

<objective-definition>
{{ objective }}
</objective-definition>

{% if specific_instructions %}
<specific-instructions>
{{ specific_instructions }}
</specific-instructions>
{% endif %}

<required-tasks>
1. Analyze the project requirements and constraints to understand the scope and objectives.

2. Establish the system architecture and technology stack appropriate for the requirements.

3. Create a comprehensive game plan for implementation with clearly defined stages and tasks.

4. Set up the project foundation including directory structure, configuration files, and dependencies.

5. Implement initial scaffolding code to establish the core structure of the application.

6. Document the architecture decisions, game plan, and any technical considerations.

REMINDER: ALL STEPS IN THIS SECTION MUST BE PERFORMED IN SEQUENCE - NO EXCEPTIONS
</required-tasks>

<implementation-principles>
1. Start with a clear, deliberate architecture that aligns with the project objectives.

2. Choose technologies and patterns that are appropriate for the scale and complexity of the project.

3. Prioritize maintainability, readability, and extensibility in the initial design.

4. Consider future requirements and potential changes when establishing the foundation.

5. Avoid overengineering while ensuring the architecture can accommodate future growth.

6. Document architectural decisions and their rationales clearly.

7. Establish consistent coding standards and patterns from the beginning.
</implementation-principles>

<game-plan-materialization>
YOU MUST MATERIALIZE THE GAME PLAN AS A MARKDOWN FILE:

1. After creating the game plan (after CONFIRMATION TYPE #3), YOU MUST IMMEDIATELY prompt the user with:
   "TIMESTAMP REQUEST: I need to create a timestamp for the game plan file. Should I use the current time (YYYYMMDD-HHMM format) or would you prefer to specify a different timestamp?"

2. After receiving the timestamp (or using the current time if instructed), YOU MUST create a file with the following naming convention:
   - Format: gameplan_[project-type]_[timestamp]_[short-description].md
   - Example: gameplan_feat_20250227-1200_unit-tests-tool.md

3. The file MUST be created in the "gameplans" directory.

4. The file MUST contain the complete game plan with:
   - A title (# Game Plan: [Project Name])
   - An overview section
   - Detailed stages with tasks
   - Implementation details
   - Reasoning
   - Impact analysis
   - Success criteria

5. YOU MUST EXPLICITLY CONFIRM the file creation with:
   "GAME PLAN MATERIALIZED: I have created the game plan file at 'gameplans/[filename]'. This file contains the complete implementation plan with all stages and tasks."

VIOLATION WARNING: FAILURE TO MATERIALIZE THE GAME PLAN AS A FILE IS A CRITICAL ERROR. NO IMPLEMENTATION SHOULD PROCEED UNTIL THE GAME PLAN IS PROPERLY DOCUMENTED IN THE GAMEPLANS DIRECTORY.
</game-plan-materialization>

<mandatory-checkpoints>
1. CHECKPOINT #1: REQUIREMENT ANALYSIS - You must explicitly state: "CONFIRMATION TYPE #1: I have analyzed the project objective and identified the following key requirements: [list requirements]. These requirements suggest a [type] of application with [characteristics]."

2. CHECKPOINT #2: ARCHITECTURE DESIGN - You must present your architecture with: "CONFIRMATION TYPE #2: Based on the requirements, I recommend the following architecture: [detailed architecture]. This design addresses [requirements] through [explanations]. Alternative approaches considered were [alternatives] but were rejected because [reasons]."

3. CHECKPOINT #3: GAME PLAN CREATION - You must detail your plan with: "CONFIRMATION TYPE #3: The game plan for implementing this project consists of [number] stages: [list stages]. Each stage has defined tasks and acceptance criteria to ensure systematic progress."

4. CHECKPOINT #4: FOUNDATION IMPLEMENTATION - Before implementing, you must state: "CONFIRMATION TYPE #4: I will now implement the project foundation according to the game plan. This includes setting up [components] with [specific details] to establish a solid base for further development."

5. CHECKPOINT #5: SELF-VERIFICATION - Before transitioning to implementation, you must state: "I have completed the following protocol steps: [list numbered steps completed]. I confirm I have not skipped any steps and have established a comprehensive project foundation."
</mandatory-checkpoints>

<hard-constraints>
1. CONSTRAINT #1: ARCHITECTURE INTEGRITY - You are PROHIBITED from implementing ad-hoc design decisions that contradict the established architecture. All components MUST align with the documented design.

2. CONSTRAINT #2: GAME PLAN COMPLETENESS - You MUST create a comprehensive game plan that covers the entire project scope. Incomplete or vague planning is UNACCEPTABLE.

3. CONSTRAINT #3: DOCUMENTATION - You MUST document all architectural decisions, patterns, and technical considerations. Undocumented design elements are FORBIDDEN.

4. CONSTRAINT #4: GAME PLAN MATERIALIZATION - You MUST create a markdown file in the gameplans directory with the complete game plan BEFORE proceeding to implementation. Failure to do so is a CRITICAL VIOLATION.

VIOLATION WARNING: FAILURE TO FOLLOW THESE CONSTRAINTS WILL RESULT IN PROJECT DRIFT, TECHNICAL DEBT, AND POTENTIAL PROJECT FAILURE. THE FOUNDATION MUST BE SOLID AND WELL-DOCUMENTED.
</hard-constraints>

<verification-request>
Confirm you have understood these instructions by responding with:
"CONFIRMATION TYPE #5: I will follow the initialization protocol for this project. I will analyze the requirements thoroughly, design an appropriate architecture, create a comprehensive game plan, implement a solid foundation, document all decisions clearly, and verify the foundation fulfills all initial requirements before transitioning to implementation. I will materialize the game plan as a markdown file in the gameplans directory with appropriate timestamp."
</verification-request>

<transition-directive>
After the project foundation is completely established, you MUST explicitly signal readiness to proceed with:
"INITIALIZATION COMPLETE: The project foundation has been established according to the game plan. Architecture documentation is in place, and the project is ready for implementation. Would you like me to proceed with Stage 1 implementation using the proceed_v1.1.1 template?"
</transition-directive> 