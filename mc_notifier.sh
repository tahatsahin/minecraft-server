#!/bin/bash

LOG_FILE="/opt/minecraft/data/logs/latest.log"
source /opt/minecraft/.env

tail -F "$LOG_FILE" | while read -r line; do
        if [[ "$line" == *"joined the game"* ]]; then
                PLAYER_NAME=$(echo "$line" | awk -F' ' '{print $4}' | awk '{print $1}')

                echo "$PLAYER_NAME just joined."
                curl -s \
                  -X POST "https://api.telegram.org/bot${TOKEN}/sendMessage" \
                  -H "Content-Type: application/json" \
                  -d "$(printf '{"chat_id":"%s","text":"!!! ALERT !!!\n%s just joined!"}' \
                      "$USER_CHAT" "$PLAYER_NAME")"
        fi
done