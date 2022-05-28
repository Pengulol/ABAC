import tkinter as tk
from tkinter import *
class Bila:
    def __init__(self, canvas, x, y):
        self.bila=canvas.create_oval(x,y,x+70,y+70,fill="Red")



