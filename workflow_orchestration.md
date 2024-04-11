This `docker-compose.yml` file defines two services:

1. `magic`:
   - Uses the Docker image `mageai/mageai:latest`.
   - Runs the command `mage start ${PROJECT_NAME}` inside the container.
   - Loads environment variables from the `.env` file.
   - Builds the container using the `Dockerfile` in the current context.
   - Sets various environment variables for the container.
   - Maps port `6789` of the host to port `6789` of the container.
   - Mounts the current directory (`.`) to `/home/src/` in the container, and mounts a specific JSON file (`personal-gcp.json`) to `/home/src/personal-gcp.json`.
   - Restarts the container automatically if it fails, up to 5 times (`on-failure:5`).

2. `postgres`:
   - Uses the Docker image `postgres:14`.
   - Restarts the container automatically if it fails.
   - Sets the container name to `${PROJECT_NAME}-postgres`.
   - Loads environment variables from the `.env` file.
   - Sets environment variables for PostgreSQL database configuration.
   - Maps port `${POSTGRES_PORT}` of the host to port `5432` of the container.

This configuration allows you to define and run a multi-container application consisting of a `magic` service and a `postgres` service using Docker Compose.
