import discord
from discord.ext import commands
from discord.ext import tasks
import utils
import requests
import json
import re
import Globals
import time
from datetime import datetime
import pytz

class Misc(commands.Cog):
    """
    Various Misc commands
    """
    def __init__(self, bot):
      self.bot = bot
      # self.sync.start()
    
    # @tasks.loop(seconds=1)
    # async def sync(self):
    #   t = datetime.now(pytz.timezone("America/New_York"))
    #   print(t.second)
    #   if(t.second == 0):
    #     self.clock.start()
    #     self.sync.stop()
    

    # @tasks.loop(seconds=60)
    # async def clock(self):
    #   t = datetime.now(pytz.timezone('America/New_York'))
    #   if(t.minute == 0):
    #     voice = self.bot.get_channel(132682549297152001)
    #     vc = await voice.connect()
    #     for x in range(0, (t.hour%12)):
    #       vc.play(discord.PCMVolumeTransformer(discord.FFmpegPCMAudio("data/bonk.mp3"), volume=1.0))
    #       while vc.is_playing():
    #         time.sleep(.1)
    #     await vc.disconnect()

    @commands.command(name="status")
    async def status(self, ctx, *args):
      """
      Change the bot's \"Playing\" status
      """
      game = discord.Game(' '.join(tuple(map(str, args))))
      await self.bot.change_presence(activity=game)


    #Create a open challenge with lichess' api
    @commands.command(name="chess")
    async def chess(self, ctx, a: int=15, b: int=10, c: str="standard"):
        """
        Creates an open challenge on lichess.org 
  
        Params are the time, and the variant, as follows
            {p1} = initial time in minutes
            {p2} = time of increment
            {p3} = game mode
  
        Parameters are optional, but will be read in order
        If one is missing the default will be used.
            (i.e !chess 10 will start a 10+10 standard game)
        """
        url = "https://lichess.org/api/challenge/open"
        #clock.limit is seconds, so I convert (allowing input by minutes), then we use
        #awkward ternaries for safety
        params = {'clock.limit': a*60, 'clock.increment': b , 'variant': c}
        resp = requests.post(url, params)
        print("Making request to lichess in chess")
        #we only want to print link if valid request
        if resp.status_code == 200:
            dict = resp.json()
            #print(dict)
            await ctx.send(dict["challenge"]["url"])    
        else:
            s = ": "
            for x in resp.json()["error"]:
                s += x + " is invalid, "
            await ctx.send("err " + str(resp.status_code) + s)
    
    #print a random name to the chat
    @commands.command(name="name")
    async def name(self, ctx):
        """
        Generates a name from the names stored on the server.
        """
        await ctx.send(utils.generate_name())
    #add a first name to the file
    @commands.command(name="addfirst")
    async def addfirst(self, ctx):
        """
        Adds a name to the firstname set.
        """
        name = re.sub(r'^!addfirst ', '', ctx.message.content)
        utils.addfirst(name)
        await ctx.send("Added " + name + " to the first name list") 
    
    #add a last name to the file
    @commands.command(name="addlast")
    async def addlast(self, ctx):
        """
        Adds a name to the lastname set.
        """
        name = re.sub(r'^!addlast ', '', ctx.message.content)
        utils.addlast(name)
        await ctx.send("Added " + name + " to the last name list") 
    #turn off bot
        #only Stephen and Colin have permission to do this
    @commands.command(name="shutdown", hidden=True)
    async def shutdown(self, ctx):
        """
        Shuts down the bot, only usable by admin
        """
        auth = ctx.message.author.id
        if Globals.users[auth] in Globals.root:
            #shutdown
            await ctx.send("Shutting Down...")
            await self.bot.close()
        elif auth in Globals.users:
            #sassy message
            await ctx.send("You cannot kill me, " + str(users[auth]).title() + ", you peasant")
        else:
            await ctx.send("You do not have permission to turn off this bot")
            #non-sassy message
    @commands.command(name="ping")
    async def ping(self, ctx):
        """
        pong
        """
        await ctx.send("pong")


def setup(bot):
  bot.add_cog(Misc(bot))