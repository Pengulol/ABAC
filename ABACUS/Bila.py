class Bila:
    diametru = 70

    def __init__(self, canvas, X, Y, nrBara, nrBila):
        self.nrBila = nrBila
        self.nrBara = nrBara
        self.canvas = canvas
        self.X = X
        self.Y = Y
        self.isMoved = False
        self.isTransport=False
        self.bila = canvas.create_oval(self.X, self.Y, self.X + self.diametru, self.Y + self.diametru, fill="Red")


    def changeColor(self):

        if self.isTransport:
            self.canvas.itemconfig(self.bila, fill="Green")
            self.isTransport = False
        elif self.isMoved:
            self.canvas.itemconfig(self.bila, fill="Yellow")
        else:
            self.canvas.itemconfig(self.bila, fill="Red")

    def moveToRight(self):
        self.canvas.move(self.bila, 2 * self.diametru, 0)
        self.X = self.X + 2 * self.diametru
        self.isMoved = True
        self.changeColor()


    def moveToLeft(self):
        self.canvas.move(self.bila, -2 * self.diametru, 0)
        self.X = self.X + -2 * self.diametru
        self.isMoved = False
        self.changeColor()
