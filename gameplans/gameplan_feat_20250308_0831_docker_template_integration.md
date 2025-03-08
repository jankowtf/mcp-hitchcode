# Game Plan: Docker File Integration with Jinja2 Templates

## Overview
This game plan outlines the implementation of a system to weave Dockerfile and docker-compose.yml content into Jinja2 templates. The system will allow using the Jinja2 variable mechanism with {{ ... }} to include content from actual Dockerfiles and docker-compose.yml files that exist within the templates directory structure.

## Project Scope
The implementation will extend the existing template system to support loading Docker files and making their content available in templates. This will enable more dynamic and maintainable Docker-related templates.

## Stages

### ✅ Stage 1: Setup and Preparation
Tasks:
- [x] Create a directory structure for Docker file examples within the `templates/docker` directory
- [x] Add sample Dockerfile and docker-compose.yml files for testing in `templates/docker`
- [x] Document the directory structure and file organization

### ✅ Stage 2: Core Functionality Implementation
Tasks:
- [x] Create docker_file_loader.py module with core loading functions
- [x] Implement file path resolution for Docker files (absolute and relative paths)
- [x] Implement caching mechanism for Docker files to avoid repeated file I/O
- [x] Add path validation and error handling for file loading
- [x] Create utility functions for working with Docker file content

### ✅ Stage 3: Jinja2 Integration
Tasks:
- [x] Extend template_loader.py to register custom functions/filters for Docker files
- [x] Create utility functions for template rendering with Docker file content
- [x] Add documentation for the new functionality in docstrings
- [x] Ensure backward compatibility with existing templates

### ✅ Stage 4: Testing and Validation
Tasks:
- [x] Create test templates that use Docker file loading
- [x] Test with various path formats and edge cases
- [x] Document usage examples
- [x] Create unit tests for the new functionality

### ✅ Stage 5: Improvements and Refinements
Tasks:
- [x] Update sample Dockerfile to use multi-stage builds and uv for Python package management
- [x] Fix import statements in __init__.py to avoid linter issues
- [x] Update documentation to reflect best practices in Docker file examples

## Implementation Details

### Docker File Loader Module
The `docker_file_loader.py` module will provide functions to:
- Locate and load Dockerfile and docker-compose.yml files from the `templates/docker` directory
- Cache loaded Docker files to avoid repeated file I/O
- Support relative paths within the templates directory
- Validate file paths and handle errors gracefully

### Jinja2 Integration
The integration with Jinja2 will:
- Add custom functions/filters for loading Docker files
- Make these functions available in templates via {{ docker_file('path/to/Dockerfile') }}
- Support loading docker-compose.yml files via {{ docker_compose('path/to/docker-compose.yml') }}
- Handle errors gracefully with appropriate error messages

### Example Usage
Templates will be able to include Docker file content like this:
```
# Example Dockerfile for a Python application
{{ docker_file('python/Dockerfile') }}

# Example docker-compose.yml for a multi-container application
{{ docker_compose('multi-container/docker-compose.yml') }}
```

Note: Paths are relative to the `templates/docker` directory.

## Reasoning
This approach extends the existing template system in a modular way without modifying its core functionality. It provides a clean and intuitive API for including Docker file content in templates, making it easy to maintain and update Docker-related templates.

## Impact Analysis
- **Positive Impacts**:
  - More maintainable Docker-related templates
  - Easier updates to Docker configurations
  - Better separation of concerns between templates and Docker configurations
  - Reduced duplication of Docker file content

- **Potential Risks**:
  - Need to ensure proper error handling for missing or invalid Docker files
  - Need to maintain backward compatibility with existing templates
  - Need to document the new functionality clearly

## Success Criteria
The implementation will be considered successful if:
1. Templates can include content from Dockerfile and docker-compose.yml files
2. The system handles errors gracefully
3. The implementation is well-documented
4. The system is tested with various path formats and edge cases 