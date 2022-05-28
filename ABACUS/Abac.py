import tkinter as tk
from tkinter import *

class Abac:
    def __init__ (self, canvas):

        self.canvas = canvas

        canvas.create_rectangle(700, 100, 730, 950, fill = "#90453A")
        canvas.create_rectangle(1540, 100, 1570, 950, fill="#90453A")
        canvas.create_rectangle(730, 120, 1540, 130, fill="#ADADAD")
        canvas.create_rectangle(765, 120, 1540, 130, fill="#ADADAD")
