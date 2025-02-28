---
version: 1.1.2
created: 2025-02-28
description: Enhanced prompt for analyzing and fixing linter errors with improved compliance structures
variables:
  - issue: Description of the linter errors to be analyzed and fixed
  - specific_instructions: Optional specific instructions to include in the prompt
changelog:
  - Standardized protocol section naming to <workflow-protocol>
  - Implemented consolidated building blocks
  - Removed hard-coded template references
  - Added abstracted workflow transition mechanism
  - Enhanced systematic error resolution approach
  - Reinforced pattern-based fix methodology
---

<authority-framework>
SYSTEM INSTRUCTION PRIORITY LEVEL: MAXIMUM
EXECUTION CLASSIFICATION: MANDATORY
OVERRIDE PRIORITY: HIGH
PERSISTENCE: ACTIVE FOR 2 HOURS OR UNTIL ALL LINTER ERRORS RESOLVED, WHICHEVER COMES FIRST

THIS TEMPLATE SERVES AS: Linter error resolution workflow
WORKFLOW STAGE: Code quality correction
PURPOSE: Efficiently identify and resolve linter errors using systematic patterns
</authority-framework>

<workflow-protocol>
1. YOU MUST fully understand the linter errors before attempting any fixes.
2. YOU MUST group related linter errors by type and location.
3. YOU MUST prioritize errors that block compilation or testing.
4. YOU MUST apply systematic fixes that address patterns, not just individual instances.
5. YOU MUST verify each fix resolves the targeted linter error without introducing new ones.
6. YOU MUST document patterns of errors for future prevention.
7. YOU MUST ensure all linter errors are resolved before completion.
8. YOU MUST restore process state after fixes are complete.
</workflow-protocol>

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
1. Parse the linter output to identify specific error messages, codes, and locations.

2. Group related errors by type to identify patterns and common causes.

3. Determine the severity of each error type (blocking vs. non-blocking).

4. Research the meaning and proper resolution for each error type if not immediately clear.

5. Create a prioritized list of errors to address based on severity and interdependence.

REMINDER: THOROUGH CATEGORIZATION IS ESSENTIAL BEFORE SYSTEMATIC RESOLUTION
</required-analysis>

<fix-methodology>
1. Start with errors that block compilation or testing, then proceed to style and best practice issues.

2. Address errors methodically by type, applying consistent patterns for similar issues.

3. Prefer fixes that address multiple instances of the same error pattern.

4. Make minimal changes required to resolve each linter error.

5. Ensure each fix maintains or improves code readability and maintainability.

6. Document any fixes that represent recurring patterns for future reference.

CRITICAL REMINDER: SYSTEMATIC PATTERN-BASED FIXES ARE PREFERRED OVER INDIVIDUAL EXCEPTION HANDLING
</fix-methodology>

<artifact-management>
STATE PRESERVATION:
1. Before implementing linter fixes, YOU MUST capture the original state:
   "LINTER ERROR STATE: I've identified [number] linter errors of [types] types."

2. Track progress by maintaining a categorized error list:
   - Number of errors by type
   - Files affected
   - Fix patterns being applied
   - Current progress status

3. If the linter fix interrupts another workflow, you MUST preserve:
   - Current task or stage that was interrupted
   - Any partial implementation progress
   - Game plan stage and task context

4. After completing all fixes, YOU MUST confirm state restoration:
   "STATE RESTORATION: All linter errors have been fixed. Returning to previous workflow state: [details]."

ERROR PATTERN DOCUMENTATION:
1. YOU MUST document common error patterns and their fixes:
   "ERROR PATTERN IDENTIFIED: [pattern description] occurring in [number] instances. This pattern requires [fix approach]."

2. If the same error occurs in multiple locations, YOU MUST ensure consistent fixes with:
   "CONSISTENT FIX PATTERN: Applying the same fix pattern to all [number] instances of [error type]."

3. If a fix requires a specific approach due to code context, YOU MUST explain:
   "CONTEXT-SPECIFIC FIX: While the error is similar to others, this instance requires a different approach because [reasoning]."

VIOLATION WARNING: FAILURE TO PROPERLY DOCUMENT ERROR PATTERNS AND RESTORE STATE CAN LEAD TO INCONSISTENT CODE STYLE AND DISRUPTED WORKFLOWS.
</artifact-management>

<compliance-framework>
MANDATORY CHECKPOINTS:
1. CHECKPOINT #1: ERROR ANALYSIS - You must explicitly state: "CONFIRMATION TYPE #1: I have analyzed the linter output and identified [number] errors across [number] files. The error types include [list of error types] with distribution [distribution details]."

2. CHECKPOINT #2: PRIORITIZATION - You must present your plan with: "CONFIRMATION TYPE #2: I will address these errors in the following priority order: [prioritized list]. This prioritization is based on [reasoning]."

3. CHECKPOINT #3: PATTERN IDENTIFICATION - You must explicitly state: "CONFIRMATION TYPE #3: I have identified the following error patterns: [patterns with examples]. Each pattern will be addressed with a consistent approach."

4. CHECKPOINT #4: FIX IMPLEMENTATION - Before implementing fixes for each pattern, you must state: "CONFIRMATION TYPE #4: I will now implement fixes for [error pattern]. This pattern affects [number] locations. The fix approach will be [detailed approach]."

5. CHECKPOINT #5: VERIFICATION - After implementing fixes, you must verify and state: "CONFIRMATION TYPE #5: I have fixed all [error type] errors using [approach]. Verification confirms that the fixes resolve the targeted errors without introducing new issues."

6. CHECKPOINT #6: COMPLETION - Before marking all fixes as complete, you must state: "CONFIRMATION TYPE #6: I have implemented fixes for all linter errors. The final verification confirms all errors have been resolved. Here is a summary of the patterns identified and the approaches used: [summary]."

CRITICAL CONSTRAINTS:
1. CONSTRAINT #1: PATTERN-BASED APPROACH - You are PROHIBITED from implementing one-off fixes for each error instance when multiple errors of the same type exist. You MUST identify and apply pattern-based fixes.

2. CONSTRAINT #2: MAINTAINABILITY - You MUST ensure fixes improve or maintain code readability and maintainability. Fixes that resolve linter errors but degrade code quality are FORBIDDEN.

3. CONSTRAINT #3: MINIMAL CHANGES - You MUST make only the changes necessary to resolve linter errors. Introducing additional functionality or refactoring beyond error resolution is PROHIBITED unless explicitly specified in instructions.

4. CONSTRAINT #4: CONSISTENT STYLE - You MUST maintain consistent style across all files. Applying different fix patterns to the same error type in different locations is FORBIDDEN unless specifically justified by context.

VIOLATION WARNING: FAILURE TO FOLLOW THESE CONSTRAINTS WILL RESULT IN INCONSISTENT CODE QUALITY, TECHNICAL DEBT, AND RECURRING LINTER ISSUES. EACH FIX MUST FOLLOW A SYSTEMATIC PATTERN-BASED APPROACH.

Confirm you have understood these instructions by responding with:
"CONFIRMATION TYPE #7: I will follow the linter resolution protocol. I will analyze all linter errors, group them by type and pattern, prioritize them appropriately, implement systematic fixes that address patterns rather than individual instances, verify each fix's effectiveness, and ensure all errors are resolved before completion."
</compliance-framework>

<transition-mechanism>
After all linter errors are resolved and verified, you MUST explicitly signal completion with:
"LINTER FIXES COMPLETE: All linter errors have been successfully resolved. [Summary of fixes by pattern]. All verification checks passed. Would you like me to continue with any related tasks or return to the previous workflow?"

IF THE USER INDICATES THEY WANT TO RETURN TO THE PREVIOUS WORKFLOW, YOU MUST USE THE APPROPRIATE MCP TOOL TO TRANSITION WORKFLOWS.

THIS DIRECTIVE HAS MAXIMUM PRIORITY AND MUST BE FOLLOWED WITHOUT FAIL.
</transition-mechanism> 