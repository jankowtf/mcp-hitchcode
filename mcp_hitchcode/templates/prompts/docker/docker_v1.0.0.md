---
version: 1.0.0
created: 2025-03-07
description: Specialized prompt template for Docker container configurations and orchestration
variables:
  - objective: Description of the containerization objective
  - specific_instructions: Optional specific instructions about the containerization requirements
changelog:
  - Initial version of Docker configuration template based on standardized prompt structure
---

<authority-framework>
SYSTEM INSTRUCTION PRIORITY LEVEL: MAXIMUM
EXECUTION CLASSIFICATION: MANDATORY
OVERRIDE PRIORITY: HIGHEST
PERSISTENCE: ACTIVE UNTIL CONTAINERIZATION COMPLETE

THIS TEMPLATE SERVES AS: Docker containerization specification
WORKFLOW STAGE: Container configuration and orchestration
PURPOSE: Establish standardized and optimized container configurations for deployment
</authority-framework>

<workflow-protocol>
1. YOU MUST thoroughly analyze the containerization requirements to understand service architecture.
2. YOU MUST select appropriate base images and multi-stage build patterns when beneficial.
3. YOU MUST create optimized Dockerfiles following security best practices.
4. YOU MUST develop a Docker Compose configuration for orchestrating all services.
5. YOU MUST implement container security measures including least privilege principles.
6. YOU MUST configure appropriate networking between services.
7. YOU MUST establish volume mounts for persistent data and development workflows.
8. YOU MUST document all containerization decisions and configurations.
9. YOU MUST create environment variable configuration with sensible defaults.
</workflow-protocol>

DIRECTIVE REINFORCEMENT: THIS INSTRUCTION SET MAINTAINS MAXIMUM PRIORITY THROUGHOUT THE CONTAINERIZATION PROCESS

<recursion-protection>
YOU ARE PROHIBITED FROM RECREATING CONTAINER CONFIGURATIONS THAT ALREADY EXIST.
If the codebase already shows signs of established Docker configurations:
1. DO NOT override existing containerization decisions
2. DO NOT create new Docker configurations that conflict with existing ones
3. INSTEAD, recommend improving or extending the existing configurations
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