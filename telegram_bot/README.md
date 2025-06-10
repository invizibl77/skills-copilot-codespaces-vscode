# Telegram GPT-бот

Простой пример бота для Telegram, который пересылает сообщения в модель GPT-3.5 и отправляет ответ пользователю.

## Требования
- Python 3.8+
- Библиотеки `python-telegram-bot` и `openai`

## Установка
```bash
pip install python-telegram-bot openai
```

## Переменные окружения
Создайте две переменные окружения:
- `TELEGRAM_TOKEN` — токен вашего бота, полученный у `@BotFather`.
- `OPENAI_API_KEY` — API-ключ OpenAI.

## Запуск
```bash
python bot.py
```

Бот начнёт опрашивать Telegram и отвечать на входящие текстовые сообщения.
