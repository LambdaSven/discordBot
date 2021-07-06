import discord
from discord.ext import commands
import time
import Globals
import youtube_dl
import Stick

ydl_opts = {
    'format': 'bestaudio/best',
}   
FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

class Audio(commands.Cog):
    """
    Various Misc commands
    """
    def __init__(self, bot):
      self.bot = bot

    @commands.Cog.listener()
    async def on_voice_state_update(self, m:discord.Member, b, a):
      if m.id not in Globals.users:
        return

      if Globals.users[m.id] == 'user1' and b.channel is None:
        time.sleep(1)
        await self.playNoContext(m, 'audioFile', 0.2)

      if Globals.users[m.id] == 'user2' and b.channel is None:
        time.sleep(1)
        await self.playNoContext(m, 'audiofile2', 0.8)

      # Repeat for each user

    @commands.command(name="monkey")
    async def monkey(self, ctx):
      """
      Monkey

      Hmm. Monkey
      """
      await self.play(ctx, 'monkey', 1.0)

    @commands.command(name="stick")
    async def stick(self, ctx):
      """
      Get Stickbugged

      lol
      """
      await ctx.send("https://media.tenor.com/images/36dd82e085114a98fe9cfe428d7a4031/tenor.gif");
      await self.play(ctx, 'stickbug', 1.0)
      

    @commands.command(name="ydl", hidden=True)
    async def ydl(self, ctx, s: str):
      if not Globals.users[ctx.author.id] in Globals.root:
        await ctx.send("You are not authorized to use this command.")
        return
      if not ctx.message.author.voice:
        await ctx.send("You are not in voice")
        return
      

      state = ctx.message.author.voice
      voice = await state.channel.connect()

      with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(s, download=False)
        URL = info['formats'][0]['url']
      
      voice.play(discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(URL, **FFMPEG_OPTIONS), 0.3))
      while voice.is_playing():
        time.sleep(.1)
      await voice.disconnect()


    @commands.command(name="die")
    async def die(self, ctx):
      """
      Die.
      """
      await self.playNoContext(ctx.message.author, 'die', 1.0)
      await ctx.author.move_to(None)

    @commands.command(name="getfucked")
    async def getfucked(self, ctx, m: discord.Member=None):
      """
      Get fucked

      Includes optional parameter, which is who you are telling to get fucked
      """

      if m is None:
        await self.play(ctx, 'getfucked', 0.2)
        await ctx.send("Get fucked.")
      else:
        if m.voice is None:
          await ctx.send("User is not in voice.")
        else:
          await self.playNoContext(m, 'getfucked', 0.2)
          await m.send(ctx.message.author.display_name + " says: Get fucked.")
        

    @commands.command(name="bonk")
    async def bonk(self, ctx, s: str="the server"):
      """
      Bonk the Voice chat

      Only usable if you are also in voice, bonks the same channel you are in.
      """
      await self.play(ctx, 'bonk', 0.8)
      await ctx.send(ctx.message.author.display_name + " has bonked " + s)
  

    @commands.command(name="ban")
    async def ban(self, ctx, m:discord.Member):
      """
      "Ban" a user

      You must tag the user for the ban to succeed, otherwise it will ban you instead
      Only usable if you are also in voice
      """
      if ctx.author.voice is None:
        await ctx.send(ctx.author.display_name + " is not in voice. ") 
        return
      await self.play(ctx, 'banned', 0.8)
      await ctx.send(ctx.message.author.display_name + " has \"banned\" " + m.display_name + " from the server")
      await m.move_to(None)

    @getfucked.error
    async def getfucked_error(self, ctx, error):
      await ctx.send("Member could not be found.")

    @ban.error
    async def ban_error(self, ctx, error):
        await self.play(ctx, 'bonk', 0.8)
        await ctx.author.move_to(None)
        await ctx.send(ctx.message.author.display_name + " has hurt themselves in their confusion!")

    @commands.command(name="play", hidden=True)
    async def play(self, ctx, s: str='bonk', f: float=0.5):
        s = "data/" + s + ".mp3" 
        if len(self.bot.voice_clients) > 0:
          return
        voice = ctx.author.voice
        if voice != None:
          vc = await voice.channel.connect()
          vc.play(discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(s), volume=f))
          while vc.is_playing():
            time.sleep(.1)
          await vc.disconnect()
        else:
          await ctx.send(str(ctx.author.display_name) + " is not in voice. ")

    @play.error
    async def play_error(self, ctx, error):
        await ctx.send("File not Found.")

    async def playNoContext(self, m: discord.Member, s: str, f: float):
        voice = m.voice
        s = "data/" + s + ".mp3"
        if voice != None:
          vc = await voice.channel.connect()
          vc.play(discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(s), volume=f))
          while vc.is_playing():
            time.sleep(.1)
          await vc.disconnect()

def setup(bot):
  bot.add_cog(Audio(bot))