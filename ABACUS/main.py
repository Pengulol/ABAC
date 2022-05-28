import tkinter as tk
from tkinter import *
from Menu import Menu
root = tk.Tk()
root.title("Abacus")
root.geometry("1920x1080")
root.attributes('-fullscreen', True)

menu = Menu(root)

root.mainloop()

def iesire(root):
    root.quit