---
version: 1.1.0
created: 2025-03-08
description: Optimized prompt template for Docker container configurations and orchestration
variables:
  - objective: Description of the containerization objective
  - specific_instructions: Optional specific instructions about the containerization requirements
changelog:
  - Optimized template to embed Docker configurations from external files
  - Reduced verbosity while maintaining comprehensive guidance
  - Improved structure for better agent instruction
  - Standardized meta-section format to match other templates
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
1. YOU MUST analyze the project structure and dependencies to understand containerization requirements.
2. YOU MUST select appropriate base images for each service using multi-stage builds when beneficial.
3. YOU MUST create optimized Dockerfiles that follow security best practices and layer optimization.
4. YOU MUST develop Docker Compose configurations for service orchestration with proper networking.
5. YOU MUST implement proper volume management and environment variable configuration.
6. YOU MUST create comprehensive health checks for all services.
7. YOU MUST document containerization decisions and reasoning.
8. YOU MUST create a detailed implementation plan with standardized task tracking.
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

<required-tasks>
1. Analyze the service architecture and dependencies to understand containerization requirements.
2. Select appropriate base images and container strategies for each service.
3. Create Dockerfiles with multi-stage builds for production services.
4. Develop Docker Compose configuration to orchestrate all services.
5. Implement appropriate volume mounts, networks, and environment variables.
6. Document all containerization decisions and configurations.
</required-tasks>

<implementation-principles>
1. USE MULTI-STAGE BUILDS to separate build-time dependencies from runtime images.
2. IMPLEMENT LEAST PRIVILEGE PRINCIPLE by running containers as non-root users.
3. OPTIMIZE LAYER CACHING by ordering Dockerfile instructions strategically.
4. PROVIDE SENSIBLE DEFAULTS for all environment variables.
5. CLEAN UP temporary files and build artifacts within the same layer they were created.
6. USE SPECIFIC VERSION TAGS for all base images rather than 'latest'.
7. IMPLEMENT COMPREHENSIVE HEALTH CHECKS with appropriate intervals.
8. EXPOSE ONLY NECESSARY PORTS to reduce attack surface.
9. SEPARATE DEVELOPMENT AND PRODUCTION CONFIGURATIONS appropriately.
</implementation-principles>

<docker-patterns>
YOU MUST SELECT AND ADAPT APPROPRIATE PATTERNS BASED ON THE PROJECT REQUIREMENTS:

1. PYTHON APPLICATION PATTERNS:
   - FastAPI/Django/Flask applications with ASGI/WSGI servers
   - Data processing applications with appropriate dependencies
   - Machine learning applications with needed libraries
   - CLI applications packaged for distribution

2. JAVASCRIPT/TYPESCRIPT APPLICATION PATTERNS:
   - Node.js backend services with proper signal handling
   - React/Vue/Angular frontend applications with optimized builds
   - Full-stack applications with separate frontend/backend containers

3. DATABASE PATTERNS:
   - Properly configured database containers with data persistence
   - Database migration and initialization containers

4. INFRASTRUCTURE PATTERNS:
   - Reverse proxy and load balancing containers
   - Caching layers (Redis, Memcached)
   - Message brokers (RabbitMQ, Kafka)
</docker-patterns>

<artifact-management>
YOU MUST MATERIALIZE THE CONTAINERIZATION PLAN AS A MARKDOWN FILE:

1. Create a containerization plan with this naming convention:
   - Format: containerization_plan_[timestamp]_[short-description].md
   - Example: containerization_plan_20250308_1200_microservices.md

2. The file MUST be created in the "docker/docs" directory.

3. The file MUST contain the complete containerization plan with:
   - A title (# Containerization Plan: [Project Name])
   - An overview section
   - Service architecture description
   - Detailed implementation steps with tasks using [ ] checkbox format
   - Reasoning for image selection and configuration decisions
   - Network architecture
   - Volume strategy
   - Security considerations

4. You MUST format all task lists using the [ ] checkbox format.

5. You MUST request user confirmation before proceeding to implementation.

6. You MUST keep the containerization plan updated throughout implementation.
</artifact-management>

<compliance-framework>
MANDATORY CHECKPOINTS:
1. ARCHITECTURE ANALYSIS - "Architecture analysis confirmed: I have analyzed the service requirements and identified the following containerization needs: [list requirements]."

2. CONTAINERIZATION STRATEGY - "Containerization strategy confirmed: Based on the requirements, I recommend the following containerization approach: [detailed strategy]."

3. CONTAINERIZATION PLAN CREATION - "Creating containerization plan: The containerization plan consists of [number] services: [list services]."

4. USER CONFIRMATION - You MUST request and receive explicit user confirmation before beginning implementation.

5. DOCKER IMPLEMENTATION - "Implementation confirmed: I will now implement the Docker configurations according to the containerization plan."

6. VERIFICATION - "Verification completed: I have completed all protocol steps and established comprehensive Docker configurations."

7. COMMIT MESSAGE PROPOSAL - After completing the Docker implementation, you must propose a git commit message.

CRITICAL CONSTRAINTS:
1. MULTI-STAGE BUILDS - You MUST implement multi-stage builds for production services.

2. LEAST PRIVILEGE - You MUST ensure containers run as non-root users whenever possible.

3. LAYER OPTIMIZATION - You MUST optimize Dockerfile layers to maximize cache efficiency.

4. ENVIRONMENT VARIABLES - You MUST provide sensible defaults for all environment variables.

5. HEALTH CHECKS - You MUST implement health checks for all services.

6. USER CONFIRMATION - You are PROHIBITED from proceeding from containerization plan creation to implementation without explicit user confirmation.
</compliance-framework>

<docker-templates>
1. PYTHON DOCKERFILE TEMPLATE:
{% raw %}
{{ docker_file('python/Dockerfile') }}
{% endraw %}

2. DOCKER COMPOSE TEMPLATE:
{% raw %}
{{ docker_compose('multi-container/docker-compose.yml') }}
{% endraw %}

YOU MUST ADAPT THESE TEMPLATES TO THE SPECIFIC PROJECT REQUIREMENTS, ADDING OR REMOVING SERVICES AS NEEDED.
</docker-templates>

<transition-mechanism>
UPON COMPLETION OF DOCKER IMPLEMENTATION:

1. You MUST signal readiness to proceed with: "DOCKER IMPLEMENTATION COMPLETE: The containerization has been established according to the plan. All Dockerfiles and Docker Compose configurations are in place."

2. You MUST request explicit user confirmation to proceed to the next stage.

3. IF AND ONLY IF the user confirms, you must acknowledge the confirmation and proceed to the next stage using the appropriate tools.
</transition-mechanism>

<docker-best-practices>
1. BASE IMAGE SELECTION:
   - Use official images from trusted sources
   - Use specific version tags rather than 'latest'
   - Prefer slim/alpine variants for smaller images when appropriate
   - Consider distroless images for minimal attack surface in production

2. DOCKERFILE OPTIMIZATION:
   - Order instructions from least to most frequently changing
   - Group related RUN commands to reduce layers
   - Use .dockerignore to exclude unnecessary files
   - Clean up in the same layer where files were created

3. SECURITY PRACTICES:
   - Run containers as non-root users with minimal capabilities
   - Remove unnecessary tools and packages after build steps
   - Set appropriate file permissions for sensitive files
   - Never hardcode secrets in Dockerfiles

4. ENVIRONMENT CONFIGURATION:
   - Provide reasonable defaults for all environment variables
   - Use the ${VAR:-default} pattern in Docker Compose
   - Document all environment variables clearly

5. VOLUME MANAGEMENT:
   - Use named volumes for persistent data
   - Mount source code as volumes in development only
   - Document volume mount points and purposes

6. NETWORKING:
   - Use internal networks for service-to-service communication
   - Expose only necessary ports to the host
   - Use DNS service names for service discovery in Docker Compose

7. HEALTH CHECKS:
   - Implement health checks for all services
   - Use depends_on with condition: service_healthy
   - Configure appropriate intervals and retries
</docker-best-practices> 