import discord
import utils
from discord.ext import commands
import Globals
import json
import asyncio

class Words(commands.Cog, name="Words"):
  last_id = 0
  with open("./data/dict.json") as file:
    valid = json.load(file)

  with open("./data/saidWords.txt") as file:
    said = file.read().splitlines() 
    
  print(said) 
  if(len(said) == 0):
    reqletter = 'a'
  else:
    reqletter = said[-1][-1]

  @commands.Cog.listener()
  async def on_message(self, message):
    if message.channel.id != 862017885173186580 or message.author.id == 517775668814151695:
        return
    word = message.content.lower()
    if(len(word) < 3):
      await message.delete()
      await message.channel.send("Words must be at least 3 letters", delete_after=2)
      return
    if word in self.valid.keys():
      if word in self.said:
        await message.delete()
        await message.channel.send(word + " has already been said", delete_after=2)
        return
      if message.author.id == self.last_id:
        await message.delete()
        await message.channel.send("It is not your turn", delete_after=2)
        return
      if(word[0] == self.reqletter):
        await message.add_reaction("👍")
        self.reqletter = word[-1]
        utils.addWords(word)
        self.said.append(word)
        self.last_id = message.author.id
      else:
        await message.delete()
        await message.channel.send("That does not start with the required letter " + self.reqletter, delete_after=1)
    else:
      await message.delete()
      await message.channel.send("That is not a word", delete_after=2)



  def __init__(self, bot):
    self.bot = bot



def setup(bot):
    bot.add_cog(Words(bot))