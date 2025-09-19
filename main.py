import asyncio
import os

from telebot.async_telebot import AsyncTeleBot

bot = AsyncTeleBot(os.environ["BOTIKKK2004_TELEGRAM_TOKEN"])


@bot.message_handler(commands=['help', 'start'])
async def send_welcome(message):
    text = 'Привет, я botikkk2004.\nПросто напишите мне что-нибудь, и я повторю это!'
    await bot.reply_to(message, text)


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
async def echo_message(message):
    await bot.reply_to(message, message.text)

if __name__ == '__main__':
    asyncio.run(bot.polling())
