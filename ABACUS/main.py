import tkinter as tk
from tkinter import *
import os


def move():
    side=canvas.bbox(cerc)
    x1,y1,x2,y2=side
    if x1<1:
        canvas.move(cerc,0,10)
    else:
        canvas.move(cerc,-10,0)
    root.after(1000,move)

root = tk.Tk()
root.geometry("900x900")


canvas = tk.Canvas(root,  bg="DodgerBlue3")

cerc=canvas.create_oval(200,200,300,300,fill="white")


canvas.pack(fill="both",expand=True)

move()


root.mainloop()
