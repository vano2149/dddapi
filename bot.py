"""
bot.py file!
"""

import asyncio
import telegram

async def main():
    bot = telegram.Bot("2117384417:AAGXVb3q9DDE_3YuxpW3gQ9U07_PyHrzLbs")
    async with bot:
        print(await bot.get_me())


if __name__ == "__main__":
    asyncio.run(main())