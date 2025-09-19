#!/usr/bin/python

# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.
#!/usr/bin/python
import asyncio
from src import handlers # NoQa
from src.common import bot

if __name__ == '__main__':
    asyncio.run(bot.polling())