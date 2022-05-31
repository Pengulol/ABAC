from Bara import Bara


class Abac:

    def __init__(self, canvas):
        X1 = 730
        X2 = 1570
        Y = 140
        self.toggleImpartire = False
        self.toggleMouse = True

        self.canvas = canvas
        self.canvas.create_rectangle(X1 - 30, 100, X1, 1050, fill="#90453A")
        self.canvas.create_rectangle(X2, 100, X2 + 30, 1050, fill="#90453A")

        self.VectorBare = []
        for z in range(0, 10):
            a = Bara(canvas, X1, X2, Y, Y + 10, z)
            Y = Y + 90
            self.VectorBare.append(a)

        def onclick(event):
            if self.toggleMouse:

                x = event.x
                y = event.y
                for bara in self.VectorBare:
                    if bara.centerline + 35 > y > bara.centerline - 35 and bara.X2 > x > bara.X1:

                        for bila in bara.VectorBile:
                            if bila.X < x < bila.X + bila.diametru and bila.Y < y < bila.Y + bila.diametru:

                                self.toggleImpartire = False
                                bara.moveBalls(bila.nrBila)
                                bara.recolorBara()

                                break
                        break

        self.canvas.bind('<Button-1>', onclick)

    def setareNumarSus(self, numar):

        aux = numar
        teavaCurenta = 0
        while aux > 0:
            nrBile = aux % 10
            for x in range(0, nrBile, +1):
                self.VectorBare[teavaCurenta].addOneBall()
            aux = int(aux / 10)
            self.VectorBare[teavaCurenta].recolorBara()
            teavaCurenta = teavaCurenta + 1

    def setareNumarJos(self, numar):

        aux = numar
        teavaCurenta = 9
        while aux > 0:
            nrBile = aux % 10
            for x in range(0, nrBile, +1):
                self.VectorBare[teavaCurenta].addOneBall()
            aux = int(aux / 10)
            self.VectorBare[teavaCurenta].recolorBara()
            teavaCurenta = teavaCurenta - 1

    def repairAdunare(self):
        for numarBara in range(9, 0, -1):
            if self.VectorBare[numarBara].isFilled():
                for x in range(0, 10, + 1):
                    self.VectorBare[numarBara].removeOneBall()
                self.VectorBare[numarBara - 1].addOneBall()
                self.VectorBare[numarBara - 1].makeTransportLastMovedBall()
                self.lastTransportPlace = numarBara - 1




    def resetBara(self, numarBara):
        if self.VectorBare[numarBara].VectorBile[9].isMoved:
            self.VectorBare[numarBara].moveBalls(9)
            self.VectorBare[numarBara].recolorBara()

    def resetAbac(self):
        for bara in self.VectorBare:
            self.resetBara(bara.numarbara)
