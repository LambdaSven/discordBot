import discord
from discord.ext import commands
import Minesweeper

class Mines(commands.Cog, name="Minesweeper"):
  """
  Play Minesweeper :)
  """
  def __init__(self, bot, dim, mines):
    self.bot = bot
    self.dim = dim
    self.mines = mines
    self.game = Minesweeper.Minesweeper(dim, mines)
    self.logic = [[False] * dim for e in range(dim)]
    self.flags = [[False] * dim for e in range(dim)]
    self.message = None
    self.ended = False

  @commands.command(name="force_reprint", hidden=True)
  async def force_reprint(self, ctx):
    if self.message is not None:
      await self.message.delete()
    self.message = await ctx.send(self.display())

  @commands.command(name="mines")
  async def newgame(self, ctx, dim: int=8, mines: int=8):
    """
    Create a new Minesweeper Game

    Accepts optional paramaters for dimensions and number of mines
      Warning, if you go too high it will not display properly
    """
    if mines > 9:
      await ctx.send("9 is the maximum dimension allowed")
    if self.message is not None:
      await self.message.delete()
    self.dim = dim
    self.mines = mines
    self.game = Minesweeper.Minesweeper(dim, mines)
    self.logic = [[False] * dim for e in range(dim)]
    self.flags = [[False] * dim for e in range(dim)]
    self.message = await ctx.send(self.display())
    self.ended = False

  @commands.command(name="reveal")
  async def reveal(self, ctx, y: int, x: int):
    """
    Reveal a square on the current minesweeper board

    Input your coordinates as (x, y), (1, 1) is the bottom left corner.
      example, !reveal 2 3
    """
    if y < 1 or y > self.dim or x < 1 or x > self.dim:
      await ctx.send("Please enter a valid coordinate.")
      return
    if self.ended:
      return
    x -= 1
    y -= 1
    if self.flags[x][y]:
      return
    self.logic[x][y] = True
    if self.game.board[x][y] is 0:
      self.recurse(x, y)
    if self.game.board[x][y] == 9:
      await ctx.send("You Lose!")
    
    if self.check_win() == self.mines:
      await ctx.send("You Win!")
      self.ended = True
    
    await self.message.edit(content=self.display())
    await ctx.message.delete()

  @commands.command(name="flag")
  async def flag(self, ctx, y: int, x: int):
    """
    Flag a square on the current Minesweeper board

    Input your coordinates as (x, y), (1, 1) is the bottom left corner.
      example, !flag 2 3
    """
    if y < 1 or y > self.dim or x < 1 or x > self.dim:
      await ctx.send("Please enter a valid coordinate.")
      return
    x -= 1
    y -= 1
    if not self.logic[x][y]:
      self.flags[x][y] = not self.flags[x][y]
    await self.message.edit(content=self.display())
    await ctx.message.delete()


  def check_win(self):
    count = 0
    for x in range(0, self.dim):
      for y in range(0, self.dim):
        if not self.logic[x][y]:
          count += 1
    return count

  def recurse(self, x, y):
    if x < 0 or x >= self.dim or y < 0 or y >= self.dim:
      return
    for i in range(-1, 2):
      for j in range(-1, 2):
        if x + i >= 0 and x + i < self.dim and y + j >= 0 and y + j < self.dim:
          if not self.logic[x+i][y+j] and not self.flags[x+i][y+j]:
            self.logic[x+i][y+j] = True
            if self.game.board[x+i][y+j] is 0:
              self.recurse(x+i, y+j)
    

  def display(self):
    s = "\u200B"
    for x in range(self.dim-1, -1, -1):
      for y in range(0, self.dim):
        if not self.logic[x][y]:
          if self.flags[x][y]:
            s +=":triangular_flag_on_post:"
          else:
            s += ":black_small_square:"
        else:
          s += self.int_to_mine(self.game.board[x][y])
      s += "\n"
    return s

  def int_to_mine(self, y: int):
        if y == 0:
          return ":blue_square:"
        if y == 1:
          return ":one:"
        if y == 2:
          return ":two:"
        if y == 3:
          return ":three:"
        if y == 4:
          return ":four:"
        if y == 5:
          return ":five:"
        if y == 6:
          return ":six:"
        if y == 7:
          return ":seven:"
        if y == 8:
          return ":eight:"
        if y == 9:
          return ":boom:"
      

def setup(bot):
    bot.add_cog(Mines(bot, 8, 8))