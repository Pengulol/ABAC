import tkinter as tk
from tkinter import *
from Bara import Bara

class Abac:



    def __init__ (self,canvas):
        X1 = 730
        X2 = 1570
        Y = 140
        self.toggleImpartire = False
        self.toggleMouse=True
        self.canvas=canvas
        self.canvas.create_rectangle(X1-30, 100, X1, 1050, fill = "#90453A")
        self.canvas.create_rectangle(X2, 100, X2 + 30, 1050, fill="#90453A")

        self.VectorTevi = []
        for z in range(0, 10):

            a=Bara(canvas, X1, X2,Y , Y + 10, z)
            Y = Y + 90
            self.VectorTevi.append(a)





        def onclick(event):
            if self.toggleMouse:
                x = event.x
                y = event.y
                for bara in self.VectorTevi:
                    if y < bara.centerline + 35 and y > bara.centerline - 35 and x < bara.X2 and x > bara.X1:

                        for bila in bara.VectorBile:
                            if x > bila.X and x < bila.X + bila.diametru and y > bila.Y and y < bila.Y + bila.diametru:
                                print(bila.nrBara)
                                self.toggleImpartire = False
                                bara.moveBalls(bila.nrBila)
                                break
                        break

        self.canvas.bind('<Button-1>', onclick)


    def setareNumarSus(self, numar):

        aux = numar
        teavaCurenta = 0
        while aux > 0:
            nrBile = aux%10
            for x in range(0,nrBile, +1):
                self.VectorTevi[teavaCurenta].addBall()
            aux = int(aux/10)
            teavaCurenta = teavaCurenta+1




    def setareNumar(self, numar):

        aux = numar
        teavaCurenta = 9
        while aux > 0:
            nrBile = aux%10
            for x in range(0,nrBile, +1):
                self.VectorTevi[teavaCurenta].addBall()
            aux = int(aux/10)
            teavaCurenta = teavaCurenta-1

    def repairAdunare(self):
        for numarBara in range(9,0,-1):
            if self.VectorTevi[numarBara].isFilled():
                for x in range(0, 10 , + 1):
                    self.VectorTevi[numarBara].removeBall()
                self.VectorTevi[numarBara-1].addBall()




    def resetBara(self, numarBara):
        if self.VectorTevi[numarBara].VectorBile[9].isMoved:
            self.VectorTevi[numarBara].moveBalls(9)

    def reset(self):
        for bara in self.VectorTevi:
            self.resetBara(bara.numarbara)


