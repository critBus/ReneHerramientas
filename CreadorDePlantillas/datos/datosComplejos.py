


def getS(cant):
    se = "\n"
    for i in range(cant):
        se += "\t"
    return se

class Imprimidor:
    def __init__(self,separacion0):
        self.r=""
        self.separacion0=separacion0
        self.s0 = getS(self.separacion0)
        self.s1 = getS(self.separacion0 + 1)
        self.s2 = getS(self.separacion0 + 2)
        self.s3 = getS(self.separacion0 + 3)
        self.s4 = getS(self.separacion0 + 4)
    
    

    
    

    def pr(self,texto):
        self.r += texto

    def pr0(self,texto):
        self.pr(self.s0 + str(texto))

    def pr1(self,texto):
        self.pr(self.s1 + str(texto))

    def pr2(self,texto):
        self.pr(self.s2 + str(texto))

    def pr3(self,texto):
        self.pr(self.s3 + str(texto))

    def pr4(self,texto):
        self.pr(self.s4 + str(texto))
dicFuncionesCreadoras={}
def crearAtributosNuevos(datosDeModelo):
    datosDeModeloOriginal=datosDeModelo.copy()
    for key in dicFuncionesCreadoras:
        datosDeModelo[key]=dicFuncionesCreadoras[key](datosDeModeloOriginal)

    

    