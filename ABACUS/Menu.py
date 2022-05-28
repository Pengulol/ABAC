import tkinter as tk
from tkinter import *
from Bila import Bila
from Abac import Abac

class Menu:

    def __init__(self , root):

        self.root=root
        self.canvas = tk.Canvas(root,  bg="DodgerBlue3")
        self.canvas.pack(fill="both",expand=True)

        frame = tk.Frame(self.canvas)

        self.buttonStart = Button(frame, text="START",command = root.quit)
        self.buttonStart.config(width = 50 , height = 5 )
        self.buttonStart.pack(side = TOP)



        self.buttonExit = Button(frame, text="EXIT", command = root.quit)
        self.buttonExit.config(width = 50, height = 5)
        self.buttonExit.pack(side = TOP)

        frame.place(anchor = NW)

        Abac(self.canvas)
