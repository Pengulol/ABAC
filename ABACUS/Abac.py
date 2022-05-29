import tkinter as tk
from tkinter import *
from Bara import Bara
class Abac:




    def __init__ (self, canvas):
        X1 = 730
        X2 = 1570
        Y = 140
        self.canvas=canvas
        self.canvas.create_rectangle(X1-30, 100, X1, 1050, fill = "#90453A")
        self.canvas.create_rectangle(X2, 100, X2 + 30, 1050, fill="#90453A")

        self.VectorTevi = []
        for z in range(0, 10):

            a=Bara(canvas, X1, X2,Y , Y + 10, z)
            Y = Y + 90
            self.VectorTevi.append(a)





        def onclick(event):
            x=event.x
            y=event.y
            for bara in self.VectorTevi:
                if y < bara.centerline + 35 and y > bara.centerline - 35 and x < bara.X2 and x > bara.X1:
                    print(bara.centerline)
                    for bila in bara.VectorBile:
                        if x > bila.X and x < bila.X + bila.diametru and y > bila.Y and y < bila.Y + bila.diametru:
                            print(bila.nrBara)
                            print(bila.nrBila)
                            bara.moveBalls( bila.nrBila)
                            break
                    break

        self.canvas.bind('<Button-1>', onclick)



    def setareBile(self,nrTeava,nrBile):
        self.VectorTevi[nrTeava].moveBalls(10-nrBile)

    def resetBara(self, numarBara):
        if self.VectorTevi[numarBara].VectorBile[9].isMoved:
            self.VectorTevi[numarBara].moveBalls(9)

    def reset(self):
        for bara in self.VectorTevi:
            self.resetBara(bara.numarbara)