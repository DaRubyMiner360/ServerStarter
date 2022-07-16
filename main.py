import os
import sys
from keep_alive import keep_alive
import discord
from discord.ext import commands

if len(sys.argv) == 1:
    print("No arguments provided!")
    exit(1)

bot = commands.Bot(
	command_prefix=commands.when_mentioned_or("?"),
	case_insensitive=True,
    intents=discord.Intents.all()
)

bot.author_id = 595353331468075018

@bot.event 
async def on_ready():
    print("I'm in")
    print(bot.user)

@bot.event
async def setup_hook():
    if __name__ == '__main__':
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                await bot.load_extension(f'cogs.{filename[: -3]}')

keep_alive()
token = os.environ.get("DISCORD_BOT_SECRET") 
bot.run(token)