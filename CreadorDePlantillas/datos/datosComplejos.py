from typing import TYPE_CHECKING, Dict, List, NoReturn, Optional, Union, Tuple, cast, ClassVar


class DatosDeCampo:
    def __init__(self,campo):
        self.tipo = campo["type"]
        self.nombreCampo = campo["name"]

        self.esID = self.nombreCampo == 'id'
        self.esNumero =not self.esID and (self.tipo == "BigAutoField" or self.tipo == "FloatField")
        self.esBoolean = self.tipo == "BooleanField"
        self.esTexto = self.tipo == "CharField"
        self.esLlave = self.tipo == "ForeignKey"
        self.esArchivo = self.tipo == "ImageField"
        self.esMany = self.tipo == 'ManyToManyField'


        self.nombreModeloReferencia = None
        if self.esMany or self.esLlave:
            self.nombreModeloReferencia =campo["related_model"]
        self.modeloReferencia=None
        #print(campo)
        self.descripcion_entrada=campo["descripcion_entrada"]
        self.descripcion_salida = campo["descripcion_salida"]



class DatosModelo:
    def __init__(self,datosDeModelo):
        self.hayUnCampoTexto = False
        self.hayUnCampoNumero = False
        self.hayUnCampoDate = False
        self.hayUnCampoBoolean = False
        self.primerCampoTexto = None
        self.primerCampoNumero = None
        self.primerCampoDate = None
        self.primerCampoBoolean = None

        self.listaCampos:List[DatosDeCampo]=[]
        for campo in datosDeModelo["campos"]:
            d = DatosDeCampo(campo)
            if d.esID:
                continue
            self.listaCampos.append(d)
            if d.esTexto:
                self.hayUnCampoTexto=True
                if not self.primerCampoTexto:
                    self.primerCampoTexto=d
            elif d.esNumero:
                self.hayUnCampoNumero = True
                if not self.primerCampoNumero:
                    self.primerCampoNumero = d
            if d.esBoolean:
                self.hayUnCampoBoolean = True
                if not self.primerCampoTexto:
                    self.primerCampoTexto = d

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
def crearAtributosNuevos(datosDeModelo,D:DatosModelo):#datosDeModelo
    datosDeModeloOriginal=datosDeModelo.copy()
    for key in dicFuncionesCreadoras:
        datosDeModelo[key]=dicFuncionesCreadoras[key](D)

    

    