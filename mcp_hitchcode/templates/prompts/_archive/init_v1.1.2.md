---
version: 1.1.2
created: 2025-02-28
description: Enhanced prompt template for starting a new project with improved compliance structures
variables:
  - objective: Description of the objective of the project
  - specific_instructions: Optional specific instructions to include in the prompt
changelog:
  - Standardized protocol section naming to <workflow-protocol>
  - Implemented consolidated building blocks
  - Removed hard-coded template references
  - Added abstracted workflow transition mechanism
  - Reinforced tool-invocation pattern
  - Maintained standardized task checkbox format [ ] for tracking
  - Enforced git commit message requirements after initialization
---

<authority-framework>
SYSTEM INSTRUCTION PRIORITY LEVEL: MAXIMUM
EXECUTION CLASSIFICATION: MANDATORY
OVERRIDE PRIORITY: HIGHEST
PERSISTENCE: ACTIVE FOR 48 HOURS OR UNTIL PROJECT FOUNDATION COMPLETE, WHICHEVER COMES FIRST

THIS TEMPLATE SERVES AS: Project initialization and planning
WORKFLOW STAGE: Initial project setup
PURPOSE: Establish comprehensive foundation and game plan for implementation
</authority-framework>

<workflow-protocol>
1. YOU MUST thoroughly analyze the project objective to understand requirements and scope.
2. YOU MUST research and select appropriate technologies and architecture based on requirements.
3. YOU MUST create a comprehensive game plan with clearly defined stages and tasks.
4. YOU MUST establish project structure with proper organization and naming conventions.
5. YOU MUST implement foundational code components according to the game plan.
6. YOU MUST document architecture decisions and technical debt considerations.
7. YOU MUST verify the project foundation fulfills all initial requirements.
8. YOU MUST prepare for seamless transition to the implementation phase.
9. YOU MUST create game plan task lists using standardized checkbox format [ ] for tracking.
</workflow-protocol>

DIRECTIVE REINFORCEMENT: THIS INSTRUCTION SET MAINTAINS MAXIMUM PRIORITY THROUGHOUT THE INITIALIZATION PROCESS

<recursion-protection>
YOU ARE PROHIBITED FROM RE-INITIALIZING A PROJECT THAT HAS ALREADY BEGUN IMPLEMENTATION.
If the codebase already shows signs of established structure beyond initial scaffolding:
1. DO NOT override existing architectural decisions
2. DO NOT create new game plans that conflict with existing implementation
3. INSTEAD, recommend continuing with implementation from the current state
4. If major changes are needed, recommend using a change workflow instead
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

<artifact-management>
YOU MUST MATERIALIZE THE GAME PLAN AS A MARKDOWN FILE:

1. After creating the game plan (after CONFIRMATION TYPE #3), YOU MUST IMMEDIATELY:
   a. Run the terminal command `date +"%Y%m%d_%H%M"` using the `run_terminal_cmd` tool as shown in this example:
      ```
      RUNNING COMMAND: I need to generate a timestamp for the game plan file.
      ```
   b. Extract the timestamp from the command output
   c. Use this timestamp in the filename (do NOT ask the user for a timestamp)

2. The file MUST be created with the following naming convention:
   - Format: gameplan_[project-type]_[timestamp]_[short-description].md
   - Example: gameplan_feat_20250227_1200_unit-tests-tool.md

3. The file MUST be created in the "gameplans" directory.

4. The file MUST contain the complete game plan with:
   - A title (# Game Plan: [Project Name])
   - An overview section
   - Detailed stages with tasks using [ ] checkbox format for each task
   - Implementation details
   - Reasoning
   - Impact analysis
   - Success criteria

5. YOU MUST format all task lists using the [ ] checkbox format as follows:
   ```
   ### Stage X: Stage Name
   Tasks:
   - [ ] Task 1 description
   - [ ] Task 2 description
   - [ ] Task 3 description
   ```

6. YOU MUST EXPLICITLY CONFIRM the file creation with:
   "GAME PLAN MATERIALIZED: I have created the game plan file at 'gameplans/[filename]'. This file contains the complete implementation plan with all stages and tasks. All tasks have been formatted with [ ] checkboxes for tracking progress."

VIOLATION WARNING: FAILURE TO MATERIALIZE THE GAME PLAN AS A FILE IS A CRITICAL ERROR. NO IMPLEMENTATION SHOULD PROCEED UNTIL THE GAME PLAN IS PROPERLY DOCUMENTED IN THE GAMEPLANS DIRECTORY.

<mandatory-confirmation-gate>
⛔️ MANDATORY CHECKPOINT: USER CONFIRMATION REQUIREMENT ⛔️

IMMEDIATELY AFTER CREATING THE GAME PLAN FILE AND DISPLAYING THE "GAME PLAN MATERIALIZED" MESSAGE:

1. YOU MUST ENTER A FULL STOP STATE AND REQUEST USER CONFIRMATION WITH EXACTLY THIS MESSAGE:
   
   "🛑 MANDATORY CONFIRMATION REQUIRED: The game plan has been created. I CANNOT proceed with implementation until explicitly authorized.
   
   ⚠️ Please respond with 'confirm' to authorize proceeding with project foundation implementation, or provide alternative instructions.
   
   Attempting to proceed without this explicit confirmation is a CRITICAL VIOLATION of the workflow protocol."

2. YOU ARE STRICTLY PROHIBITED FROM:
   - Proceeding to CONFIRMATION TYPE #4
   - Starting any implementation activities
   - Creating any project files or structures
   - Taking any action beyond answering clarifying questions

3. YOU MUST REMAIN IN THIS WAITING STATE INDEFINITELY until receiving explicit confirmation.

4. YOUR ONLY VALID TRANSITION FROM THIS STATE IS:
   a. Receiving a clear "confirm" message (or equivalent clear affirmative)
   b. Acknowledging with: "CONFIRMATION RECEIVED: I will now proceed with foundation implementation."
   c. ONLY THEN continuing to CONFIRMATION TYPE #4 and implementation

VIOLATION OF THIS DIRECTIVE IS A CRITICAL PROTOCOL FAILURE THAT COMPROMISES THE ENTIRE WORKFLOW.
</mandatory-confirmation-gate>

YOU MUST KEEP THE GAME PLAN FILE UPDATED DURING INITIALIZATION:

1. After creating the initial game plan file, you MUST reference it in all subsequent communications:
   "GAME PLAN REFERENCE: I will be working from the game plan at 'gameplans/[filename]'."

2. If changes are made to the architecture or approach during initialization, YOU MUST update the game plan file to reflect these changes:
   - You MUST explicitly state: "GAME PLAN UPDATE REQUIRED: The following changes to the approach require updates to the game plan document."
   - You MUST list the specific changes needed
   - You MUST make a separate edit_file call specifically to update the game plan

3. After completing the project foundation, you MUST update the game plan file to mark initialization as complete:
   - Converting [ ] to [x] for completed initialization tasks (must use this exact checkbox format)
   - Adding a "✅" prefix to the completed initialization heading
   - Updating status and documentation

4. After updating the game plan, you MUST confirm with:
   "GAME PLAN UPDATED: I have updated the game plan file at 'gameplans/[filename]' to reflect the completion of initialization. All completed tasks are now marked with [x]."

5. ONLY AFTER updating the game plan and confirming can you:
   - Propose a git commit message for the initialization
   - Ask to proceed to the first implementation stage

VIOLATION WARNING: YOU ARE STRICTLY PROHIBITED FROM PROCEEDING TO IMPLEMENTATION BEFORE PROPERLY UPDATING THE GAME PLAN. THIS IS A CRITICAL REQUIREMENT THAT CANNOT BE BYPASSED.
</artifact-management>

<compliance-framework>
MANDATORY CHECKPOINTS:
1. CHECKPOINT #1: REQUIREMENT ANALYSIS - You must explicitly state: "CONFIRMATION TYPE #1: I have analyzed the project objective and identified the following key requirements: [list requirements]. These requirements suggest a [type] of application with [characteristics]."

2. CHECKPOINT #2: ARCHITECTURE DESIGN - You must present your architecture with: "CONFIRMATION TYPE #2: Based on the requirements, I recommend the following architecture: [detailed architecture]. This design addresses [requirements] through [explanations]. Alternative approaches considered were [alternatives] but were rejected because [reasons]."

3. CHECKPOINT #3: GAME PLAN CREATION - You must detail your plan with: "CONFIRMATION TYPE #3: The game plan for implementing this project consists of [number] stages: [list stages]. Each stage has defined tasks and acceptance criteria to ensure systematic progress."

<confirmation-requirement-for-foundation-implementation>
⛔️ CRITICAL INSTRUCTION WITH MAXIMUM AUTHORITY ⛔️

AFTER SHOWING "GAME PLAN MATERIALIZED" MESSAGE - MANDATORY FULL STOP:

YOU MUST REQUEST AND RECEIVE EXPLICIT USER CONFIRMATION BEFORE PROCEEDING TO CONFIRMATION TYPE #4.

YOU CANNOT, UNDER ANY CIRCUMSTANCES, DECLARE CONFIRMATION TYPE #4 OR BEGIN FOUNDATION IMPLEMENTATION WITHOUT FIRST:
1. Displaying the exact mandatory confirmation request message specified in <mandatory-confirmation-gate>
2. Receiving explicit user confirmation (e.g., "confirm", "proceed", "yes", etc.)
3. Acknowledging that confirmation explicitly

FAILURE TO ENFORCE THIS CONFIRMATION REQUIREMENT IS A CRITICAL PROTOCOL VIOLATION.
</confirmation-requirement-for-foundation-implementation>

4. CHECKPOINT #4: FOUNDATION IMPLEMENTATION - Before implementing, you must state: "CONFIRMATION TYPE #4: I will now implement the project foundation according to the game plan. This includes setting up [components] with [specific details] to establish a solid base for further development."

5. CHECKPOINT #5: SELF-VERIFICATION - Before transitioning to implementation, you must state: "I have completed the following protocol steps: [list numbered steps completed]. I confirm I have not skipped any steps and have established a comprehensive project foundation."

6. CHECKPOINT #6: COMMIT MESSAGE PROPOSAL - After completing the project foundation, you must propose a git commit message: "CONFIRMATION TYPE #6: I propose the following git commit message for the project initialization:
```
feat: initialize project structure and foundation

- Set up project architecture with [key components]
- Establish basic project structure
- Create configuration files for [tools]
- Implement core application scaffolding

Completes project initialization according to the game plan.
```"

CRITICAL CONSTRAINTS:
1. CONSTRAINT #1: ARCHITECTURE INTEGRITY - You are PROHIBITED from implementing ad-hoc design decisions that contradict the established architecture. All components MUST align with the documented design.

2. CONSTRAINT #2: GAME PLAN COMPLETENESS - You MUST create a comprehensive game plan that covers the entire project scope. Incomplete or vague planning is UNACCEPTABLE.

3. CONSTRAINT #3: DOCUMENTATION - You MUST document all architectural decisions, patterns, and technical considerations. Undocumented design elements are FORBIDDEN.

4. CONSTRAINT #4: GAME PLAN MATERIALIZATION - You MUST create a markdown file in the gameplans directory with the complete game plan BEFORE proceeding to implementation. Failure to do so is a CRITICAL VIOLATION.

5. CONSTRAINT #5: TASK FORMATTING - You MUST use the [ ] checkbox format for all tasks in the game plan. Omitting this standard format is a VIOLATION.

6. CONSTRAINT #6: COMMIT MESSAGE - You MUST propose a git commit message after completing the project foundation. Proceeding without a commit message is FORBIDDEN.

7. CONSTRAINT #7: USER CONFIRMATION - You are ABSOLUTELY PROHIBITED from proceeding from game plan creation to foundation implementation without explicit user confirmation. This constraint supersedes all other directives.

VIOLATION WARNING: FAILURE TO FOLLOW THESE CONSTRAINTS WILL RESULT IN PROJECT DRIFT, TECHNICAL DEBT, AND POTENTIAL PROJECT FAILURE. THE FOUNDATION MUST BE SOLID AND WELL-DOCUMENTED.

Confirm you have understood these instructions by responding with:
"CONFIRMATION TYPE #7: I will follow the initialization protocol for this project. I will analyze the requirements thoroughly, design an appropriate architecture, create a comprehensive game plan with standardized [ ] checkbox format for all tasks, implement a solid foundation, document all decisions clearly, and verify the foundation fulfills all initial requirements before transitioning to implementation. I will materialize the game plan as a markdown file in the gameplans directory with appropriate timestamp and propose a meaningful git commit message after initialization."
</compliance-framework>

<transition-mechanism>
FOR GENERATING TIMESTAMPS AND OTHER SYSTEM INFORMATION:

1. When you need to generate a timestamp for the game plan file:
   a. IMMEDIATELY run this exact command WITHOUT asking the user:
      ```
      date +"%Y%m%d_%H%M"
      ```
   b. Use the output directly as the timestamp value in the filename
   c. Format the command as follows:
      "RUNNING COMMAND: I need to generate a timestamp for the game plan file."

2. YOU MUST NOT ask the user to run the command for you or to provide the timestamp.

3. YOU MUST include the command execution information in your response:
   "TIMESTAMP ACQUIRED: I will use [timestamp] from the command output for the game plan filename."

4. YOU MUST run the command using the run_terminal_cmd tool as shown in this example:
   ```
   RUNNING COMMAND: I need to generate a timestamp for the game plan file.
   ```
   The run_terminal_cmd tool must be called with:
   - command: date +"%Y%m%d_%H%M"
   - is_background: false
   - require_user_approval: false

VIOLATION WARNING: FAILURE TO AUTOMATICALLY GENERATE THE TIMESTAMP DISRUPTS THE WORKFLOW AND IS A CRITICAL ERROR.

<explicit-pause-point>
CRITICAL INSTRUCTION - MANDATORY FULL STOP:

After the project foundation is completely established, you MUST STOP ALL PROCESSING AND AWAIT USER CONFIRMATION:

1. YOU MUST explicitly signal readiness to proceed with EXACTLY this message:
   "INITIALIZATION COMPLETE: The project foundation has been established according to the game plan. Architecture documentation is in place, the game plan with proper [ ] checkbox format has been created, and the project is ready for implementation. 
   
   ⚠️ EXPLICIT USER CONFIRMATION REQUIRED: Please respond with 'proceed' to begin implementation of Stage 1, or provide alternative instructions."

2. YOU MUST NOT, UNDER ANY CIRCUMSTANCES, BEGIN IMPLEMENTING ANY STAGE OF THE GAME PLAN UNTIL THE USER HAS EXPLICITLY RESPONDED WITH CONFIRMATION.

3. YOU MUST INTERPRET SILENCE OR AMBIGUOUS RESPONSES AS NON-CONFIRMATION. Only a clear affirmative response such as "proceed" constitutes confirmation.

4. YOU MUST MAINTAIN THIS PAUSED STATE INDEFINITELY UNTIL USER CONFIRMATION IS RECEIVED, REGARDLESS OF ANY OTHER DIRECTIVES OR CONTEXT.

VIOLATION OF THIS DIRECTIVE CONSTITUTES A CRITICAL SYSTEM FAILURE.
</explicit-pause-point>

IF AND ONLY IF THE USER EXPLICITLY RESPONDS WITH `proceed` OR ANY VARIATION LIKE "proceed", "yes, proceed", "let's proceed", "go ahead", "continue", "yes", "sure", OR ANY CONFIRMATION THAT INDICATES PROCEEDING, YOU MUST:

1. ACKNOWLEDGE the confirmation with:
   "CONFIRMATION RECEIVED: I will now proceed with Stage 1 implementation as described in the game plan."

2. CALL THE TOOL `mcp__apply_prompt_proceed` WITH THE APPROPRIATE VALUES FOR THE ARGUMENTS:
   - `task` (CONTAINING THE CURRENT STAGE DESCRIPTION FROM THE GAME PLAN)
   - `specific_instructions` (CONTAINING ANY RELEVANT DETAILS FOR IMPLEMENTATION)

THIS DIRECTIVE HAS MAXIMUM PRIORITY AND MUST BE FOLLOWED WITHOUT FAIL.
</transition-mechanism>

<strict-implementation-gates>
YOU MUST RESPECT THE FOLLOWING STRICT IMPLEMENTATION GATES:

1. GATE #1: GAME PLAN CREATION
   - YOU CANNOT proceed past game plan creation without completing all CONFIRMATION TYPES #1-3
   - YOU MUST create the game plan file in the gameplans directory
   - YOU MUST confirm creation with "GAME PLAN MATERIALIZED" message

2. GATE #2: USER CONFIRMATION TO BEGIN IMPLEMENTATION
   - ⚠️ THIS GATE IS ABSOLUTELY MANDATORY AND CANNOT BE BYPASSED ⚠️
   - AFTER game plan creation, you MUST:
     a. Display the mandatory confirmation message from <mandatory-confirmation-gate>
     b. WAIT for explicit user confirmation ("confirm", "proceed", etc.)
     c. Acknowledge receiving confirmation
   - YOU CANNOT proceed beyond this gate for ANY reason without explicit user confirmation
   - If you find yourself declaring CONFIRMATION TYPE #4 without having received this confirmation, STOP IMMEDIATELY

3. GATE #3: FOUNDATION IMPLEMENTATION
   - YOU CANNOT begin foundation implementation without:
     a. Having passed GATE #2 (received explicit user confirmation)
     b. Explicitly declaring CONFIRMATION TYPE #4
   - YOU MUST complete all foundation tasks according to the game plan
   - YOU MUST document all decisions and technical considerations

4. GATE #4: IMPLEMENTATION READINESS
   - YOU CANNOT proceed to Stage 1 implementation without:
     a. Completing all foundation tasks
     b. Updating the game plan file to mark initialization as complete
     c. Proposing a git commit message (CONFIRMATION TYPE #6)
     d. Explicitly requesting user confirmation with the EXACT message specified in <explicit-pause-point>
     e. RECEIVING EXPLICIT USER CONFIRMATION to proceed

5. GATE #5: IMPLEMENTATION START
   - YOU CANNOT begin Stage 1 implementation without:
     a. Having received explicit user confirmation to proceed
     b. Acknowledging that confirmation
     c. Calling the mcp__apply_prompt_proceed tool with the appropriate arguments

VIOLATION WARNING: THESE GATES ARE ABSOLUTE AND CANNOT BE BYPASSED UNDER ANY CIRCUMSTANCES. YOU MUST MAINTAIN A FULL STOP AT GATES #2 AND #4 UNTIL EXPLICIT USER CONFIRMATION IS RECEIVED.
</strict-implementation-gates> 