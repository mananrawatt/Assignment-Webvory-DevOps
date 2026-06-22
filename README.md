# AI Backend Assignment

## Overview

This project demonstrates the deployment and productionization of a backend application using FastAPI, Docker, PostgreSQL, Redis, NGINX, and GitHub Actions.

The solution focuses on containerization, service orchestration, monitoring, health checks, security considerations, backup strategy, and CI/CD automation.

---

## Architecture

```text
                    GitHub
                       |
                       v
              GitHub Actions
             Build & Validation
                       |
                       v

+--------------------------------------------------+
|            Deployment Environment                |
|                                                  |
|     +------------------------+                   |
|     |         NGINX          |                   |
|     |     Reverse Proxy      |                   |
|     +-----------+------------+                   |
|                 |                                |
|                 v                                |
|     +------------------------+                   |
|     |        FastAPI         |                   |
|     |    Backend Service     |                   |
|     +-----+------------+-----+                   |
|           |            |                         |
|           |            |                         |
|           v            v                         |
|      +--------+   +----------+                   |
|      | Redis  |   |PostgreSQL|                  |
|      | Cache  |   | Database |                  |
|      +--------+   +----------+                  |
|                         |                        |
|                         v                        |
|                   Backup Script                  |
|                    SQL Dumps                     |
+--------------------------------------------------+
```

---

## Technology Stack

### Application Layer

* FastAPI
* Python 3.12

### Database Layer

* PostgreSQL 16

### Cache Layer

* Redis 7

### Reverse Proxy

* NGINX

### Containerization

* Docker
* Docker Compose

### CI/CD

* GitHub Actions

### Monitoring

* Prometheus Metrics Endpoint

---

## Features Implemented

### Dockerized Application

The FastAPI application is containerized using Docker and can be deployed consistently across environments.

### Docker Compose Orchestration

The following services are orchestrated through Docker Compose:

* FastAPI
* PostgreSQL
* Redis
* NGINX

### NGINX Reverse Proxy

NGINX acts as the public-facing entry point and forwards requests to the FastAPI application.

### Environment Variables

Application configuration is managed through a `.env` file.

### Health Checks

Implemented endpoints:

* `/health`
* `/db-test`
* `/redis-test`

Enhanced health validation includes:

* Application status
* PostgreSQL connectivity
* Redis connectivity

### Logging

Application logs are generated using Python logging.

View logs:

```bash
docker logs fastapi-app
```

### Monitoring

Prometheus metrics are exposed through:

```text
/metrics
```

Metrics can be scraped by Prometheus and visualized using Grafana.

### AI / LLM Readiness

Implemented:

```text
/ai-health
```

The architecture is designed to support:

* Ollama
* OpenAI APIs
* Llama Models
* Hugging Face Models

without requiring infrastructure changes.

### Backup Strategy

Backup script:

```bash
./scripts/backup.sh
```

Features:

* PostgreSQL SQL dumps
* Timestamp-based backup naming
* Backup retention support

### Restart Strategy

All services use:

```yaml
restart: unless-stopped
```

This ensures automatic recovery after:

* Host reboot
* Docker restart
* Container failure

---

## API Endpoints

### Root Endpoint

```http
GET /
```

### Health Check

```http
GET /health
```

### Database Validation

```http
GET /db-test
```

### Redis Validation

```http
GET /redis-test
```

### Monitoring Metrics

```http
GET /metrics
```

### AI Health Endpoint

```http
GET /ai-health
```

---

## Running the Project

### Clone Repository

```bash
git clone <repository-url>

cd ai-backend-assignment
```

### Start Application

```bash
docker compose up -d --build
```

### Verify Containers

```bash
docker ps
```

### Verify Endpoints

```text
http://localhost:8081/
http://localhost:8081/health
http://localhost:8081/db-test
http://localhost:8081/redis-test
http://localhost:8081/metrics
http://localhost:8081/ai-health
```

---

## CI/CD Pipeline

GitHub Actions automatically performs:

* Source Checkout
* Docker Image Build
* Docker Compose Validation
* Application Startup Validation
* Health Check Verification

Workflow file:

```text
.github/workflows/deploy.yml
```

---

## Security Considerations

Implemented:

* Environment variable management
* Internal Docker networking
* Reverse proxy architecture
* Container restart policies

Production Recommendations:

* UFW Firewall
* Fail2Ban
* HTTPS using Let's Encrypt
* Secret Management Solutions

---

## SSL Strategy

Since a public domain was not available, SSL was not configured directly.

Production approach:

* Let's Encrypt Certificates
* NGINX SSL Termination
* Automatic Certificate Renewal

---

## Deployment Approach

The application is deployed locally using Docker Compose.

The same architecture can be deployed to:

* AWS EC2
* Azure VM
* Google Compute Engine
* DigitalOcean Droplets
* Any Linux VPS

with minimal changes.

---

## Bonus Features

### Implemented

* Prometheus Metrics Endpoint
* AI Health Endpoint
* Automated Database Backups
* Enhanced Health Checks
* Container Restart Policies

### Production Enhancements

* Grafana Dashboards
* Prometheus Monitoring Stack
* Cloudflare Integration
* Zero-Downtime Deployments
* Automated VPS Deployments
* Distributed Tracing

---

## Assignment Requirement Mapping

| Requirement                | Status |
| -------------------------- | ------ |
| Dockerized Application     | ✅      |
| Docker Compose             | ✅      |
| FastAPI Service            | ✅      |
| PostgreSQL                 | ✅      |
| Redis                      | ✅      |
| NGINX Reverse Proxy        | ✅      |
| Environment Variables      | ✅      |
| Health Endpoint            | ✅      |
| Logging Strategy           | ✅      |
| Backup Strategy            | ✅      |
| CI/CD Pipeline             | ✅      |
| Deployment Documentation   | ✅      |
| Architecture Diagram       | ✅      |
| SSL Approach Documentation | ✅      |
| Monitoring Implementation  | ✅      |
| AI/LLM Readiness           | ✅      |

---

## Author

Manan Rawat
DevOps Engineer
