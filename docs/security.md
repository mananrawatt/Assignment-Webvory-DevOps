# Security Measures

## Environment Variables

Sensitive configuration values are stored using environment variables through the `.env` file and are not hardcoded in the application source code.

## Docker Network Isolation

PostgreSQL and Redis are deployed within an internal Docker network and are not exposed publicly.

## NGINX Reverse Proxy

NGINX acts as the public entry point and forwards requests to the FastAPI application. Backend services remain inaccessible from the internet.

## Restart Policies

All containers use:

restart: unless-stopped

to automatically recover from crashes and host reboots.

## Firewall (Production Recommendation)

Only the following ports should be exposed:

* 22 (SSH)
* 80 (HTTP)
* 443 (HTTPS)

Example:

ufw allow 22
ufw allow 80
ufw allow 443

## Fail2Ban (Production Recommendation)

Fail2Ban should be configured to protect SSH access from brute-force attacks.

## SSL/TLS

HTTPS should be enabled using Let's Encrypt certificates managed by NGINX.
