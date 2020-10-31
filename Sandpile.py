import numpy as np
import matplotlib.pyplot as plot
from timeit import default_timer


class SandPile():
    def __init__(self, pilesize, row, col):
        #create the board
        self.pilesize = pilesize
        self.row = row
        self.col = col
        self.board = np.zeros((col, row), int)



    def AddSand(self,x,y,amount):
        #Add specified amount of sand to the specified location
        self.board[x,y] = amount

    def Fall(self, x,y):
        #Makes the specified pile collapse and distribute it's sand to the tiles around it
        Grains = self.board[x, y] // self.pilesize
        self.board[x, y] = self.board[x, y] % self.pilesize

        self.board[x+1,y]+=Grains


        self.board[x-1,y]+=Grains


        self.board[x,y+1]+=Grains


        self.board[x,y-1]+=Grains

        #Clears a 1 space border around the board to insure there are no Index errors
        self.board[0]=0
        self.board[-1]=0
        self.board[:,0]=0
        self.board[:,-1]=0





    def Topple(self):
        #Checks if there are any piles that are too large
        start = default_timer() #Times the process
        while np.max(self.board) >= self.pilesize:


            a, b = np.where(test.board >= test.pilesize)

            self.Fall(a,b)


        duration = default_timer() - start
        print(duration)

    def ShowGraph(self):
        #Displays the final product
        map = plot.pcolor(self.board)
        plot.axis("off")
        plot.imshow(self.board)
        plot.colorbar(map, ticks=range(self.pilesize))
        plot.show()













if __name__== '__main__':
    test = SandPile(4,501,501)
    test.AddSand(250,250,100000)

    test.Topple()

    test.ShowGraph()


