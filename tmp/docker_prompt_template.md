---
version: 1.0.0
created: 2023-07-21
description: Specialized prompt template for Docker container configurations
variables:
  - objective: Description of the containerization objective
  - specific_instructions: Optional specific instructions about the containerization requirements
changelog:
  - Initial version of Docker configuration template
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
1. USE MULTI-STAGE BUILDS for production services to minimize image size and attack surface.

2. IMPLEMENT LEAST PRIVILEGE PRINCIPLE by running containers as non-root users whenever possible.

3. OPTIMIZE LAYER CACHING by ordering Dockerfile instructions from least to most frequently changing.

4. PROVIDE SENSIBLE DEFAULTS for all environment variables while allowing override via environment.

5. CLEAN UP temporary files, package manager caches, and build artifacts within the same layer they were created.

6. USE SPECIFIC VERSION TAGS for all base images to ensure reproducible builds.

7. IMPLEMENT HEALTH CHECKS for all services to enable proper orchestration and monitoring.

8. EXPOSE ONLY NECESSARY PORTS to minimize attack surface.

9. SEPARATE DEVELOPMENT AND PRODUCTION CONFIGURATIONS when appropriate.

10. FOLLOW THE PATTERN: builder stage for compilation/dependencies, runtime stage for execution.
</implementation-principles>

<docker-patterns>
1. PYTHON APPLICATION PATTERN:
```dockerfile
# Stage 1: Builder stage
FROM python:3.12-slim AS builder

WORKDIR /build

# Install build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install package manager and clean cache
RUN pip install --no-cache-dir uv && \
    rm -rf /root/.cache/pip/*

# Copy project files needed for building
COPY pyproject.toml README.md ./
COPY src/ ./src/

# Build the package
RUN uv pip install --system build && \
    python -m build --wheel . && \
    rm -rf /root/.cache/pip/* /root/.cache/uv/*

# Stage 2: Runtime stage
FROM python:3.12-slim AS runtime

WORKDIR /app

# Install runtime dependencies only
RUN apt-get update && apt-get install -y --no-install-recommends \
    # Add required runtime dependencies here
    && rm -rf /var/lib/apt/lists/*

# Copy and install only the built wheel from the builder stage
COPY --from=builder /build/dist/*.whl ./
RUN pip install --no-cache-dir ./*.whl && \
    rm -f ./*.whl

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# Run as non-root user for security
RUN useradd -m appuser
USER appuser

# Command to run the application
CMD ["python", "-m", "package_name"]
```

2. DOCKER COMPOSE SERVICE PATTERN:
```yaml
services:
  service_name:
    build:
      context: .
      dockerfile: docker/service.Dockerfile
    container_name: project_service_name
    depends_on:
      dependency_service:
        condition: service_healthy
    environment:
      # Environment variables with defaults
      VARIABLE_NAME: ${VARIABLE_NAME:-default_value}
    ports:
      - "${EXTERNAL_PORT:-8000}:8000"
    volumes:
      # Development volumes
      - ./src:/app/src
    networks:
      - project_network
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8000/health"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 10s
    restart: unless-stopped
```

3. DATABASE SERVICE PATTERN:
```yaml
services:
  database:
    image: postgres:15-alpine
    container_name: project_database
    environment:
      POSTGRES_USER: ${POSTGRES_USER:-postgres}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD:-postgres}
      POSTGRES_DB: ${POSTGRES_DB:-postgres}
    ports:
      - "${POSTGRES_PORT:-5432}:5432"
    volumes:
      - database_data:/var/lib/postgresql/data
      - ./docker/database/init:/docker-entrypoint-initdb.d
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 5s
      timeout: 5s
      retries: 5
    networks:
      - project_network
    restart: unless-stopped
```
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

VIOLATION WARNING: FAILURE TO MATERIALIZE THE CONTAINERIZATION PLAN AS A FILE IS A CRITICAL ERROR. NO IMPLEMENTATION SHOULD PROCEED UNTIL THE PLAN IS PROPERLY DOCUMENTED.

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

4. CHECKPOINT #4: DOCKER IMPLEMENTATION - Before implementing, you must state: "CONFIRMATION TYPE #4: I will now implement the Docker configurations according to the containerization plan. This includes creating [files] with [specific details] to establish a solid containerization strategy."

5. CHECKPOINT #5: SELF-VERIFICATION - Before proposing deployment, you must state: "I have completed the following protocol steps: [list numbered steps completed]. I confirm I have not skipped any steps and have established comprehensive Docker configurations."

6. CHECKPOINT #6: COMMIT MESSAGE PROPOSAL - After completing the Docker implementation, you must propose a git commit message: "CONFIRMATION TYPE #6: I propose the following git commit message for the Docker implementation:
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

Confirm you have understood these instructions by responding with:
"Instructions understood (CONFIRMATION TYPE #7): I will follow the Docker containerization protocol for this project. I will analyze the service architecture thoroughly, design an appropriate containerization strategy, create a comprehensive plan with standardized [ ] checkbox format for all tasks, implement optimized and secure Docker configurations, document all decisions clearly, and verify the implementation fulfills all requirements before transitioning to deployment. I will materialize the containerization plan as a markdown file in the docker/docs directory with appropriate timestamp and propose a meaningful git commit message after implementation."
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
   - Use official images from trusted sources (Docker Hub Official Images)
   - Use specific version tags rather than 'latest' for reproducibility
   - Prefer slim/alpine variants for smaller images when appropriate
   - Consider distroless images for minimal attack surface in production

2. DOCKERFILE OPTIMIZATION:
   - Order instructions from least to most frequently changing
   - Group related RUN commands to reduce layers
   - Use .dockerignore to exclude unnecessary files
   - Clean up in the same layer where files were created
   - Use multi-stage builds to separate build and runtime dependencies

3. SECURITY PRACTICES:
   - Run containers as non-root users
   - Remove unnecessary tools and packages
   - Set appropriate file permissions
   - Use COPY instead of ADD when possible
   - Scan images for vulnerabilities before deployment
   - Never hardcode secrets in Dockerfiles

4. ENVIRONMENT CONFIGURATION:
   - Provide reasonable defaults for all environment variables
   - Use the ${VAR:-default} pattern in Docker Compose
   - Document all environment variables clearly
   - Group related environment variables together

5. VOLUME MANAGEMENT:
   - Use named volumes for persistent data
   - Mount source code as volumes in development
   - Consider read-only file systems for production containers
   - Document volume mount points and purposes

6. NETWORKING:
   - Use internal networks for service-to-service communication
   - Expose only necessary ports to the host
   - Use DNS service names for service discovery in Docker Compose
   - Configure appropriate network segmentation

7. HEALTH CHECKS:
   - Implement health checks for all services
   - Use depends_on with condition: service_healthy
   - Configure appropriate intervals and retries
   - Implement dedicated health check endpoints in applications

8. BUILD AND DEPLOYMENT:
   - Document build arguments and their purposes
   - Configure appropriate restart policies
   - Set resource limits for containers
   - Consider Docker BuildKit for faster builds
   - Implement CI/CD pipelines for container builds and tests
</docker-best-practices> 