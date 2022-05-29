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


    def moveBalls(self, nrBila):

        if self.VectorBile[nrBila].isMoved:
            for x in range(nrBila, -1, -1):
                if self.VectorBile[x].isMoved:
                    self.VectorBile[x].moveLeft()

        else:
            for x in range(nrBila, 10, +1):
                if not self.VectorBile[x].isMoved:
                    self.VectorBile[x].moveRight()
