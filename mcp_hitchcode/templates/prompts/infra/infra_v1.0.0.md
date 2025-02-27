---
version: 1.0.0
created: 2025-02-27
description: Template for laying out system infrastructure and tool stack information
variables:
  - infrastructure_info: Description of the infrastructure and tool stack
  - specific_instructions: Optional specific instructions to include in the prompt
---

Infrastructure Information: {{ infrastructure_info }}

<your-task>
Based on the provided infrastructure information, create a comprehensive and structured documentation of the system infrastructure and tool stack. This should serve as a reference for all team members and ensure consistent understanding of the development environment.
</your-task>

<your-documentation-structure>
Please organize the infrastructure documentation in the following sections:

1. **System Language and Runtime**
   - Programming language(s) and version(s)
   - Runtime environment details
   - Key language-specific configurations

2. **Dependency Management**
   - Package manager(s) used
   - Dependency resolution strategy
   - Version pinning approach

3. **Development Environment**
   - Required development tools
   - IDE recommendations and configurations
   - Local environment setup instructions

4. **Testing Framework**
   - Testing libraries and frameworks
   - Test runners and execution environment
   - Testing patterns and conventions

5. **Database and Data Storage**
   - Database systems and versions
   - ORM/data access layers
   - Migration and schema management

6. **API and Service Integration**
   - API frameworks and patterns
   - External service integrations
   - Authentication and authorization mechanisms

7. **Deployment Infrastructure**
   - Hosting environment
   - Containerization and orchestration
   - CI/CD pipeline details

8. **Monitoring and Observability**
   - Logging infrastructure
   - Metrics collection
   - Error tracking and reporting

9. **Security Considerations**
   - Security tools and practices
   - Compliance requirements
   - Vulnerability management approach
</your-documentation-structure>

<your-maxim-of-action>
1. Be comprehensive but concise - include all relevant details without unnecessary verbosity.

2. Prioritize clarity and accessibility - the documentation should be understandable by all team members regardless of their familiarity with the stack.

3. Include specific versions and configuration details where applicable to ensure reproducibility.

4. Highlight any non-standard or custom configurations that differ from typical defaults.

5. Document known limitations, workarounds, or areas that require special attention.
</your-maxim-of-action>

{% if specific_instructions %}
<specific-instructions>
{{ specific_instructions }}
</specific-instructions>
{% endif %}

THIS IS THE ACTUAL PROMPT FOR GUIDING YOUR NEXT STEPS. 