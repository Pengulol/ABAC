import tkinter as tk
from tkinter import *
from Bila import Bila
class Bara:
    def __init__(self, canvas, X1, X2, Y1, Y2, numarbara):
        self.X1 = X1
        self.X2 = X2
        self.centerline = (Y1+Y2)/2
        self.numarbara = numarbara
        canvas.create_rectangle(X1, Y1, X2, Y2, fill="#ADADAD")
        self.VectorBile=[]
        X = X1
        Y = (Y1+Y2)/2 -35
        for z in range(0, 10):

            a=Bila(canvas, X , Y,numarbara,z)
            X=X+70

            self.VectorBile.append(a)

    def addBall(self):
        for x in range(0, 10 , +1):

            if (x == 9):

                self.VectorBile[9].moveRight()

                return
            if (self.VectorBile[x].isMoved == True):
                return

            if (self.VectorBile[x+1].isMoved == True):
                self.VectorBile[x].moveRight()
                return

    def isFilled(self):
        return self.VectorBile[0].isMoved
    def numberOfMovedBalls(self):
        nr = 0
        for x in range(0 , 10):
            if self.VectorBile[x].isMoved:
                nr = nr + 1
        return nr
    def removeBall(self):
        for x in range(9, -1 , -1):
            if(x == 0):
                self.moveBalls(0)
                return
            if(not self.VectorBile[x].isMoved):
                return
            if(not self.VectorBile[x-1].isMoved):
                self.VectorBile[x].moveLeft()
                return


    def moveBalls(self, pozBilaStart):

        if self.VectorBile[pozBilaStart].isMoved:
            for x in range(pozBilaStart, -1, -1):
                if self.VectorBile[x].isMoved:
                    self.VectorBile[x].moveLeft()

        else:
            for x in range(pozBilaStart, 10, +1):
                if not self.VectorBile[x].isMoved:
                    self.VectorBile[x].moveRight()
