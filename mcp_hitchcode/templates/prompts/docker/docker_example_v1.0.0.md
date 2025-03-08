---
version: 1.0.0
created: 2025-03-08
description: Example template demonstrating Docker file loading
variables:
  - docker_file_path: Path to the Dockerfile to include
  - docker_compose_path: Path to the docker-compose.yml file to include
changelog:
  - Initial version of Docker example template
---

# Docker Configuration Example

## Dockerfile

```dockerfile
{{ docker_file(docker_file_path) }}
```

## Docker Compose

```yaml
{{ docker_compose(docker_compose_path) }}
```

## Usage Instructions

The above Docker configurations can be used to set up a containerized environment for your application.

To build and run the containers:

```bash
docker-compose up -d
```

To stop the containers:

```bash
docker-compose down
``` 