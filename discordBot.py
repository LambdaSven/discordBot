import discord
from discord.ext import commands
import tokens

#set default for the bot
bot = commands.Bot(command_prefix='!', description='does a few things')

#log to console when bot is active
@bot.event
async def on_ready():
    print("Logged in as")
    print(bot.user.name)
    print(bot.user.id)
    print("---")
    game = discord.Game("with the API")
    await bot.change_presence(activity=game)

extensions = ['cogs.Simul',
              'cogs.Monster',
              'cogs.Misc',
              'cogs.Audio',
              'cogs.Mines',
              'cogs.Words']

for x in extensions:
    bot.load_extension(x)



#run the bot
bot.run(tokens.discordBotToken)






