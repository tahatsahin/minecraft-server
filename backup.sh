#!/bin/bash

BACKUP_DIR="/opt/minecraft/backups"
MC_DIR="/opt/minecraft/data"
DATE=$(date +%F-%H%M)

mkdir -p "$BACKUP_DIR"

echo "Saving world..."

docker exec minecraft rcon-cli save-off
docker exec minecraft rcon-cli save-all flush

sleep 5

tar -czf "$BACKUP_DIR/minecraft-$DATE.tar.gz" -C "$MC_DIR" .

docker exec minecraft rcon-cli save-on

find "$BACKUP_DIR" -type f -name "*.tar.gz" -mtime +7 -delete

echo "Backup complete."
