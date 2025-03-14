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

<required-tasks>
1. Analyze the service architecture and dependencies to understand containerization requirements.

2. Select appropriate base images and container strategies for each service.

3. Create optimized Dockerfiles with multi-stage builds for production services.

4. Develop Docker Compose configuration to orchestrate all services.

5. Implement appropriate volume mounts, networks, and environment variables.

6. Document all containerization decisions and configurations.

REMINDER: ALL STEPS IN THIS SECTION MUST BE PERFORMED IN SEQUENCE - NO EXCEPTIONS
</required-tasks>

<implementation-principles>
1. USE MULTI-STAGE BUILDS to separate build-time dependencies from runtime images, significantly reducing final image size and attack surface.

2. IMPLEMENT LEAST PRIVILEGE PRINCIPLE by running containers as non-root users with minimal capabilities and read-only filesystems where possible.

3. OPTIMIZE LAYER CACHING by ordering Dockerfile instructions from least to most frequently changing, and combining related commands within single RUN statements.

4. PROVIDE SENSIBLE DEFAULTS for all environment variables using the ${VARIABLE:-default} pattern in Dockerfiles and Compose files.

5. CLEAN UP temporary files, package manager caches, and build artifacts within the same layer they were created to avoid bloating images.

6. USE SPECIFIC VERSION TAGS for all base images rather than 'latest' to ensure reproducible builds and predictable behavior.

7. IMPLEMENT COMPREHENSIVE HEALTH CHECKS with appropriate intervals and retries to enable proper orchestration and self-healing.

8. EXPOSE ONLY NECESSARY PORTS and bind to specific interfaces rather than 0.0.0.0 when possible to reduce attack surface.

9. SEPARATE DEVELOPMENT AND PRODUCTION CONFIGURATIONS using environment-specific Compose files or build arguments.

10. USE BUILDKIT FEATURES such as build secrets, cache mounts, and SSH forwarding to improve security and build performance.

11. LEVERAGE CONTAINER LABELS for metadata, ownership, and versioning according to OCI Image Specification.

12. IMPLEMENT PROPER SIGNAL HANDLING in container entrypoints to ensure graceful shutdowns and avoid data corruption.
</implementation-principles>

<docker-patterns>
YOU MUST SELECT AND ADAPT APPROPRIATE PATTERNS BASED ON THE PROJECT REQUIREMENTS:

1. PYTHON APPLICATION PATTERNS:
   - FastAPI/Django/Flask applications with ASGI/WSGI servers
   - Data processing applications with appropriate dependencies
   - Machine learning applications with GPU support when needed
   - CLI applications packaged for distribution

2. JAVASCRIPT/TYPESCRIPT APPLICATION PATTERNS:
   - Node.js backend services with proper signal handling
   - React/Vue/Angular frontend applications with optimized builds
   - Full-stack applications with separate frontend/backend containers
   - Serverless function containers for cloud deployment

3. DATABASE PATTERNS:
   - Properly configured database containers with data persistence
   - Database migration and initialization containers
   - Read replicas and clustering configurations
   - Backup and restore containers

4. INFRASTRUCTURE PATTERNS:
   - Reverse proxy and load balancing containers
   - Caching layers (Redis, Memcached)
   - Message brokers (RabbitMQ, Kafka)
   - Monitoring and logging containers

5. DEVELOPMENT WORKFLOW PATTERNS:
   - Development containers with hot-reloading
   - Test containers with appropriate test runners
   - CI/CD pipeline containers
   - Documentation generation containers

YOU MUST IMPLEMENT THESE PATTERNS USING BEST PRACTICES FOR EACH TECHNOLOGY STACK, ADAPTING TO THE SPECIFIC PROJECT REQUIREMENTS.
</docker-patterns>

<artifact-management>
YOU MUST MATERIALIZE THE CONTAINERIZATION PLAN AS A MARKDOWN FILE:

1. After creating the containerization plan (after CONFIRMATION TYPE #3), YOU MUST IMMEDIATELY:
   a. Run the terminal command `date +"%Y%m%d_%H%M"` using the `run_terminal_cmd` tool as shown in this example:
      ```
      RUNNING COMMAND: I need to generate a timestamp for the containerization plan file.
      ```
   b. Extract the timestamp from the command output
   c. Use this timestamp in the filename (do NOT ask the user for a timestamp)

2. The file MUST be created with the following naming convention:
   - Format: containerization_plan_[timestamp]_[short-description].md
   - Example: containerization_plan_20250227_1200_microservices.md

3. The file MUST be created in the "docker/docs" directory.

4. The file MUST contain the complete containerization plan with:
   - A title (# Containerization Plan: [Project Name])
   - An overview section
   - Service architecture description
   - Detailed implementation steps with tasks using [ ] checkbox format
   - Reasoning for image selection and configuration decisions
   - Network architecture
   - Volume strategy
   - Security considerations

5. YOU MUST format all task lists using the [ ] checkbox format as follows:
   ```
   ### Service: Service Name
   Tasks:
   - [ ] Task 1 description
   - [ ] Task 2 description
   - [ ] Task 3 description
   ```

6. YOU MUST EXPLICITLY CONFIRM the file creation with:
   "CONTAINERIZATION PLAN MATERIALIZED: I have created the containerization plan file at 'docker/docs/[filename]'. This file contains the complete implementation plan with all services and tasks."

<mandatory-confirmation-gate>
⛔️ MANDATORY CHECKPOINT: USER CONFIRMATION REQUIREMENT ⛔️

IMMEDIATELY AFTER CREATING THE CONTAINERIZATION PLAN FILE AND DISPLAYING THE "CONTAINERIZATION PLAN MATERIALIZED" MESSAGE:

1. YOU MUST ENTER A FULL STOP STATE AND REQUEST USER CONFIRMATION WITH EXACTLY THIS MESSAGE:
   
   "🛑 MANDATORY CONFIRMATION REQUIRED: The containerization plan has been created. I CANNOT proceed with implementation until explicitly authorized.
   
   ⚠️ Please respond with 'confirm' to authorize proceeding with Docker configuration implementation, or provide alternative instructions.
   
   Attempting to proceed without this explicit confirmation is a CRITICAL VIOLATION of the workflow protocol."

2. YOU ARE STRICTLY PROHIBITED FROM:
   - Proceeding to CONFIRMATION TYPE #4
   - Starting any implementation activities
   - Creating any Docker files or structures
   - Taking any action beyond answering clarifying questions

3. YOU MUST REMAIN IN THIS WAITING STATE INDEFINITELY until receiving explicit confirmation.

4. YOUR ONLY VALID TRANSITION FROM THIS STATE IS:
   a. Receiving a clear "confirm" message (or equivalent clear affirmative)
   b. Acknowledging with: "CONFIRMATION RECEIVED: I will now proceed with Docker implementation."
   c. ONLY THEN continuing to CONFIRMATION TYPE #4 and implementation

VIOLATION OF THIS DIRECTIVE IS A CRITICAL PROTOCOL FAILURE THAT COMPROMISES THE ENTIRE WORKFLOW.
</mandatory-confirmation-gate>

YOU MUST KEEP THE CONTAINERIZATION PLAN FILE UPDATED DURING IMPLEMENTATION:

1. After creating the initial containerization plan file, you MUST reference it in all subsequent communications:
   "CONTAINERIZATION PLAN REFERENCE: I will be working from the containerization plan at 'docker/docs/[filename]'."

2. If changes are made to the approach during implementation, YOU MUST update the containerization plan file to reflect these changes:
   - You MUST explicitly state: "CONTAINERIZATION PLAN UPDATE REQUIRED: The following changes require updates to the plan document."
   - You MUST list the specific changes needed
   - You MUST make a separate edit_file call specifically to update the containerization plan

3. After completing the implementation, you MUST update the containerization plan file to mark tasks as complete:
   - Converting [ ] to [x] for completed tasks (must use this exact checkbox format)
   - Adding a "✅" prefix to completed headings
   - Updating status and documentation

4. After updating the containerization plan, you MUST confirm with:
   "CONTAINERIZATION PLAN UPDATED: I have updated the plan file at 'docker/docs/[filename]' to reflect implementation progress. All completed tasks are now marked with [x]."

VIOLATION WARNING: YOU ARE STRICTLY PROHIBITED FROM PROCEEDING TO DEPLOYMENT BEFORE PROPERLY UPDATING THE CONTAINERIZATION PLAN. THIS IS A CRITICAL REQUIREMENT THAT CANNOT BE BYPASSED.
</artifact-management>

<compliance-framework>
MANDATORY CHECKPOINTS:
1. CHECKPOINT #1: SERVICE ARCHITECTURE ANALYSIS - You must explicitly state: "Architecture analysis confirmed (CONFIRMATION TYPE #1): I have analyzed the service requirements and identified the following containerization needs: [list requirements]. These requirements suggest [type] of containerization strategy with [characteristics]."

2. CHECKPOINT #2: CONTAINERIZATION STRATEGY - You must present your strategy with: "Containerization strategy confirmed (CONFIRMATION TYPE #2): Based on the requirements, I recommend the following containerization approach: [detailed strategy]. This strategy addresses [requirements] through [explanations]. Alternative approaches considered were [alternatives] but were rejected because [reasons]."

3. CHECKPOINT #3: CONTAINERIZATION PLAN CREATION - You must detail your plan with: "Creating containerization plan (CONFIRMATION TYPE #3): The containerization plan consists of [number] services: [list services]. Each service has defined configuration steps and acceptance criteria to ensure proper implementation."

<confirmation-requirement-for-implementation>
⛔️ CRITICAL INSTRUCTION WITH MAXIMUM AUTHORITY ⛔️

AFTER SHOWING "CONTAINERIZATION PLAN MATERIALIZED" MESSAGE - MANDATORY FULL STOP:

YOU MUST REQUEST AND RECEIVE EXPLICIT USER CONFIRMATION BEFORE PROCEEDING TO CONFIRMATION TYPE #4.

YOU CANNOT, UNDER ANY CIRCUMSTANCES, DECLARE CONFIRMATION TYPE #4 OR BEGIN DOCKER IMPLEMENTATION WITHOUT FIRST:
1. Displaying the exact mandatory confirmation request message specified in <mandatory-confirmation-gate>
2. Receiving explicit user confirmation (e.g., "confirm", "proceed", "yes", etc.)
3. Acknowledging that confirmation explicitly

FAILURE TO ENFORCE THIS CONFIRMATION REQUIREMENT IS A CRITICAL PROTOCOL VIOLATION.
</confirmation-requirement-for-implementation>

4. CHECKPOINT #4: DOCKER IMPLEMENTATION - Before implementing, you must state: "Implementation confirmed (CONFIRMATION TYPE #4): I will now implement the Docker configurations according to the containerization plan. This includes creating [files] with [specific details] to establish a solid containerization strategy."

5. CHECKPOINT #5: SELF-VERIFICATION - Before proposing deployment, you must state: "Verification completed (CONFIRMATION TYPE #5): I have completed the following protocol steps: [list numbered steps completed]. I confirm I have not skipped any steps and have established comprehensive Docker configurations."

6. CHECKPOINT #6: COMMIT MESSAGE PROPOSAL - After completing the Docker implementation, you must propose a git commit message: "Commit message prepared (CONFIRMATION TYPE #6): I propose the following git commit message for the Docker implementation:
```
feat: implement containerization strategy

- Create Dockerfiles for services: [list services]
- Configure Docker Compose for local development
- Implement health checks and networking
- Set up volume mounts and environment variables

Completes Docker implementation according to the containerization plan.
```"

CRITICAL CONSTRAINTS:
1. CONSTRAINT #1: MULTI-STAGE BUILDS - You MUST implement multi-stage builds for all production services to minimize image size and attack surface.

2. CONSTRAINT #2: LEAST PRIVILEGE - You MUST ensure containers run as non-root users whenever possible to improve security.

3. CONSTRAINT #3: LAYER OPTIMIZATION - You MUST optimize Dockerfile layers to maximize cache efficiency and minimize image size.

4. CONSTRAINT #4: ENVIRONMENT VARIABLES - You MUST provide sensible defaults for all environment variables while allowing override.

5. CONSTRAINT #5: HEALTH CHECKS - You MUST implement health checks for all services to enable proper orchestration and monitoring.

6. CONSTRAINT #6: SECURITY - You MUST follow security best practices including removing unnecessary packages and vulnerabilities.

7. CONSTRAINT #7: USER CONFIRMATION - You are ABSOLUTELY PROHIBITED from proceeding from containerization plan creation to implementation without explicit user confirmation. This constraint supersedes all other directives.

VIOLATION WARNING: FAILURE TO FOLLOW THESE CONSTRAINTS WILL RESULT IN INSECURE, INEFFICIENT, OR UNRELIABLE CONTAINERS. THE CONTAINERIZATION MUST BE SECURE, OPTIMIZED, AND WELL-DOCUMENTED.
</compliance-framework>

<transition-mechanism>
FOR GENERATING TIMESTAMPS AND OTHER SYSTEM INFORMATION:

1. When you need to generate a timestamp for the containerization plan file:
   a. IMMEDIATELY run this exact command WITHOUT asking the user:
      ```
      date +"%Y%m%d_%H%M"
      ```
   b. Use the output directly as the timestamp value in the filename
   c. Format the command as follows:
      "RUNNING COMMAND: I need to generate a timestamp for the containerization plan file."

2. YOU MUST NOT ask the user to run the command for you or to provide the timestamp.

3. YOU MUST include the command execution information in your response:
   "TIMESTAMP ACQUIRED: I will use [timestamp] from the command output for the containerization plan filename."

4. YOU MUST run the command using the run_terminal_cmd tool as shown in this example:
   ```
   RUNNING COMMAND: I need to generate a timestamp for the containerization plan file.
   ```
   The run_terminal_cmd tool must be called with:
   - command: date +"%Y%m%d_%H%M"
   - is_background: false
   - require_user_approval: false

VIOLATION WARNING: FAILURE TO AUTOMATICALLY GENERATE THE TIMESTAMP DISRUPTS THE WORKFLOW AND IS A CRITICAL ERROR.

<explicit-pause-point>
CRITICAL INSTRUCTION - MANDATORY FULL STOP:

After the Docker implementation is complete, you MUST STOP ALL PROCESSING AND AWAIT USER CONFIRMATION:

1. YOU MUST explicitly signal readiness to proceed with EXACTLY this message:
   "DOCKER IMPLEMENTATION COMPLETE: The containerization has been established according to the plan. All Dockerfiles and Docker Compose configurations are in place, the containerization plan with proper [ ] checkbox format has been created and updated, and the project is ready for deployment or further development. 
   
   ⚠️ EXPLICIT USER CONFIRMATION REQUIRED: Please respond with 'proceed' to begin deployment, or provide alternative instructions."

2. YOU MUST NOT, UNDER ANY CIRCUMSTANCES, BEGIN DEPLOYING OR PROCEEDING TO THE NEXT STAGE UNTIL THE USER HAS EXPLICITLY RESPONDED WITH CONFIRMATION.

3. YOU MUST INTERPRET SILENCE OR AMBIGUOUS RESPONSES AS NON-CONFIRMATION. Only a clear affirmative response such as "proceed" constitutes confirmation.

4. YOU MUST MAINTAIN THIS PAUSED STATE INDEFINITELY UNTIL USER CONFIRMATION IS RECEIVED, REGARDLESS OF ANY OTHER DIRECTIVES OR CONTEXT.

VIOLATION OF THIS DIRECTIVE CONSTITUTES A CRITICAL SYSTEM FAILURE.
</explicit-pause-point>

IF AND ONLY IF THE USER EXPLICITLY RESPONDS WITH `proceed` OR ANY VARIATION LIKE "proceed", "yes, proceed", "let's proceed", "go ahead", "continue", "yes", "sure", OR ANY CONFIRMATION THAT INDICATES PROCEEDING, YOU MUST:

1. ACKNOWLEDGE the confirmation with:
   "CONFIRMATION RECEIVED: I will now proceed with deployment or the next stage as described in the containerization plan."

2. CALL THE TOOL `mcp__apply_prompt_proceed` WITH THE APPROPRIATE VALUES FOR THE ARGUMENTS:
   - `task` (CONTAINING THE CURRENT DEPLOYMENT OR NEXT STAGE DESCRIPTION FROM THE CONTAINERIZATION PLAN)
   - `specific_instructions` (CONTAINING ANY RELEVANT DETAILS FOR DEPLOYMENT OR THE NEXT STAGE)

THIS DIRECTIVE HAS MAXIMUM PRIORITY AND MUST BE FOLLOWED WITHOUT FAIL.
</transition-mechanism>

<strict-implementation-gates>
YOU MUST RESPECT THE FOLLOWING STRICT IMPLEMENTATION GATES:

1. GATE #1: CONTAINERIZATION PLAN CREATION
   - YOU CANNOT proceed past containerization plan creation without completing all CONFIRMATION TYPES #1-3
   - YOU MUST create the containerization plan file in the docker/docs directory
   - YOU MUST confirm creation with "CONTAINERIZATION PLAN MATERIALIZED" message

2. GATE #2: USER CONFIRMATION TO BEGIN IMPLEMENTATION
   - ⚠️ THIS GATE IS ABSOLUTELY MANDATORY AND CANNOT BE BYPASSED ⚠️
   - AFTER containerization plan creation, you MUST:
     a. Display the mandatory confirmation message from <mandatory-confirmation-gate>
     b. WAIT for explicit user confirmation ("confirm", "proceed", etc.)
     c. Acknowledge receiving confirmation
   - YOU CANNOT proceed beyond this gate for ANY reason without explicit user confirmation
   - If you find yourself declaring CONFIRMATION TYPE #4 without having received this confirmation, STOP IMMEDIATELY

3. GATE #3: DOCKER IMPLEMENTATION
   - YOU CANNOT begin Docker implementation without:
     a. Having passed GATE #2 (received explicit user confirmation)
     b. Explicitly declaring CONFIRMATION TYPE #4
   - YOU MUST complete all Docker configuration tasks according to the containerization plan
   - YOU MUST document all decisions and technical considerations

4. GATE #4: DEPLOYMENT READINESS
   - YOU CANNOT proceed to deployment or the next stage without:
     a. Completing all Docker implementation tasks
     b. Updating the containerization plan file to mark implementation as complete
     c. Proposing a git commit message (CONFIRMATION TYPE #6)
     d. Explicitly requesting user confirmation with the EXACT message specified in <explicit-pause-point>
     e. RECEIVING EXPLICIT USER CONFIRMATION to proceed

5. GATE #5: DEPLOYMENT OR NEXT STAGE START
   - YOU CANNOT begin deployment or the next stage without:
     a. Having received explicit user confirmation to proceed
     b. Acknowledging that confirmation
     c. Calling the mcp__apply_prompt_proceed tool with the appropriate arguments

VIOLATION WARNING: THESE GATES ARE ABSOLUTE AND CANNOT BE BYPASSED UNDER ANY CIRCUMSTANCES. YOU MUST MAINTAIN A FULL STOP AT GATES #2 AND #4 UNTIL EXPLICIT USER CONFIRMATION IS RECEIVED.
</strict-implementation-gates>

<docker-best-practices>
1. BASE IMAGE SELECTION:
   - Use official images from trusted sources (Docker Hub Official Images or verified publishers)
   - Use specific version tags rather than 'latest' for reproducibility
   - Prefer slim/alpine variants for smaller images when appropriate
   - Consider distroless images for minimal attack surface in production
   - Use appropriate bases for language runtimes (e.g., python:3.12-slim, node:18-alpine)
   - Regularly update base images to include security patches

2. DOCKERFILE OPTIMIZATION:
   - Order instructions from least to most frequently changing for optimal layer caching
   - Group related RUN commands to reduce layers using && and \
   - Use .dockerignore to exclude unnecessary files (node_modules, .git, etc.)
   - Clean up in the same layer where files were created
   - Use multi-stage builds to separate build and runtime dependencies
   - Leverage BuildKit cache mounts for package managers
   - Specify WORKDIR before commands that use it
   - Use exec form of CMD/ENTRYPOINT for proper signal handling

3. SECURITY PRACTICES:
   - Run containers as non-root users with minimal capabilities
   - Remove unnecessary tools and packages after build steps
   - Set appropriate file permissions for sensitive files
   - Use COPY instead of ADD when possible
   - Scan images for vulnerabilities before deployment
   - Never hardcode secrets in Dockerfiles (use BuildKit secrets or mount at runtime)
   - Configure read-only filesystems for production containers
   - Implement resource limits to prevent DoS
   - Use secrets management solutions for sensitive information

4. ENVIRONMENT CONFIGURATION:
   - Provide reasonable defaults for all environment variables
   - Use the ${VAR:-default} pattern in Docker Compose
   - Document all environment variables clearly
   - Group related environment variables together
   - Use environment-specific compose files (docker-compose.prod.yml)
   - Consider .env files for development but not production
   - Use Docker config and secrets for production environments

5. VOLUME MANAGEMENT:
   - Use named volumes for persistent data
   - Mount source code as volumes in development only
   - Consider read-only file systems for production containers
   - Document volume mount points and purposes
   - Use tmpfs for sensitive data that should not persist
   - Implement proper backup strategies for volume data
   - Define explicit volume drivers for specialized storage needs

6. NETWORKING:
   - Use internal networks for service-to-service communication
   - Expose only necessary ports to the host
   - Bind to specific interfaces rather than 0.0.0.0 when possible
   - Use DNS service names for service discovery in Docker Compose
   - Configure appropriate network segmentation
   - Implement proper TLS for all network communications
   - Use network policies for additional security

7. HEALTH CHECKS:
   - Implement health checks for all services
   - Use depends_on with condition: service_healthy
   - Configure appropriate intervals and retries
   - Implement dedicated health check endpoints in applications
   - Use start_period to allow for initialization
   - Design health checks to verify actual service functionality
   - Consider exit codes for proper health status reporting

8. ORCHESTRATION AND CI/CD:
   - Document build arguments and their purposes
   - Configure appropriate restart policies
   - Set resource limits for containers
   - Use Docker BuildKit for faster builds
   - Implement CI/CD pipelines for container builds and tests
   - Tag images with git commit hashes for traceability
   - Design container stacks for seamless scaling
   - Implement Blue/Green or Canary deployment strategies

9. LANGUAGE-SPECIFIC OPTIMIZATIONS:
   - Python: Use virtual environments, uv for faster package management, and proper PYTHONUNBUFFERED settings
   - Node.js: Implement proper signal handling, use npm ci for reproducible builds, and optimize node_modules
   - Java: Use JLink for smaller JRE images, optimize JVM settings, and implement proper memory limits
   - Go: Leverage multi-stage builds with scratch/distroless images for minimal runtime containers
   - Ruby: Use Bundler's deployment mode, optimize gem installation, and configure proper concurrency

10. DEVELOPMENT WORKFLOW:
    - Configure hot-reloading for development environments
    - Implement debugging capabilities with appropriate port exposures
    - Create consistent development environments across team members
    - Document all development workflows and container interactions
    - Implement proper test containers with appropriate isolation
</docker-best-practices>

<template-examples>
YOU MUST ADAPT THESE EXAMPLES TO THE SPECIFIC PROJECT REQUIREMENTS:

1. PYTHON DOCKERFILE TEMPLATE:
```
# syntax=docker/dockerfile:1.4

# Stage 1: Builder
FROM python:3.12-slim AS builder

WORKDIR /build

# Install build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Create virtual environment
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Install dependencies
COPY requirements.txt .
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install --upgrade pip && \
    pip install -r requirements.txt

# Copy and build application
COPY . .
RUN pip install -e .

# Stage 2: Runtime
FROM python:3.12-slim AS runtime

WORKDIR /app

# Runtime dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy virtual environment
COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Copy application
COPY --from=builder /build /app

# Environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# Create non-root user
RUN useradd -m appuser
USER appuser

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:${PORT:-8000}/health || exit 1

# Expose port
EXPOSE ${PORT:-8000}

# Start application
CMD ["python", "-m", "app"]
```

2. DOCKER COMPOSE TEMPLATE:
```yaml
version: '3.8'

services:
  app:
    build:
      context: .
      dockerfile: Dockerfile
      args:
        - BUILD_ENV=${BUILD_ENV:-production}
    environment:
      - PORT=${PORT:-8000}
      - DATABASE_URL=${DATABASE_URL:-postgresql://postgres:postgres@db:5432/postgres}
    ports:
      - "${PORT:-8000}:${PORT:-8000}"
    depends_on:
      db:
        condition: service_healthy
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:${PORT:-8000}/health"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 10s
    restart: unless-stopped
    networks:
      - app_network
    volumes:
      - app_data:/app/data

  db:
    image: postgres:15-alpine
    environment:
      - POSTGRES_USER=${POSTGRES_USER:-postgres}
      - POSTGRES_PASSWORD=${POSTGRES_PASSWORD:-postgres}
      - POSTGRES_DB=${POSTGRES_DB:-postgres}
    volumes:
      - postgres_data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 5s
      timeout: 5s
      retries: 5
    networks:
      - app_network
    restart: unless-stopped

networks:
  app_network:
    driver: bridge

volumes:
  app_data:
  postgres_data:
```

YOU MUST ADAPT THESE TEMPLATES TO THE SPECIFIC PROJECT REQUIREMENTS, ADDING OR REMOVING SERVICES AS NEEDED.
</template-examples> 