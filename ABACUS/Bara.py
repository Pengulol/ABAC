from Bila import Bila


class Bara:
    def __init__(self, canvas, X1, X2, Y1, Y2, nrBara):
        self.X1 = X1
        self.X2 = X2
        self.centerline = (Y1 + Y2) / 2
        self.numarbara = nrBara
        canvas.create_rectangle(X1, Y1, X2, Y2, fill="#ADADAD")
        self.VectorBile = []
        X = X1
        Y = (Y1 + Y2) / 2 - 35
        for z in range(0, 10):

            a = Bila(canvas, X, Y, nrBara, z)
            X = X + 70
            self.VectorBile.append(a)

    def recolorBara(self):
        for x in range(0, 10):
            self.VectorBile[x].changeColor()


    def addOneBall(self):
        for x in range(0, 10, +1):

            if x == 9:
                self.VectorBile[9].moveToRight()

                return
            if self.VectorBile[x].isMoved is True:
                return

            if self.VectorBile[x + 1].isMoved is True:
                self.VectorBile[x].moveToRight()
                return

    def isEmpty(self):
        return not self.VectorBile[9].isMoved

    def isFilled(self):
        return self.VectorBile[0].isMoved

    def numberOfMovedBalls(self):
        nr = 0
        for x in range(0, 10):
            if self.VectorBile[x].isMoved:
                nr = nr + 1
        return nr

    def removeOneBall(self):
        for x in range(9, -1, -1):
            if x == 0:
                self.moveBalls(0)

                return
            if not self.VectorBile[x].isMoved:
                return
            if not self.VectorBile[x - 1].isMoved:
                self.VectorBile[x].moveToLeft()

                return

    def moveBalls(self, pozBilaStart):

        if self.VectorBile[pozBilaStart].isMoved:
            for x in range(pozBilaStart, -1, -1):
                if self.VectorBile[x].isMoved:
                    self.VectorBile[x].moveToLeft()


        else:
            for x in range(pozBilaStart, 10, +1):
                if not self.VectorBile[x].isMoved:
                    self.VectorBile[x].moveToRight()


    def makeTransportLastMovedBall(self):
        x = int(0)
        while x < 10 and not self.VectorBile[x].isMoved:
            x = x+1
        if x != 10:
            self.VectorBile[x].isTransport = True
            self.VectorBile[x].changeColor()
    def makeTransportLastUnMovedBall(self):
        x = int(-1)
        while x < 9 and not self.VectorBile[x+1].isMoved:
            x = x+1


        self.VectorBile[x].isTransport = True
        self.VectorBile[x].changeColor()

