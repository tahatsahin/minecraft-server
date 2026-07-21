import subprocess
import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Configuration
load_dotenv()
TOKEN = os.getenv("TOKEN")
ALLOWED_USER_ID = int(os.getenv("USER_CHAT"))

async def list_players(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Sec Check
    if update.effective_user.id != ALLOWED_USER_ID:
        await update.message.reply_text("Unauthorized access.")
        return

    try:
        result = subprocess.run(
                ["docker", "exec", "minecraft", "rcon-cli", "list"],
                capture_output=True,
                text=True,
                check=True
                )

        output = result.stdout.strip() if result.stdout else "No output."
        await update.message.reply_text(f" **ServerStatus: **\n`{output}`", parse_mode="Markdown")

    except subprocess.CalledProcessError as e:
        error_msg = e.stderr.strip() if e.stderr else str(e)
        await update.message.reply_text("Error executing command.")
    except Exception as e:
        await update.message.reply_text("Unexpected error.")
        
async def server_status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ALLOWED_USER_ID:
        await update.message.reply_text("Unauthorized access.")
        return
    
    try:
        result = subprocess.run(
                ["docker", "compose", "ps"],
                capture_output=True,
                text=True,
                check=True
                )
        output = result.stdout.strip() if result.stdout else "No output."
        await update.message.reply_text(f" **Docker: **\n`{output}`", parse_mode="Markdown")
        
    except subprocess.CalledProcessError as e:
        error_msg = e.stderr.strip() if e.stderr else str(e)
        await update.message.reply_text("Error executing command.")
    except Exception as e:
        await update.message.reply_text("Unexpected error.")
    
        
async def restart_server(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ALLOWED_USER_ID:
        await update.message.reply_text("Unauthorized access.")
        return
    
    try:
        result = subprocess.run(
                ["docker", "compose", "restart", "mc"],
                capture_output=True,
                text=True,
                check=True
                )
        output = result.stdout.strip() if result.stdout else "No output."
        await update.message.reply_text(f" **Docker: **\n`{output}`", parse_mode="Markdown")
        
    except subprocess.CalledProcessError as e:
        error_msg = e.stderr.strip() if e.stderr else str(e)
        await update.message.reply_text("Error executing command.")
    except Exception as e:
        await update.message.reply_text("Unexpected error.")
    
async def close_server(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ALLOWED_USER_ID:
        await update.message.reply_text("Unauthorized access.")
        return
    
    try:
        result = subprocess.run(
                ["docker", "compose", "down", "mc"],
                capture_output=True,
                text=True,
                check=True
                )
        output = result.stdout.strip() if result.stdout else "No output."
        await update.message.reply_text(f" **Docker: **\n`{output}`", parse_mode="Markdown")
        
    except subprocess.CalledProcessError as e:
        error_msg = e.stderr.strip() if e.stderr else str(e)
        await update.message.reply_text("Error executing command.")
    except Exception as e:
        await update.message.reply_text("Unexpected error.")
    
async def open_server(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ALLOWED_USER_ID:
        await update.message.reply_text("Unauthorized access.")
        return
    
    try:
        result = subprocess.run(
                ["docker", "compose", "up", "mc", "-d"],
                capture_output=True,
                text=True,
                check=True
                )
        output = result.stdout.strip() if result.stdout else "No output."
        await update.message.reply_text(f" **Docker: **\n`{output}`", parse_mode="Markdown")
        
    except subprocess.CalledProcessError as e:
        error_msg = e.stderr.strip() if e.stderr else str(e)
        await update.message.reply_text("Error executing command.")
    except Exception as e:
        await update.message.reply_text("Unexpected error.")

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("online", list_players))
    app.add_handler(CommandHandler("status", server_status))
    app.add_handler(CommandHandler("restart", restart_server))
    app.add_handler(CommandHandler("down", close_server))
    app.add_handler(CommandHandler("up", open_server))
    
    print("Bot is polling.")
    app.run_polling()

if __name__ == "__main__":
    main()