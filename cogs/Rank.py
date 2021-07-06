import discord
from discord.ext import commands

class Rank(commands.Cog, name="Rank"):
  """
  This is the subset of commands for returning player ranks from various apis
  """
  def __init__(self, bot):
    self.bot = bot

  

def setup(bot):
    bot.add_cog(Monster(bot))