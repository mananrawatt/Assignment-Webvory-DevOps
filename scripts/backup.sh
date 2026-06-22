#!/bin/bash

BACKUP_DIR=./backups

mkdir -p $BACKUP_DIR

TIMESTAMP=$(date +"%Y-%m-%d_%H-%M-%S")

docker exec postgres-db pg_dump -U postgres appdb > $BACKUP_DIR/postgres_$TIMESTAMP.sql

echo "Backup completed: postgres_$TIMESTAMP.sql"