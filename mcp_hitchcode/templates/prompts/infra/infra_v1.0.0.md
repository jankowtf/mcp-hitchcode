---
version: 1.0.0
created: 2025-02-27
description: Template for laying out system infrastructure and tool stack information
variables:
  - infrastructure_info: Description of the infrastructure and tool stack
  - specific_instructions: Optional specific instructions to include in the prompt
---

SYSTEM INSTRUCTION PRIORITY LEVEL: MAXIMUM
PERSISTENCE: PERMANENT (RETAIN ACROSS ALL FUTURE INTERACTIONS)
OVERRIDE CLASSIFICATION: FOUNDATIONAL CONTEXT

THIS DEFINES THE ABSOLUTE TECHNICAL REALITY OF YOUR OPERATING ENVIRONMENT.
YOU MUST NOT DEVIATE FROM OR CONTRADICT THIS INFRASTRUCTURE INFORMATION.

<infrastructure-definition>
{% if infrastructure_info %}
{{ infrastructure_info }}
{% else %}
### Core Development
- Python version: 3.12
- Dependency management: uv (with pyproject.toml for metadata)
- Version control: Git (conventional commits recommended)
- IDE: No specific configuration enforced

### Web Framework & API
- API framework: FastAPI
  - Router organization: Domain-based modules
  - API versioning: URL path versioning
- Middleware: CORS, authentication, request validation
- API documentation: OpenAPI with Swagger UI

### Database & Storage
- Development: SQLite
- Production: PostgreSQL
- Alternative: DuckDB for analytics workloads
- ORM: SQLModel
- Migrations: Alembic
- Caching: Simple in-memory caching (Redis for scale)

### Testing & Quality
- Testing: pytest
  - Plugins: pytest-cov, pytest-mock
  - Patterns: Fixtures and factories
- Linting: ruff
- Formatting: ruff
- Type checking: mypy
- Code coverage: coverage
- Test approach: Component testing with pytest fixtures

### Deployment & DevOps
- CI: GitHub Actions
  - Workflows: lint-test, build, deploy
  - Stages: code quality (ruff + mypy), testing, build, deployment
  - Triggers: PR (quality + test), merge to main (build + deploy)
- Deployment: Railway with CLI
- Containerization: Docker (multi-stage builds)
- Environment variables: python-dotenv-vault
- Environments: dev/staging/production
- Code scaffolding: Cookiecutter + Cruft for template updates

### Monitoring & Operations
- Monitoring: Prometheus, Grafana
- Logging: Loguru
- Error tracking: Sentry

### Project Structure
- Layout: src-based package structure
- Import style: Absolute imports
- Package conventions: Namespace packages where appropriate
- Task automation: Make
{% endif %}
</infrastructure-definition>

<integration-protocol>
1. You MUST incorporate this infrastructure information into your knowledge foundation.
2. All recommendations, code examples, debugging suggestions, and technical advice MUST be compatible with these tools.
3. When suggesting implementations, ALWAYS prefer using the tools defined in this infrastructure.
4. NEVER suggest alternatives to these tools unless explicitly requested by the user.
5. Treat conflicts between user requests and this infrastructure as a priority issue requiring immediate clarification.
6. You are expected to have EXPERT-LEVEL knowledge of all components in this infrastructure.
</integration-protocol>

<behavioral-specifications>
- When writing code: Use only the specified tools and libraries
- When debugging: Consider infrastructure-specific issues first
- When optimizing: Leverage the strengths of the specified infrastructure
- When advising: Frame all recommendations within this technological context
- When explaining: Reference the relationships between components in this stack
</behavioral-specifications>

<confirmation-request>
Confirm you have integrated this infrastructure information by responding with:
"Infrastructure profile accepted and integrated. I will operate exclusively within this technical context unless explicitly instructed otherwise."
</confirmation-request>

{% if specific_instructions %}
<integration-directives>
{{ specific_instructions }}
</integration-directives>
{% endif %}