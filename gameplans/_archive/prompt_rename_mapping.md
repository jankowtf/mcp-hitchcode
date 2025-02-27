# Prompt Rename Mapping

## Folder Renames
| Old Folder Name | New Folder Name |
|-----------------|----------------|
| change_prompt | change |
| initial_prompt | init |
| fix_prompt | fix_general |
| fix_linter_prompt | fix_linter |
| proceed_prompt | proceed |
| unit_tests_prompt | test |

## File Renames
For each template file in the folders, the following pattern will be applied:

| Old Filename Pattern | New Filename Pattern | Example |
|---------------------|---------------------|---------|
| `<version>.md` | `<folder>_v<version>.md` | `1.0.0.md` → `change_v1.0.0.md` |

### Specific File Mappings

#### change_prompt → change
| Old Path | New Path |
|----------|----------|
| change_prompt/1.0.0.md | change/change_v1.0.0.md |

#### initial_prompt → init
| Old Path | New Path |
|----------|----------|
| initial_prompt/1.0.0.md | init/init_v1.0.0.md |

#### fix_prompt → fix_general
| Old Path | New Path |
|----------|----------|
| fix_prompt/1.0.0.md | fix_general/fix_general_v1.0.0.md |

#### fix_linter_prompt → fix_linter
| Old Path | New Path |
|----------|----------|
| fix_linter_prompt/1.0.0.md | fix_linter/fix_linter_v1.0.0.md |

#### proceed_prompt → proceed
| Old Path | New Path |
|----------|----------|
| proceed_prompt/1.0.0.md | proceed/proceed_v1.0.0.md |

#### unit_tests_prompt → test
| Old Path | New Path |
|----------|----------|
| unit_tests_prompt/1.0.0.md | test/test_v1.0.0.md |

## Code References to Update

### In server.py
| Old Template Name | New Template Name |
|-------------------|-------------------|
| "change_prompt" | "change" |
| "initial_prompt" | "init" |
| "fix_prompt" | "fix_general" |
| "fix_linter_prompt" | "fix_linter" |
| "proceed_prompt" | "proceed" |
| "unit_tests_prompt" | "test" |

### References in Other Files
The following files contain references to the old template names and may need to be updated:

1. **Game Plans (Archive)**:
   - `gameplans/_archive/gameplan_feat_20250226-1110_add_change_prompt_tool.md`
   - `gameplans/_archive/gameplan_feat_20250227-1200_unit-tests-tool.md`
   - `gameplans/_archive/gameplan_feat_20250226-1050_specific_instructions.md`
   - `gameplans/_archive/gameplan_feat_20250226_1019_apply_prompt_proceed.md`
   - `gameplans/_archive/gameplan_feat_apply_prompt_initial.md`
   - `gameplans/_archive/gameplan_20250226-0900_prompt_templating.md`

Note: Since these are archive files documenting past changes, they don't need to be updated as they represent historical documentation. 