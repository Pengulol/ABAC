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

        self.button1 = Button(self.frameCalcul, text="COMPUTE", command=self.computef)
        self.button1.config(width=20)
        self.button1.pack(pady=10, side=TOP)

        self.button2 = Button(self.frame1, text="RESULT", command=self.result)
        self.button2.config(width=50, height=5)
        self.button2.pack(side=TOP)

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
        self.frameCalcul.pack(side=LEFT)

        self.abac = Abac(self.canvas)

    def result(self):

        res = 0
        inc = 1
        for x in range(9, -1, -1):
            for bila in self.abac.VectorTevi[x].VectorBile:
                if bila.isMoved == True:
                    res = res + inc
            inc = inc * 10
        self.text.set("RESULT:" + str(res))













    def adunare(self, op1, op2):
        x = op1 + op2
        self.abac.setareNumar(op1)




        print(x)

    def scadere(self, op1, op2):
        x = op1 - op2
        if op1 < op2:
            self.eroare.config(text="error: result is negative")
            return
        print(x)

    def inmultire(self, op1, op2):
        x = op1 * op2
        print(x)

    def impartire(self, op1, op2):
        x = op1 / op2
        print(x)

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
        self.abac.reset()
        try:
            op1 = int(self.primulOperand.get())
            op2 = int(self.alDoileaOperand.get())
            self.eroare.config(text="")

        except:
            self.eroare.config(text="please insert numbers")
            self.primulOperand.delete(0, END)
            self.alDoileaOperand.delete(0, END)
            return
        if op1 < 0 or op2 < 0:
            self.eroare.config(text="please insert natural numbers")
            return

        opt = self.optiune.get()
        self.switch(opt, op1, op2)