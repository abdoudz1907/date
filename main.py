from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from datetime import datetime

TOKEN = "7641786261:AAGa8qPUTZS1rz6LN1nNorkQi1dC_g33rXw"

async def date_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    today = datetime.now().strftime("%Y-%m-%d")
    await update.message.reply_text(f"📅 تاريخ اليوم هو: {today}")

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("date", date_command))
    app.run_polling()

if __name__ == '__main__':
    main()
