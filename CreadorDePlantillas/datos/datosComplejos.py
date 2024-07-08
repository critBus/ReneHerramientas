from typing import (
    TYPE_CHECKING,
    ClassVar,
    Dict,
    List,
    NoReturn,
    Optional,
    Tuple,
    Union,
    cast,
)

saltar_campos = ["content_type", "password"]


class DatosDeCampo:
    def __init__(self, campo):
        self.tipo = campo["type"]
        self.nombreCampo = campo["name"]

        self.esID = self.nombreCampo == "id"
        self.esNumero = not self.esID and (
            self.tipo == "BigAutoField"
            or self.tipo == "FloatField"
            or self.tipo == "DecimalField"
            or self.tipo == "IntegerField"
        )
        self.esBoolean = self.tipo == "BooleanField"
        self.esTexto = self.tipo == "CharField" or self.tipo == "EmailField"
        self.esLlave = self.tipo == "ForeignKey"
        self.esArchivo = self.tipo == "ImageField"
        self.esMany = self.tipo == "ManyToManyField"
        self.esDate = self.tipo == "DateTimeField" or self.tipo == "DateField"
        self.esExtraReferencia = (
            self.tipo == "Extra_ManyToManyField" or self.tipo == "Extra_ForeignKey"
        )

        self.nombreModeloReferencia = None
        if self.esMany or self.esLlave or self.esExtraReferencia:
            self.nombreModeloReferencia = campo["related_model"]
        self.modeloReferencia = None
        # print(campo)
        self.descripcion_entrada = campo["descripcion_entrada"]
        self.descripcion_salida = campo["descripcion_salida"]
        self.related_name = campo["related_name"] if "related_name" in campo else None


class DatoCodigo:
    def __init__(self):
        self.codigo = ""
        self.descripcion = ""


class Codigos:
    def __init__(self):
        self.permiso = DatoCodigo()
        self.pre_save = DatoCodigo()
        self.serializer = ""

    def inicializar(self, D, dc_codigo):
        self.permiso.codigo = dc_codigo["permisos"]
        self.permiso.descripcion = dc_codigo["permisos_descripcion"]
        self.pre_save = dc_codigo["save"]
        if "serializer" in dc_codigo:
            sr = dc_codigo["serializer"]
            self.serializer = sr if len(sr) > 0 else D.serializerDefault
        else:
            self.serializer = D.serializerDefault


class DatosEnpoint:
    def __init__(self):
        self.list = Codigos()
        self.retrive = Codigos()
        self.create = Codigos()
        self.update = Codigos()
        self.delete = Codigos()


class DatosModelo:
    def __init__(self, datosDeModelo):
        self.hayUnCampoTexto = False
        self.hayUnCampoNumero = False
        self.hayUnCampoDate = False
        self.hayUnCampoBoolean = False
        self.primerCampoTexto = None
        self.primerCampoNumero = None
        self.primerCampoDate = None
        self.primerCampoBoolean = None

        self.nombreModelo = datosDeModelo["modelo"]
        self.serializerDefault = self.nombreModelo + "Serializer"

        self.datosEnpoint = DatosEnpoint()
        dc = datosDeModelo["codigos"]
        dc_codigo = dc["create"]
        self.datosEnpoint.create.inicializar(self, dc_codigo)
        dc_codigo = dc["destroy"]
        self.datosEnpoint.delete.inicializar(self, dc_codigo)
        dc_codigo = dc["edit"]
        self.datosEnpoint.update.inicializar(self, dc_codigo)
        dc_codigo = dc["list"]
        self.datosEnpoint.list.inicializar(self, dc_codigo)
        dc_codigo = dc["view"]
        self.datosEnpoint.retrive.inicializar(self, dc_codigo)

        self.listaCampos: List[DatosDeCampo] = []
        # self.listaCampos.append({
        #
        # })
        for campo in datosDeModelo["campos"]:
            d = DatosDeCampo(campo)

            # if d.esID:
            #     continue
            self.listaCampos.append(d)
            if d.nombreCampo in saltar_campos:
                continue
            if d.esTexto:
                self.hayUnCampoTexto = True
                if not self.primerCampoTexto:
                    self.primerCampoTexto = d
            elif d.esNumero:
                self.hayUnCampoNumero = True
                if not self.primerCampoNumero:
                    self.primerCampoNumero = d
            elif d.esBoolean:
                self.hayUnCampoBoolean = True
                if not self.primerCampoBoolean:
                    self.primerCampoBoolean = d
            elif d.esDate:
                self.hayUnCampoDate = True
                if not self.primerCampoDate:
                    self.primerCampoDate = d


def getS(cant):
    se = "\n"
    for i in range(cant):
        se += "\t"
    return se


class Imprimidor:
    def __init__(self, separacion0):
        self.r = ""
        self.separacion0 = separacion0
        self.s0 = getS(self.separacion0)
        self.s1 = getS(self.separacion0 + 1)
        self.s2 = getS(self.separacion0 + 2)
        self.s3 = getS(self.separacion0 + 3)
        self.s4 = getS(self.separacion0 + 4)

    def pr(self, texto):
        self.r += texto

    def pr0(self, texto):
        self.pr(self.s0 + str(texto))

    def pr1(self, texto):
        self.pr(self.s1 + str(texto))

    def pr2(self, texto):
        self.pr(self.s2 + str(texto))

    def pr3(self, texto):
        self.pr(self.s3 + str(texto))

    def pr4(self, texto):
        self.pr(self.s4 + str(texto))


dicFuncionesCreadoras = {}


def crearAtributosNuevos(datosDeModelo, D: DatosModelo):  # datosDeModelo
    datosDeModeloOriginal = datosDeModelo.copy()
    for key in dicFuncionesCreadoras:
        datosDeModelo[key] = dicFuncionesCreadoras[key](D)
