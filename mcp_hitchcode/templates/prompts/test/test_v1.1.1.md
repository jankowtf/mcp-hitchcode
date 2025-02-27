---
version: 1.1.1
created: 2025-02-29
description: Enhanced prompt for generating unit tests for code with improved compliance structures
variables:
  - code_to_test: The code that needs unit tests
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
OVERRIDE PRIORITY: 5 OF 5 (YIELDS TO ALL OTHER TEMPLATES)
PERSISTENCE: ACTIVE FOR 2 HOURS OR UNTIL TEST SUITE COMPLETION, WHICHEVER COMES FIRST

<template-relationship-map>
THIS TEMPLATE: Test generation template
FEEDS INTO: proceed_v1.1.1 (after tests are completed)
PRECEDED BY: Any template when test coverage is needed
RELATIONSHIP TO infra: Respects infrastructure constraints defined in infra template
RELATIONSHIP TO fix templates: Can be interrupted by fix workflows but maintains test strategy
</template-relationship-map>

<primary-protocol: testing-sequence>
1. YOU MUST thoroughly analyze the code to understand its purpose and functionality.
2. YOU MUST identify all testable functions, methods, and components.
3. YOU MUST develop a comprehensive testing strategy that covers all code paths.
4. YOU MUST implement tests for normal operation, edge cases, and error conditions.
5. YOU MUST ensure tests are isolated and do not depend on the state of other tests.
6. YOU MUST verify that tests actually validate the intended functionality.
7. YOU MUST use appropriate mocking and fixtures for external dependencies.
8. YOU MUST document your testing approach and any assumptions made.
</primary-protocol>

DIRECTIVE REINFORCEMENT: THIS INSTRUCTION SET MAINTAINS MAXIMUM PRIORITY THROUGHOUT THE TEST DEVELOPMENT PROCESS

<code-definition>
{{ code_to_test }}
</code-definition>

{% if specific_instructions %}
<specific-instructions>
{{ specific_instructions }}
</specific-instructions>
{% endif %}

<test-strategy-protocol>
1. Analyze the code and identify its key components, functions, and methods.

2. Determine which testing frameworks and tools are appropriate based on project configuration.

3. Develop a testing strategy that includes:
   a) Unit tests for individual functions and methods
   b) Integration tests for component interactions
   c) Edge case tests for boundary conditions
   d) Error handling tests for expected exceptions

4. Implement the tests according to the strategy, ensuring thorough coverage.

5. Verify that the tests accurately validate the code's intended behavior.

REMINDER: COMPREHENSIVE TEST STRATEGY DEVELOPMENT IS MANDATORY BEFORE WRITING TESTS
</test-strategy-protocol>

<testing-principles>
1. Tests should be isolated and independent of each other.

2. Each test should have a clear purpose and verify a specific aspect of functionality.

3. Use appropriate mocking and fixtures to isolate the code being tested from its dependencies.

4. Aim for high test coverage, but prioritize testing critical paths and complex logic.

5. Include edge cases and error conditions in your testing strategy.

6. Follow the project's existing testing patterns and conventions.

7. Write clear, descriptive test names that indicate what is being tested.
</testing-principles>

<test-coverage-protocol>
For each function/method being tested, YOU MUST include tests for:
1. Normal operation with valid inputs
2. Edge cases (empty collections, minimum/maximum values, etc.)
3. Error conditions and exception handling
4. Any special cases mentioned in the code or requirements

YOUR TEST SUITE MUST PROVIDE COMPREHENSIVE VALIDATION OF THE CODE
</test-coverage-protocol>

<mandatory-checkpoints>
1. CHECKPOINT #1: CODE ANALYSIS - You must explicitly state: "CONFIRMATION TYPE #1: I have analyzed the code and identified the following components to test: [list components]. The key functionality includes [functionality] and the expected behavior is [behavior]."

2. CHECKPOINT #2: TEST STRATEGY - You must present your strategy with: "CONFIRMATION TYPE #2: My testing strategy is: [detailed strategy]. I will use [framework/approach] and focus on [focus areas]. I will create [number] test categories covering [coverage areas]."

3. CHECKPOINT #3: TEST IMPLEMENTATION - Before writing tests, you must state: "CONFIRMATION TYPE #3: I will now implement tests for [component] using the following approach: [approach]. These tests will verify [what is being verified] under [conditions]."

4. CHECKPOINT #4: TEST VERIFICATION - After implementing tests, you must verify and state: "CONFIRMATION TYPE #4: I have created [number] tests that verify: (1) normal operation, (2) edge cases, (3) error conditions, and (4) integration points. The estimated coverage is [coverage]."

5. CHECKPOINT #5: SELF-VERIFICATION - Before marking the tests as complete, you must state: "I have completed the following protocol steps: [list numbered steps completed]. I confirm I have not skipped any steps and have maintained testing rigor throughout the process."
</mandatory-checkpoints>

<hard-constraints>
1. CONSTRAINT #1: TEST ISOLATION - You are PROHIBITED from creating tests that depend on the state or outcome of other tests. Each test MUST be fully isolated.

2. CONSTRAINT #2: COVERAGE COMPLETENESS - You MUST test all logical branches and edge cases. Incomplete test coverage is UNACCEPTABLE.

3. CONSTRAINT #3: FRAMEWORK CONSISTENCY - You MUST use the testing frameworks and patterns consistent with the existing project structure. Non-conforming test patterns are FORBIDDEN.

VIOLATION WARNING: FAILURE TO FOLLOW THESE CONSTRAINTS WILL RESULT IN FRAGILE TESTS, MISSING COVERAGE, AND UNRELIABLE TEST RESULTS. EACH TEST MUST BE ROBUST AND COMPREHENSIVE.
</hard-constraints>

<verification-request>
Confirm you have understood these instructions by responding with:
"CONFIRMATION TYPE #5: I will follow the testing protocol for the provided code. I will analyze the code thoroughly, develop a comprehensive testing strategy, implement tests that cover normal operation, edge cases, and error conditions, ensure test isolation, and verify the accuracy and coverage of my tests."
</verification-request>

<completion-directive>
After the test suite is completely implemented, you MUST explicitly signal completion with:
"TEST SUITE COMPLETE: I have created a comprehensive test suite with [number] tests covering [coverage details]. Would you like me to continue with any other testing tasks or return to the previous workflow?"
</completion-directive> 