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
        self.board[x,y] = amount

    def Fall(self, x,y):

        Grains = self.board[x, y] // self.pilesize
        self.board[x, y] = self.board[x, y] % self.pilesize

        self.board[x+1,y]+=Grains


        self.board[x-1,y]+=Grains


        self.board[x,y+1]+=Grains


        self.board[x,y-1]+=Grains


        self.board[0]=0
        self.board[-1]=0
        self.board[:,0]=0
        self.board[:,-1]=0





    def Topple(self):

        start = default_timer()
        while np.max(self.board) >= self.pilesize:


            a, b = np.where(test.board >= test.pilesize)

            self.Fall(a,b)


        duration = default_timer() - start
        print(duration)

    def ShowGraph(self):
        map = plot.pcolor(test.board)
        plot.axis("off")
        plot.imshow(test.board)
        plot.colorbar(map, ticks=range(self.pilesize))
        plot.show()













if __name__== '__main__':
    test = SandPile(4,501,501)

    #test.AddSand(101,101,100000)
    #test.AddSand(401,401,100000)
    #test.AddSand(101,401,100000)
    #test.AddSand(401,101,100000)
    test.AddSand(250,250,100000)

    test.Topple()





    test.ShowGraph()


