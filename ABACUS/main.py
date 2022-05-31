import tkinter as tk
from Menu import Menu

root = tk.Tk()
root.title("Abacus")
root.geometry("900x400")
root.attributes('-fullscreen', True)

menu = Menu(root)

root.mainloop()


def iesire(root):
    root.quit
