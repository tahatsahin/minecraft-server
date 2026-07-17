# Minecraft Server Utility Scripts

This repository contains several utility scripts used to monitor and maintain the Minecraft server.

## Requirements

* Python 3
* Bash
* Cron
* `nohup`

Make sure all scripts have the correct permissions before running them:

```bash
chmod +x /opt/minecraft/mc_notifier.sh
chmod +x /opt/minecraft/backup.sh
```

---

## Start the Online Status Service

Runs the Python service in the background:

```bash
nohup python3 mc_online.py > /dev/null 2>&1 &
```

---

## Start the Join Notification Service

Runs the Minecraft join notifier in the background:

```bash
nohup /bin/bash /opt/minecraft/mc_notifier.sh > /dev/null 2>&1 &
```

This script monitors the Minecraft server log and sends Telegram notifications whenever a player joins the server.

---

## Configure Automatic Nightly Backups

Edit the user's crontab:

```bash
crontab -e
```

Add the following line to execute the backup script every day at **03:00**:

```cron
0 3 * * * /opt/minecraft/backup.sh >> /var/log/minecraft-backup.log 2>&1
```

The backup log will be written to:

```text
/var/log/minecraft-backup.log
```

---

## Verify Running Processes

To verify that the background services are running:

```bash
ps aux | grep mc_online.py
ps aux | grep mc_notifier.sh
```

---

## Stop the Services

Locate the process IDs:

```bash
ps aux | grep mc_online.py
ps aux | grep mc_notifier.sh
```

Terminate them using:

```bash
kill <PID>
```

Or, to stop all matching processes:

```bash
pkill -f mc_online.py
pkill -f mc_notifier.sh
```
