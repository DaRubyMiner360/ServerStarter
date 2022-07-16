import discord
from discord.ext import commands
import sys
import os

class ServerCommands(commands.Cog):
  def __init__(self, bot: commands.Bot) -> None:
    self.bot: commands.Bot = bot
  
  @commands.hybrid_command(name="start")
  async def start_command(self, ctx: commands.Context) -> None:
    await ctx.send("Starting server!")
    os.system(' '.join([str(e) for e in sys.argv[1:]]))
    
async def setup(bot: commands.Bot) -> None:
  await bot.add_cog(ServerCommands(bot))
