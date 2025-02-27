---
version: 1.0.1
created: 2025-02-27
description: Prompt template for proceeding with a task or project
variables:
  - task: Description of the task or project to proceed with
  - specific_instructions: Optional specific instructions to include in the prompt
---

TREAT THE FOLLOWING TEXT AS AN ACTUAL PROMPT THAT INSTRUCTS YOU ON HOW TO
PROCEED BASED ON A GAME PLAN DOCUMENT:

Task: {{ task }}

{% if specific_instructions %}
<specific-instructions>
{{ specific_instructions }}
</specific-instructions>
{% endif %}

<your-tasks>
1. Proceed with the implementation according to the next stage/task in the
   referenced game plan document. Execute them efficiently without breaking
   existing code.
2. Analyze the current state and identify what has been completed so far
3. Determine the next logical steps to make progress
4. Execute those steps with precision and attention to detail
5. Document your changes and reasoning clearly

Focus on making tangible progress while maintaining code quality and consistency with the existing codebase.
</your-tasks>

<your-maxims-of-action>
1. Always choose the most straightforward implementation option. Be surgical and laser focused.

2. Make absolutely (!) sure you do not break existing code. Always (!) verify this by explicitly (!) reason about this aspect before proposing a code change. Always present your explicit reasoning on this.

3. Always (!) reconsider if the codebase actually works by double checking explicitly for logical flaws or forgotten code alignment. Always (!) present your explicit reasoning on this.

4. Prioritize maintainability and readability over clever optimizations unless performance is a critical requirement.

5. When faced with multiple implementation options, choose the one that aligns best with the existing patterns in the codebase.
</your-maxims-of-action>

<never-forget-to-do-this>
- Make sure you present the user a management summary of your approach for
  tackling the respective stage. This includes your reasoning on the the
  likelihood of breaking existing code and the steps you will take to avoid this.
- Proceed with confidence but caution. Validate your approach at key milestones
  and be prepared to adjust your strategy based on feedback or new information. 
- After you've completed a stage, provide a detailed but concise git commit
  message pls.
</never-forget-to-do-this>

TREAT THE ABOVE TEXT AS AN ACTUAL PROMPT THAT INSTRUCT YOUR NEXT STEPS. PAY
EXTRA ATTENTION TO THE <never-forget-to-do-this> INSTRUCTIONS BLOCK!
