import tkinter as tk

class Bila:

    def __init__(self, canvas):
        self.canvas=tk.Canvas

    def move():
        side = canvas.bbox(cerc)
        x1, y1, x2, y2 = side
        if x1 < 1:
            canvas.move(cerc, 0, 10)
        else:
            canvas.move(cerc, -10, 0)

    cerc = canvas.create_oval(200, 200, 300, 300, fill="white")