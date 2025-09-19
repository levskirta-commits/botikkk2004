#!/usr/bin/python

# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.
#!/usr/bin/python
import asyncio
from src import handlers # NoQa
from src.common import bot
from src.dao.models import Base, async_engine

async def init_db():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
if __name__ == '__main__':
    asyncio.run(init_db())
    asyncio.run(bot.polling())