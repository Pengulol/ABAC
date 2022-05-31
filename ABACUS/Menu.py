import tkinter as tk
from tkinter import *
from Abac import Abac


class Menu:

    def __init__(self, root):

        self.root = root
        self.canvas = tk.Canvas(root, bg="DodgerBlue3")
        self.canvas.pack(fill="both", expand=True)
        self.canvas.configure(width=1920, height=1080)

        self.ResultSiExit = tk.Frame(self.canvas)
        self.frameCalcul = tk.Frame(self.canvas)

        self.text = tk.StringVar()
        self.text.set("RESULT:  -  ")

        self.buttonResult = Button(self.ResultSiExit, text="RESULT", command=self.result)
        self.buttonResult.config(width=40, height=5)
        self.buttonResult.pack(side=TOP)

        self.Result = Label(self.ResultSiExit, textvariable=self.text)
        self.Result.config(width=40, height=5)
        self.Result.pack(side=TOP)

        self.buttonExit = Button(self.ResultSiExit, text="EXIT", command=root.quit)
        self.buttonExit.config(width=40, height=5)
        self.buttonExit.pack(side=TOP)

        self.ResultSiExit.place(anchor=NW)

        self.buttonCompute = Button(self.frameCalcul, text="COMPUTE", command=self.computef)
        self.buttonCompute.config(width=40)
        self.buttonCompute.pack(pady=10, side=TOP)

        self.framePrim = Frame(self.frameCalcul)
        self.primulOperand = Entry(self.framePrim, width=15)
        self.primulOperand.pack(side=RIGHT)
        self.primulOperand_lable = Label(self.framePrim, text="X = ")
        self.primulOperand_lable.pack(side=LEFT)
        self.framePrim.pack(side=TOP)

        self.frameDoi = Frame(self.frameCalcul)
        self.alDoileaOperand = Entry(self.frameDoi, width=15)
        self.alDoileaOperand.pack(side=RIGHT)
        self.alDoileaOperand_lable = Label(self.frameDoi, text="Y = ")
        self.alDoileaOperand_lable.pack(side=LEFT)
        self.frameDoi.pack(side=TOP)

        self.optiune = StringVar()
        self.optiune.set("adunare")
        self.dropbox = OptionMenu(self.frameCalcul, self.optiune, "adunare", "scadere", "inmultire", "impartire")
        self.dropbox.config(width=30, font=10)
        self.dropbox.pack(pady=10, side=TOP)

        self.eroare = Label(self.frameCalcul, text='')
        self.eroare.pack(side=TOP)

        self.var = tk.IntVar()
        self.buttonNext = Button(self.frameCalcul, text="-->", width=30, command=lambda: self.var.set(1), state=DISABLED)
        self.buttonNext.pack(side=TOP)

        self.frameCalcul.pack(side=LEFT)

        self.abac = Abac(self.canvas)

    def resultSUS(self):
        res = 0
        inc = 1
        for x in range(0, 7, +1):
            for bila in self.abac.VectorBare[x].VectorBile:
                if bila.isMoved:
                    res = res + inc

            inc = inc * 10

        return res

    def resultJOS(self):
        res = 0
        inc = 1
        for x in range(9, 6, -1):
            for bila in self.abac.VectorBare[x].VectorBile:
                if bila.isMoved is True:
                    res = res + inc

            inc = inc * 10

        return res

    def resultImpartire(self):
        resSus = self.resultSUS()
        resJos = self.resultJOS()
        self.text.set("RESULT:" + str(resJos) + " Rest:" + str(resSus))

    def result(self):
        if not self.abac.toggleImpartire:
            res = 0
            inc = 1

            for x in range(9, -1, -1):
                for bila in self.abac.VectorBare[x].VectorBile:
                    if bila.isMoved is True:
                        res = res + inc

                inc = inc * 10

            self.text.set("RESULT:" + str(res))
        else:
            self.resultImpartire()

    def adaugareNumarInversat(self, numar, nrCifre):
        nrBara = 10 - nrCifre

        while nrBara < 10:
            cifraAux = numar % 10
            bile = self.abac.VectorBare[nrBara].numberOfMovedBalls()
            suma = cifraAux + bile

            if suma >= 10:
                self.buttonNext.wait_variable(self.var)
                suma = suma - 10
                self.abac.VectorBare[nrBara].moveBalls(0)
                self.abac.VectorBare[nrBara].recolorBara()
                self.buttonNext.wait_variable(self.var)
                self.abac.repairAdunare()
                self.buttonNext.wait_variable(self.var)

                while suma > 0:
                    self.abac.VectorBare[nrBara].addOneBall()
                    self.abac.VectorBare[nrBara].recolorBara()

                    suma = suma - 1
            else:
                self.buttonNext.wait_variable(self.var)

                while cifraAux > 0:
                    self.abac.VectorBare[nrBara].addOneBall()
                    self.abac.VectorBare[nrBara].recolorBara()

                    cifraAux = cifraAux - 1

            numar = int(numar / 10)
            nrBara = nrBara + 1

    def scadereNumarInversat(self, numar, nrCifre):
        nrBara = 10 - nrCifre

        while nrBara < 10:
            cifraAux = numar % 10
            bile = self.abac.VectorBare[nrBara].numberOfMovedBalls()
            diferenta = bile - cifraAux

            if diferenta < 0:
                if not self.abac.VectorBare[nrBara].isEmpty():
                    self.buttonNext.wait_variable(self.var)
                    self.abac.VectorBare[nrBara].moveBalls(9)
                    self.abac.VectorBare[nrBara].recolorBara()

                self.buttonNext.wait_variable(self.var)
                nrBaraAux = nrBara - 1

                while self.abac.VectorBare[nrBaraAux].isEmpty():
                    self.abac.VectorBare[nrBaraAux].moveBalls(1)
                    self.abac.VectorBare[nrBaraAux].recolorBara()
                    self.buttonNext.wait_variable(self.var)
                    nrBaraAux = nrBaraAux - 1

                self.abac.VectorBare[nrBaraAux].removeOneBall()
                self.abac.VectorBare[nrBaraAux].makeTransportLastUnMovedBall()

                self.buttonNext.wait_variable(self.var)
                diferenta = 10 + diferenta

                for x in range(0, diferenta):
                    self.abac.VectorBare[nrBara].addOneBall()

                self.abac.VectorBare[nrBara].recolorBara()
            else:
                self.buttonNext.wait_variable(self.var)

                for x in range(0, cifraAux):
                    self.abac.VectorBare[nrBara].removeOneBall()
            self.abac.VectorBare[nrBara].recolorBara()
            numar = int(numar / 10)
            nrBara = nrBara + 1

    def scadereSus(self, nrScazator):
        nrBara = 0

        while nrScazator > 0:
            if self.abac.VectorBare[nrBara].isEmpty():
                self.abac.VectorBare[nrBara].moveBalls(0)
                self.abac.VectorBare[nrBara].recolorBara()
                nrBaraAux = nrBara + 1

                while self.abac.VectorBare[nrBaraAux].isEmpty():
                    self.abac.VectorBare[nrBaraAux].moveBalls(1)
                    self.abac.VectorBare[nrBaraAux].recolorBara()
                    nrBaraAux = nrBaraAux + 1

                self.abac.VectorBare[nrBaraAux].removeOneBall()
                self.abac.VectorBare[nrBaraAux].makeTransportLastUnMovedBall()
                self.buttonNext.wait_variable(self.var)
                self.abac.VectorBare[nrBaraAux].recolorBara()

                self.abac.VectorBare[nrBara].moveBalls(0)

            self.abac.VectorBare[nrBara].removeOneBall()
            self.abac.VectorBare[nrBara].recolorBara()
            nrScazator = nrScazator - 1

    def setareStareButoane(self, newState):
        self.buttonCompute.config(state=newState)
        self.dropbox.config(state=newState)
        self.buttonExit.config(state=newState)
        self.primulOperand.config(state=newState)
        self.alDoileaOperand.config(state=newState)
        self.buttonResult.config(state=newState)
        if newState is NORMAL:
            self.buttonNext.config(state=DISABLED)
        elif newState is DISABLED:
            self.buttonNext.config(state=NORMAL)

        self.abac.toggleMouse = not self.abac.toggleMouse

    @staticmethod
    def invNumar(numar):
        aux = 0

        while numar > 0:
            aux = aux * 10 + int(numar % 10)
            numar = int(numar / 10)

        return aux

    @staticmethod
    def cifreNumar(numar):
        nrCifre = 0

        while numar > 0:
            nrCifre = nrCifre + 1
            numar = int(numar / 10)

        return nrCifre

    def adunare(self, op1, op2):
        self.abac.resetAbac()
        self.abac.setareNumarJos(op1)

        a = self.invNumar(op2)
        b = self.cifreNumar(op2)
        self.adaugareNumarInversat(a, b)
        self.eroare.config(text="Final apasa pe result")

    def scadere(self, op1, op2):
        if op1 - op2 < 0:
            self.eroare.config(text="error result is negativ")
            return
        self.abac.resetAbac()
        self.abac.setareNumarJos(op1)
        a = self.invNumar(op2)
        b = self.cifreNumar(op2)
        self.scadereNumarInversat(a, b)
        self.eroare.config(text="Final apasa pe result")

    def inmultire(self, op1, op2):
        if op1 < op2:
            aux = op1
            op1 = op2
            op2 = aux

        self.abac.setareNumarJos(op1)
        self.abac.setareNumarSus(op2)
        a = self.invNumar(op1)
        b = self.cifreNumar(op1)
        op2 = op2 - 1
        self.buttonNext.wait_variable(self.var)
        self.abac.VectorBare[0].removeOneBall()
        self.abac.VectorBare[0].recolorBara()

        while op2 > 0:
            op2 = op2 - 1
            self.buttonNext.wait_variable(self.var)
            self.scadereSus(1)
            self.adaugareNumarInversat(a, b)

        self.eroare.config(text="Final apasa pe result")

    def impartire(self, op1, op2):
        self.abac.toggleImpartire = True
        self.abac.setareNumarSus(op1)

        while op1 >= op2:
            self.buttonNext.wait_variable(self.var)
            self.scadereSus(op2)
            self.adaugareNumarInversat(1, 1)
            op1 = op1 - op2

        self.eroare.config(text="Final apasa pe result")

    def switch(self, optiune, op1, op2):
        if optiune == "+":
            self.adunare(op1, op2)
        elif optiune == "-":
            self.scadere(op1, op2)
        elif optiune == "*":
            self.inmultire(op1, op2)
        elif optiune == "/":
            self.impartire(op1, op2)
        else:
            print("something went wrong2")

    def computef(self):
        self.abac.toggleImpartire = False
        self.abac.resetAbac()
        self.setareStareButoane(DISABLED)
        try:
            op1 = int(self.primulOperand.get())
            op2 = int(self.alDoileaOperand.get())
            self.eroare.config(text="")
        except:
            self.eroare.config(text="please insert numbers")
            self.primulOperand.delete(0, END)
            self.alDoileaOperand.delete(0, END)
            self.setareStareButoane(NORMAL)
            return

        if op1 < 0 or op2 < 0:
            self.eroare.config(text="please insert natural numbers")
            self.primulOperand.delete(0, END)
            self.alDoileaOperand.delete(0, END)
            self.setareStareButoane(NORMAL)
            return

        opt = self.optiune.get()
        self.switch(opt, op1, op2)

        self.setareStareButoane(NORMAL)
