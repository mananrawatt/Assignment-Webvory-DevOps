# Deployment Guide

## Prerequisites

* Docker
* Docker Compose

## Clone Repository

git clone <repository-url>

cd ai-backend-assignment

## Configure Environment Variables

Update the .env file as required.

## Start Application

docker compose up -d --build

## Verify Containers

docker ps

## Verify Application

Health Check:

http://localhost:8081/health

Database Check:

http://localhost:8081/db-test

Redis Check:

http://localhost:8081/redis-test

## Logging

Application Logs:

docker logs fastapi-app

NGINX Logs:

docker exec -it nginx-proxy cat /var/log/nginx/access.log

## Backup

Run:

./scripts/backup.sh

## Production Deployment Approach

For a production VPS:

1. Install Docker and Docker Compose
2. Clone repository
3. Configure environment variables
4. Execute:

docker compose up -d --build

## SSL Strategy

If a domain is available, Let's Encrypt certificates can be configured through NGINX for HTTPS.

## CI/CD

GitHub Actions automatically:

* Builds Docker images
* Validates Docker Compose configuration
* Starts containers
* Performs health checks

The workflow can be extended to deploy to a VPS through SSH-based deployment.
