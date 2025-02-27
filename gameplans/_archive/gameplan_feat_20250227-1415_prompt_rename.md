# Game Plan: Renaming Prompt Folders and Updating Template Filenames

## Overview
This game plan outlines the steps to rename the prompt folders and update the template filenames in the MCP Simple Tool. The goal is to make the folder names more concise and ensure the template filenames include the directory name for better organization.

## Current Structure
- Current folder names: `change_prompt`, `initial_prompt`, `fix_prompt`, `fix_linter_prompt`, `proceed_prompt`, `unit_tests_prompt`
- Current template filenames: `1.0.0.md`, etc.

## Target Structure
- New folder names: `change`, `init`, `fix_general`, `fix_linter`, `proceed`, `test`
- New template filenames: `change_v1.0.0.md`, `init_v1.0.0.md`, etc.

## Stage 1: Analysis and Preparation

- [x] **Task 1.1: Create a backup of the current templates**
  - Create a backup of the entire `prompts` directory to ensure we can revert if needed
  - This will serve as a safety net in case anything goes wrong during the migration

- [x] **Task 1.2: Map the folder and file renames**
  - Create a detailed mapping of old folder names to new folder names
  - Create a detailed mapping of old filenames to new filenames
  - This mapping will guide the implementation and ensure nothing is missed

- [x] **Task 1.3: Identify code references to template names**
  - Identify all places in the codebase that reference the template names
  - This includes the `server.py` file where template names are used in the `render_prompt_template` function
  - Understanding these references is crucial to ensure we don't break existing functionality

## Stage 2: Update Template Loader

- [x] **Task 2.1: Modify the template loader to handle the new filename pattern**
  - Update the `_build_version_registry` function to recognize the new filename pattern
  - The current pattern is `^\d+\.\d+\.\d+\.md$` (e.g., `1.0.0.md`)
  - The new pattern should be `^[a-z_]+_v\d+\.\d+\.\d+\.md$` (e.g., `change_v1.0.0.md`)
  - This change is critical to ensure the template loader can find and load the templates

- [x] **Task 2.2: Update the version extraction logic**
  - Modify how version strings are extracted from filenames
  - Currently, it removes the `.md` extension to get the version
  - The new logic needs to extract the version from the `_v1.0.0.md` format
  - This ensures version comparison and selection work correctly

- [x] **Task 2.3: Test the updated template loader**
  - Create test files with the new naming pattern
  - Verify that the template loader can correctly identify and load these files
  - This testing is crucial before proceeding with the actual migration

## Stage 3: Migrate Templates

- [x] **Task 3.1: Create the new directory structure**
  - Create the new directories with the updated names
  - This prepares the filesystem for the template migration

- [x] **Task 3.2: Copy and rename template files**
  - Copy each template file to its new location with the updated filename
  - For example, copy `prompts/change_prompt/1.0.0.md` to `prompts/change/change_v1.0.0.md`
  - This preserves the original files until we're sure everything works

- [x] **Task 3.3: Verify template content**
  - Check that all template content has been correctly migrated
  - Ensure no templates were missed during the migration
  - This verification step helps catch any issues before updating the code

## Stage 4: Update Code References

- [x] **Task 4.1: Update references in server.py**
  - Update all references to the old template names in the `server.py` file
  - This includes the `render_prompt_template` calls in the various `apply_prompt_*` functions
  - These changes ensure the code uses the new template names

- [x] **Task 4.2: Update any other code references**
  - Search for and update any other references to the template names in the codebase
  - This ensures all parts of the application use the new template names

- [x] **Task 4.3: Test the updated code**
  - Run the application and test each prompt tool
  - Verify that all templates are correctly loaded and rendered
  - This testing ensures the changes haven't broken any functionality

## Stage 5: Cleanup

- [x] **Task 5.1: Remove the old directories and files**
  - Once everything is working correctly, remove the old directories and files
  - This cleanup step ensures the codebase is clean and organized

- [x] **Task 5.2: Update documentation**
  - Update any documentation that references the template names
  - This ensures the documentation is consistent with the code

- [x] **Task 5.3: Final verification**
  - Perform a final verification of all functionality
  - Ensure all templates are correctly loaded and rendered
  - This final check confirms everything is working as expected

## Project Completion

**Status: COMPLETED ✅**

All stages of the prompt folder renaming project have been successfully completed:

- Stage 1: Planning and preparation ✅
- Stage 2: Implementation preparation ✅
- Stage 3: Migration of templates ✅
- Stage 4: Update code references ✅
- Stage 5: Cleanup ✅

The project has been fully implemented with all templates successfully migrated to the new directory structure, all code references updated, and comprehensive verification tests confirming that all functionality works as expected.

**Final verification results:**
- Directory structure verification: PASSED
- Template loading verification: PASSED
- Server functions verification: PASSED

All temporary files have been cleaned up, and the project is now complete.

## Implementation Details

### Template Loader Changes
The key changes to the template loader will be in the `_build_version_registry` function:

```python
# Current pattern
if re.match(r"^\d+\.\d+\.\d+\.md$", filename):
    version_str = filename[:-3]  # Remove the .md extension
    version_files.append((version_str, filename))

# New pattern
if re.match(r"^[a-z_]+_v(\d+\.\d+\.\d+)\.md$", filename):
    version_str = re.search(r"_v(\d+\.\d+\.\d+)\.md$", filename).group(1)
    version_files.append((version_str, filename))
```

### Server.py Changes
The changes to `server.py` will be straightforward:

```python
# Current
response_text = render_prompt_template(
    "initial_prompt",
    version_str=version,
    project=project,
    specific_instructions=specific_instructions,
)

# New
response_text = render_prompt_template(
    "init",
    version_str=version,
    project=project,
    specific_instructions=specific_instructions,
)
```

Similar changes will be needed for all other template references.

## Risks and Mitigations

1. **Risk**: Breaking existing functionality if template names are missed
   - **Mitigation**: Comprehensive testing of all prompt tools after the changes

2. **Risk**: Version extraction logic might not work correctly with the new filename format
   - **Mitigation**: Thorough testing of the template loader with the new filename pattern

3. **Risk**: Some templates might be missed during migration
   - **Mitigation**: Verify all templates are migrated and test all functionality

4. **Risk**: The application might not find templates at runtime
   - **Mitigation**: Keep backups of the original templates until everything is verified

## Conclusion
This game plan provides a comprehensive approach to renaming the prompt folders and updating the template filenames. By following these steps, we can ensure a smooth transition to the new naming scheme without breaking existing functionality. 