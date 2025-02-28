---
version: 1.0.0
description: Template for fixing linter errors
---

Issue: {{ issue }}

<your-task>
Do a step by step root cause analysis for the given linter errors. Then synthesize the necessary changes to fix these errors.
</your-task>

<your-agency>
Create or update a task-based (including checkboxes) game plan with stages. Use filename structure `gameplan_linter_<yyyymmdd-hhmm>_<id>.md` in directory `gameplans`. IMPORTANT: Please ask me for the concrete timestamp to use and let me verify the ID before creating the game plan doc.

Make sure you also add your reasoning and top-level details/references on how to implement the fix(es) to the respective tasks in the game plan.

Also make sure you present me a management summary of your approach and the stages in the chat.
</your-agency>

<your-maxim-of-action>
1. Always choose the most straightforward implementation option. Be surgical and laser focused.

2. Make absolutely (!) sure you do not break existing code. Always (!) verify this by explicitly (!) reason about this aspect before proposing a code change. Always present your explicit reasoning on this.

3. Always (!) reconsider if the codebase actually works by double checking explicitly for logical flaws or forgotten code alignment. Always (!) present your explicit reasoning on this.

4. Linter errors are often related to changes in package interfaces. Find and read through the most recent developer docs on the relevant packages.

5. When fixing linter errors, prioritize maintaining compatibility with existing code over introducing new patterns.
</your-maxim-of-action>

<very-important>
You never just proceed with implementing stages of the game plan, you always ask for my confirmation for this.
</very-important> 