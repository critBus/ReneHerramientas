"""
    filterset_fields = {
        'paginas': ['gte', 'lte'],
        'titulo': ['contains'],
        'editorial__nombre': ['contains']
    }
    search_fields = ['titulo', 'editorial__nombre']
    ordering_fields = ['pk', 'titulo']
    ordering = ['pk']
"""
from typing import TYPE_CHECKING, Dict, List, NoReturn, Optional, Union, Tuple, cast, ClassVar
from .datosComplejos import *

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

        self.listaModelos:List[DatosDeCampo]=[]
        for campo in datosDeModelo["campos"]:
            d = DatosDeCampo(campo)
            if d.esID:
                continue
            self.listaModelos.append(d)
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



def crearAtributosExtras(datosDeModelo):
    p=Imprimidor(1)
    D = DatosModelo(datosDeModelo)

    if D.hayUnCampoTexto or D.hayUnCampoNumero or D.hayUnCampoBoolean:
        p.pr0("filterset_fields = {")

        for d in D.listaModelos:
            if d.esTexto:
                p.pr1("'"+d.nombreCampo+"' : ['contains','exact'],")
            elif d.esNumero:
                p.pr1("'"+d.nombreCampo + "' : ['gte', 'lte','exact'],")
            elif d.esBoolean:
                p.pr1("'"+d.nombreCampo+"' : ['contains','exact'],")
        p.pr0("}")
    if D.hayUnCampoTexto or D.hayUnCampoNumero:
        p.pr0("search_fields=[")
        for d in D.listaModelos:
            if d.esTexto or d.esNumero:
                p.pr("'"+d.nombreCampo+"' ,")
        p.pr("]")

        p.pr0("ordering_fields=['pk' ,")
        for d in D.listaModelos:
            if d.esTexto or d.esNumero:
                p.pr("'" + d.nombreCampo + "' ,")
        p.pr("]")
    p.pr0("ordering = ['")
    d=None
    if D.hayUnCampoDate:
        d=D.primerCampoDate
    elif D.hayUnCampoTexto:
        d=D.primerCampoTexto
    elif D.hayUnCampoNumero:
        d=D.primerCampoNumero


    if d:
        p.pr(d.nombreCampo+"']")
    else:
        p.pr("pk']")
    p.pr1("")
    return p.r

dicFuncionesCreadoras['atributosExtra']=crearAtributosExtras
