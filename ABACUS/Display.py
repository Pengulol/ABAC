import tkinter as tk

class Display:

    def __init__(self):
        self.root=tk.Tk()
        self.canvas=tk.Canvas(self.root,bg="DodgerBlue3")
        self.canvas.pack()

        self.root.mainloop()

