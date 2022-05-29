import tkinter as tk
from tkinter import *
import time
from Abac import Abac

res = 0


class Menu:

    def __init__(self, root):


        self.root = root
        self.canvas = tk.Canvas(root, bg="DodgerBlue3")
        self.canvas.pack(fill="both", expand=True)
        self.canvas.configure(width=1920, height=1080)

        self.frame1 = tk.Frame(self.canvas)
        self.frame2 = tk.Frame(self.canvas)
        self.frameCalcul = tk.Frame(self.canvas)
        self.text = tk.StringVar()
        self.text.set("RESULT:  -  ")
        self.Result = Label(self.frame1, textvariable=self.text)
        self.Result.config(width=50, height=5)

        self.buttonCompute = Button(self.frameCalcul, text="COMPUTE", command=self.computef)
        self.buttonCompute.config(width=20)
        self.buttonCompute.pack(pady=10, side=TOP)

        self.buttonResult = Button(self.frame1, text="RESULT", command=self.result)
        self.buttonResult.config(width=50, height=5)
        self.buttonResult.pack(side=TOP)

        self.Result.pack(side=TOP)

        self.buttonExit = Button(self.frame1, text="EXIT", command=root.quit)
        self.buttonExit.config(width=50, height=5)
        self.buttonExit.pack(side=TOP)

        self.frame1.place(anchor=NW)

        self.framePrim = Frame(self.frameCalcul)
        self.primulOperand = Entry(self.framePrim, width=10)
        self.primulOperand.pack(side=RIGHT)
        self.primulOperand_lable = Label(self.framePrim, text="X = ")
        self.primulOperand_lable.pack(side=LEFT)
        self.framePrim.pack(side=TOP)

        self.frameDoi = Frame(self.frameCalcul)
        self.alDoileaOperand = Entry(self.frameDoi, width=10)
        self.alDoileaOperand.pack(side=RIGHT)
        self.alDoileaOperand_lable = Label(self.frameDoi, text="Y = ")
        self.alDoileaOperand_lable.pack(side=LEFT)
        self.frameDoi.pack(side=TOP)






        self.optiune = StringVar()
        self.optiune.set("+")

        self.dropbox = OptionMenu(self.frameCalcul, self.optiune, "+", "-", "*", "/")
        self.dropbox.pack(side=TOP)

        self.eroare = Label(self.frameCalcul, text='')
        self.eroare.pack(side=TOP)

        self.var = tk.IntVar()
        self.buttonNext=Button(self.frameCalcul,text="-->",command=lambda:self.var.set(1),state=DISABLED)
        self.buttonNext.pack(side=TOP)

        self.frameCalcul.pack(side=LEFT)

        self.abac = Abac( self.canvas)

    def resultSUS(self):
        res = 0
        inc = 1
        for x in range(0, 7 , +1):
            for bila in self.abac.VectorTevi[x].VectorBile:
                if bila.isMoved == True:
                    res = res + inc
            inc = inc*10
        return res

    def resultJOS(self):
        res = 0
        inc = 1
        for x in range(9, 6, -1):
            for bila in self.abac.VectorTevi[x].VectorBile:
                if bila.isMoved == True:
                    res = res + inc
            inc = inc * 10
        return res

    def resultImpartire(self):
        resSus=self.resultSUS()
        resJos=self.resultJOS()
        self.text.set("RESULT:" + str(resJos) +" Rest:" + str(resSus))

    def result(self):
        if not self.abac.toggleImpartire:
            res = 0
            inc = 1
            for x in range(9, -1, -1):
                for bila in self.abac.VectorTevi[x].VectorBile:
                    if bila.isMoved == True:
                        res = res + inc
                inc = inc * 10
            self.text.set("RESULT:" + str(res))
        else:
            self.resultImpartire()

    def adaugareNumarInversat(self, numar, nrCifre):
        nrTeava = 10 - nrCifre

        while (nrTeava < 10):
            cifraAux = numar % 10
            bile = self.abac.VectorTevi[nrTeava].numberOfMovedBalls()
            suma=cifraAux + bile
            if suma >= 10:
                self.buttonNext.wait_variable(self.var)
                suma = suma - 10
                self.abac.VectorTevi[nrTeava].moveBalls(0)
                self.buttonNext.wait_variable(self.var)
                self.abac.repairAdunare()
                self.buttonNext.wait_variable(self.var)
                while suma > 0:
                    self.abac.VectorTevi[nrTeava].addBall()
                    suma = suma - 1
            else:
                self.buttonNext.wait_variable(self.var)
                while cifraAux > 0:

                    self.abac.VectorTevi[nrTeava].addBall()
                    cifraAux = cifraAux - 1

            numar = int(numar/10)

            nrTeava = nrTeava+1

    def scadereNumarInversat(self, numar, nrCifre):
        nrTeava = 10 - nrCifre

        while (nrTeava < 10):
            cifraAux = numar % 10
            bile = self.abac.VectorTevi[nrTeava].numberOfMovedBalls()
            diferenta = bile - cifraAux
            if diferenta < 0:

                if not self.abac.VectorTevi[nrTeava].isEmpty():
                    self.buttonNext.wait_variable(self.var)
                    self.abac.VectorTevi[nrTeava].moveBalls(9)
                self.buttonNext.wait_variable(self.var)

                nrTeavaAux = nrTeava - 1
                while self.abac.VectorTevi[nrTeavaAux].isEmpty():
                    self.abac.VectorTevi[nrTeavaAux].moveBalls(1)
                    self.buttonNext.wait_variable(self.var)
                    nrTeavaAux = nrTeavaAux - 1

                self.abac.VectorTevi[nrTeavaAux].removeBall()
                self.buttonNext.wait_variable(self.var)
                diferenta = 10 + diferenta
                for x in range(0, diferenta):
                    self.abac.VectorTevi[nrTeava].addBall()

            else:
                self.buttonNext.wait_variable(self.var)
                for x in range(0, cifraAux):
                    self.abac.VectorTevi[nrTeava].removeBall()
            numar = int(numar/10)
            nrTeava = nrTeava + 1

    def scadereSus(self,nrScazator):
        teavaCurenta=0
        while nrScazator>0:
            if self.abac.VectorTevi[teavaCurenta].isEmpty():
                self.abac.VectorTevi[teavaCurenta].moveBalls(0)
                auxTeava=teavaCurenta+1
                while self.abac.VectorTevi[auxTeava].isEmpty():
                    self.abac.VectorTevi[auxTeava].moveBalls(1)
                    auxTeava=auxTeava+1
                self.abac.VectorTevi[auxTeava].removeBall()
                self.buttonNext.wait_variable(self.var)
            self.abac.VectorTevi[teavaCurenta].removeBall()
            nrScazator=nrScazator-1

    def resetareButoane(self):
        self.buttonCompute.config(state=NORMAL)
        self.dropbox.config(state=NORMAL)
        self.buttonExit.config(state=NORMAL)
        self.primulOperand.config(state=NORMAL)
        self.alDoileaOperand.config(state=NORMAL)
        self.buttonResult.config(state=NORMAL)
        self.buttonNext.config(state=DISABLED)
        self.abac.toggleMouse = True

    def invNumar(self,numar):
        aux=0
        while numar>0:
            aux=aux*10+int(numar%10)
            numar=int(numar/10)
        return aux

    def cifreNumar(self,numar):
        nrcifre=0
        while numar>0:
            nrcifre=nrcifre+1
            numar=int(numar/10)
        return nrcifre

    def adunare(self, op1, op2):
        self.abac.reset()
        self.abac.setareNumar(op1)

        a = self.invNumar(op2)
        b = self.cifreNumar(op2)
        self.adaugareNumarInversat(a,b)
        self.eroare.config(text="Final apasa pe result")

    def scadere(self, op1, op2):
        self.abac.reset()
        self.abac.setareNumar(op1)
        a = self.invNumar(op2)
        b = self.cifreNumar(op2)
        self.scadereNumarInversat(a,b)
        self.eroare.config(text="Final apasa pe result")

    def inmultire(self, op1, op2):
        if op1<op2:
            aux=op1
            op1=op2
            op2=aux
        self.abac.setareNumar(op1)
        self.abac.setareNumarSus(op2)
        a = self.invNumar(op1)
        b = self.cifreNumar(op1)
        op2 = op2 - 1
        self.buttonNext.wait_variable(self.var)
        self.abac.VectorTevi[0].removeBall()
        while op2 > 0:
            op2 = op2-1
            self.buttonNext.wait_variable(self.var)
            self.scadereSus(1)
            self.adaugareNumarInversat(a,b)
        self.eroare.config(text="Final apasa pe result")


    def impartire(self, op1, op2):
        self.abac.toggleImpartire = True
        if op1 < op2:
            aux = op1
            op1 = op2
            op2 = aux
        self.abac.setareNumarSus(op1)
        while op1 >= op2:
            self.buttonNext.wait_variable(self.var)
            self.scadereSus(op2)
            self.adaugareNumarInversat(1,1)
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
        self.abac.reset()
        self.abac.toggleMouse=False
        self.buttonNext.config(state=NORMAL)
        self.buttonCompute.config(state=DISABLED)
        self.dropbox.config(state=DISABLED)
        self.buttonExit.config(state=DISABLED)
        self.primulOperand.config(state=DISABLED)
        self.alDoileaOperand.config(state=DISABLED)
        self.buttonResult.config(state=DISABLED)
        try:
            op1 = int(self.primulOperand.get())
            op2 = int(self.alDoileaOperand.get())
            self.eroare.config(text="")


        except:
            self.eroare.config(text="please insert numbers")
            self.primulOperand.delete(0, END)
            self.alDoileaOperand.delete(0, END)
            self.resetareButoane()
            return



        if op1 < 0 or op2 < 0:
            self.eroare.config(text="please insert natural numbers")
            self.primulOperand.delete(0, END)
            self.alDoileaOperand.delete(0, END)
            self.resetareButoane()
            return




        opt = self.optiune.get()
        self.switch(opt, op1, op2)

        self.resetareButoane()