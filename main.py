
import os
import asyncio
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "أهلاً بك في QUREO Assistant 🤖\n"
        "أرسل سؤال البرمجة أو صورة التمرين وسأساعدك في فهمه وحله."
    )

async def question(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "وصل سؤالك بنجاح! 📚\n"
        "سيتم تجهيز مساعد تحليل الأسئلة في الخطوة القادمة."
    )

def main():
    token = os.environ.get("BOT_TOKEN")
    if not token:
        raise RuntimeError("BOT_TOKEN is missing")

    app = Application.builder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(
        filters.TEXT & ~filters.COMMAND, question
    ))

    asyncio.set_event_loop(asyncio.new_event_loop())
    app.run_polling()

if __name__ == "__main__":
    main()
