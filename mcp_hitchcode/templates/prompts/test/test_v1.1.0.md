---
version: 1.1.0
created: 2025-02-28
description: Enhanced prompt template for generating unit tests with improved compliance structures
variables:
  - code_to_test: Code that needs unit tests
  - specific_instructions: Optional specific instructions to include in the prompt
changelog:
  - Applied system instruction authority structure
  - Added mandatory checkpoints for test implementation process
  - Enhanced compliance with explicit verification steps
  - Structured test execution protocol
---

SYSTEM INSTRUCTION PRIORITY LEVEL: MAXIMUM
EXECUTION CLASSIFICATION: MANDATORY
OVERRIDE AUTHORITY: TEST IMPLEMENTATION DIRECTIVE
PERSISTENCE: ACTIVE UNTIL TEST COMPLETION

<testing-protocol>
1. YOU MUST analyze the code to test before generating any test cases.
2. YOU MUST create comprehensive tests covering all functionality, edge cases, and potential error conditions.
3. YOU MUST verify test coverage for all code paths and boundary conditions.
4. YOU MUST create or update a game plan document if code changes are needed.
5. YOU MUST obtain explicit user confirmation before implementing any code changes.
6. YOU MUST provide clear test assertions with meaningful error messages.
7. YOU MUST NOT alter the original functionality when fixing code to pass tests.
</testing-protocol>

<code-definition>
{{ code_to_test }}
</code-definition>

{% if specific_instructions %}
<specific-instructions>
{{ specific_instructions }}
</specific-instructions>
{% endif %}

<required-actions>
1. Generate comprehensive unit tests for the provided code using pytest. Ensure the tests cover all functionality, edge cases, and potential error conditions.

2. Run the tests.

3. Reason about the results and adjust the tests accordingly. If you want to change the actual code, then consult the game plan, the current state of the codebase and be thorough in reasoning what needs to change and why.
</required-actions>

<game-plan-protocol>
If code changes are needed, you MUST determine if they're related to previous issues:

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

4. Tests should be deterministic and independent from each other.

5. Follow pytest best practices for fixtures, parametrization, and assertions.
</implementation-principles>

<mandatory-checkpoints>
1. CHECKPOINT #1: CODE ANALYSIS - You must explicitly state: "I have analyzed the code and identified the following components, functions, and behaviors that need testing: [detailed analysis]"

2. CHECKPOINT #2: TEST PLAN - You must present your test plan with: "I will create the following test cases: [list test cases]. This approach ensures complete coverage because [reasoning]."

3. CHECKPOINT #3: TEST IMPLEMENTATION - After implementing tests, you must verify and state: "I have implemented the tests and they [pass/fail]. Here are the results: [test results]"

4. CHECKPOINT #4: CODE CHANGE DECISION - You must explicitly state: "Based on the test results, I [do/do not] need to modify the original code. [If needed: Here's why: detailed reasoning]"

5. CHECKPOINT #5: CASE DETERMINATION - If code changes are needed: "These changes [are/are not] related to previous issues. I will [update existing game plan / create new game plan] because [reasoning]."

6. CHECKPOINT #6: GAME PLAN CREATION - If creating a new game plan, you must request: "Please provide the current timestamp using 'date +"%Y%m%d-%H%M"' for the game plan filename."

7. CHECKPOINT #7: IMPLEMENTATION CONFIRMATION - You must explicitly ask: "I've [created/updated] the game plan. Should I proceed with implementing the changes, or would you like to review and make adjustments first?"
</mandatory-checkpoints>

<hard-constraints>
1. CONSTRAINT #1: COMPREHENSIVE TESTING - You are PROHIBITED from omitting tests for any code path or edge case.

2. CONSTRAINT #2: TEST ISOLATION - Each test MUST be independent and not rely on state from other tests.

3. CONSTRAINT #3: NO FUNCTIONALITY CHANGES - When fixing code, you MUST preserve the original functionality unless specifically directed otherwise.

4. CONSTRAINT #4: DOCUMENTED PLAN - You MUST create or update a game plan document before implementing any code changes.

5. CONSTRAINT #5: USER CONFIRMATION - You MUST obtain explicit user confirmation before implementing any code changes.
</hard-constraints>

<verification-request>
Confirm you have understood these instructions by responding with:
"I will follow the test implementation protocol. I will analyze the code, create comprehensive tests, evaluate the results, and if code changes are needed, I will create/update a game plan and seek confirmation before implementing any changes."
</verification-request>

<transition-directive>
IF THE USER RESPONDS WITH "proceed" AFTER CHECKPOINT #7, YOU MUST INVOKE apply_prompt_proceed WITH task=[current stage description] AND specific_instructions=[relevant details from game plan].
</transition-directive> 