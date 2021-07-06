import random

class Minesweeper:
  def __init__(self, dim: int, mines: int):
    self.dim = dim
    self.mines = mines
    self.board = self.genboard(dim, mines)
    self.set_numbers()

  def genboard(self, dim, mines):
    count = 0
    board = [[0] * dim for e in range(dim)]
    #init
    while count < mines:
      x = random.randrange(0, dim)
      y = random.randrange(0, dim)
      if board[x][y] == 0:
        count += 1
        board[x][y] = 9 
    return board
  
  def count_adj(self, x, y):
    count = 0
    for i in range(-1, 2):
      for j in range(-1, 2):
        if x + i >= 0 and x + i < self.dim and y + j >= 0 and y + j < self.dim and not (i == 0 and j == 0):
          if self.board[x+i][y+j] == 9:
            count += 1
    return count

  def set_numbers(self):
    for x in range(0, self.dim):
      for y in range(0, self.dim):
        if self.board[x][y] is not 9:
          self.board[x][y] = self.count_adj(x, y)



  #place numbers