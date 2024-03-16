# 12 Factor App Checklist

When deploying an application or microservice we advocate the [12-factor](https://12factor.net/) application pattern because it results in applications perfectly designed to run on Kubernetes.

Applications that adhere to these characteristics will make best use of the High Availability and Scaling features Kubernetes has to offer. [12-factor](https://12factor.net/) applications are suitable for deployments that can leverage applications HorizontalPodAutoscaler functionality.

The actionable recommendations listed below leverage “real world” experience of deploying applications and microservices to kubernetes.

## Codebase

- One-repo-per-service (poly-repo) architectures (preferred, not required)
- Use a Git-based workflow with [pull requests](https://docs.github.com/en/github/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests) & approval process
- Dockerized with a `Dockerfile`
- Automated tests exist to validate application works

## Dependencies

- Service dependencies are explicitly declared in the configuration (e.g. `DB_HOST`)
- Services are loosely coupled so that they can be started in any order
- Application dependencies are explicitly pinned in manifests (E.g. `package.json`);
- Use [Semantic Versioning](https://semver.org/) rather than commit SHAs for pinning, where possible

## Config

- All configuration settings are passed via environment variables and not hardcoded.
- Services can be dynamically reconfigured without recompilation (e.g. by changing settings)
- Use DNS-based service discovery (instead of IPs or depend on `consul`); use short-dns names with search domains rather than FQHN
- Use Azure SDK's DefaultAzureCredential for automatic Azure configuration (E.g. do not validate `AZURE_TENANT_ID`, `AZURE_CLIENT_ID`, and `AZURE_CLIENT_SECRET` variables are configured)

## Backing Services

- Use object storage where files are needed (not local storage)
- Use external databases (e.g. Postgres, MySQL, Redis, etc) to persist state
- Use environment variables for configuration (e.g. timeouts, endpoints, etc)
- Use configurable timeouts on connections, responses from backends

## Build, Release, Run

- Well-defined process to build (e.g. compile) the application and start it (e.g. a `Makefile`)
- `Dockerfile` defines `ENTRYPOINT` to run the application
- Docker composition (`docker-compose.yml`) can bring up the environment for automated testing
- Cut releases on merge to master (preferred, not required); use [Semantic Versioning](https://semver.org/)

## Processes

- All processes must expose health check endpoints (`/health`)
- Should not depend on a process manager (e.g. `pm2`)
- Should exit non-zero upon fatal errors
- Must respond to `SIGTERM` and exit gracefully
- Health checks should not depend on the health of the backing services
- Does not require privileged execution (e.g. `root`)

## Port binding

- `Dockerfiles` define a `PORT` definition
- Services should listen on a preconfigured bind-address and port (e.g. `0.0.0.0:8000`)
- Should listen on [non-privileged](https://www.w3.org/Daemon/User/Installation/PrivilegedPorts.html) ports  (`> 1024`)

## Concurrency

- Application can be run any number of times in parallel (e.g. no expectation of locking)
- Application does not maintain a large pool of persistent database connections (e.g. configurable pool size)
- Application uses database transactions, if applicable; avoids deadlocks
- Application does not depend on sticky sessions; requests can hit any process

## Disposability

- Should be entirely stateless (e.g. not maintain any local state, all state offloaded to backing services)
- Processes can be easily created or destroyed without any orchestrated shutdown process
- No `POSIX` filesystem required for persistence (local caching/buffering okay)

## Environment Parity

- All environments function the same way when configured with the same settings
- Flags should enable/disable functionality without knowledge of stage or environment (e.g. do not use if `($environment == 'dev') { ... }`)
- Do not use hostnames for conditional/routing logic (use Ingress)

## Logs

- Logs are emitted to `stdout`
- Events are structured event streams (e.g. JSON)
- Do not write logs to disk (to mitigate the need for log rotation)

## Admin processes

- Database migrations should be automated and run as a separate container
- Cronjobs can be run as a separate container
- Batch processing should run as a separate container
