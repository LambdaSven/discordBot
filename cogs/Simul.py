import discord
from discord.ext import commands
import utils
import Globals
simul = {}

class Simul(commands.Cog, name="Simul"):
  """
  This is the subset of commands to control Simuls
  """
  def __init__(self, bot):
      self.bot = bot

  @commands.command(name="players")
  async def players(self, ctx):
      """
      View all players currently in queue for a simul invite
      """
      s = "Currently in simul are: "
      for x in simul.keys():
          u = await self.bot.fetch_user(x)
          s += "\n\t" + u.display_name
      await ctx.send(s)

  @commands.command(name="join")
  async def join(self, ctx):
      """
      Join the queue to be in a simul
      """
      if ctx.message.author.id not in simul:
          simul[ctx.message.author.id] = "" 
          s = ctx.message.author.display_name + " has joined the simul\n Currently signed up are: "
          for x in simul.keys():
              u = await self.bot.fetch_user(x) 
              s += "\n\t" + u.display_name
          await ctx.send(s)
      else:
          await ctx.send(ctx.message.author.display_name + " is already in the simul")

  @commands.command(name="leave")
  async def leave(self, ctx):
      """
      Leave the queue for the simul
      """
      e = ctx.message.author.id
      if e in simul:
          simul.pop(e)
          s = ctx.message.author.display_name + " has been removed from the simul\n Currently signed up are: "
          for x in simul.keys():
              u = await self.bot.fetch_user(x)
              s += "\n\t" + u.display_name
          await ctx.send(s)
      else:
          await ctx.send(ctx.message.author.display_name + "Is not currently in the simul") 

  @commands.command(name="start")
  async def start(self, ctx):
      """
      Start the simul. 

      Invites will be sent out to all registered players, as well as the player who sent the command

      Can only be started by a player not registered to play
      """
      u = await self.bot.fetch_user(ctx.message.author.id)
      if ctx.message.author.id in simul.keys():
          await ctx.send("You are currently registered as a player.")
          return
      for x in simul.keys():
          l = utils.make_lichess_link()
          d = await self.bot.fetch_user(x)
          await u.send(d.display_name + ":" + l)
          await d.send(l)
      simul.clear()

  @commands.command(name="clear", hidden=True)
  async def clear(self, ctx):
      """
      Clears all players from the simul queue - only usable by admin
      """
      if users[ctx.message.author.id] in Globals.root:
          simul.clear()
          await ctx.send("Cleared Simul")
      else:
          await ctx.send("You are not authorized to use this command")   

def setup(bot):
    bot.add_cog(Simul(bot))