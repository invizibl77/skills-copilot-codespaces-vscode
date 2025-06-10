import os
import openai
from telegram.ext import Updater, MessageHandler, Filters

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

openai.api_key = OPENAI_API_KEY


def handle_message(update, context):
    user_text = update.message.text
    try:
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_text}],
        )
        reply = completion.choices[0].message["content"].strip()
    except Exception as e:
        reply = f"Ошибка: {e}"
    update.message.reply_text(reply)


def main():
    if not TELEGRAM_TOKEN or not OPENAI_API_KEY:
        raise RuntimeError("Не заданы переменные TELEGRAM_TOKEN и OPENAI_API_KEY")
    updater = Updater(TELEGRAM_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
