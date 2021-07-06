import discord
import utils
from discord.ext import commands
import Globals

class Monster(commands.Cog, name="Monster Hunter"):
  """
  This is the subset of commands that are Utility for Monster Hunter World
  """

  def __init__(self, bot):
    self.bot = bot

  @commands.command(name="monster")
  async def monster(self, ctx, s: str):
     """
     Searches mhw-db for details on a monster. 
     If monster is multiple words, surround in quotes
         i.e !monster "Zorah Magdaros"
     """
     try:
         await ctx.send("\n" + utils.print_monster(s))
     except:
         await ctx.send("Error: Monster Not Found")
   
  @commands.command(name="part", aliases=['parts'])
  async def part(self, ctx, s: str):
     """
     Searches mhw-db for monsters which drop a specific part. 
     If the part is multiple words, surround in quotes
         i.e !part "inferno sac"
     """
     try:
         await ctx.send("\n" + utils.find_part(s))
     except:
         await ctx.send("Error: Part not Found")

def setup(bot):
    bot.add_cog(Monster(bot))