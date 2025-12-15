import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_NAME = "SMOKELAB SYSTEM"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Салют. Я SMOKELAB SYSTEM ☁️🔥\n\n"
        "Твой виртуальный помощник в кальянных делах.\n"
        "Запара — она в голове. Погнали."
    )

def main():
    token = os.getenv("BOT_TOKEN")
    if not token:
        raise RuntimeError("BOT_TOKEN not found")

    app = ApplicationBuilder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == "__main__":
    main()
