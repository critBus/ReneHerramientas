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

def crearParametrosPostCrear(D:DatosModelo):
    p=Imprimidor(4)

    for d in D.listaCampos:
        p.pr0("'" + d.nombreCampo + "' : '" + d.descripcion_entrada + "',")

    return p.r

dicFuncionesCreadoras['parametros_post_descripcion_crear']=crearParametrosPostCrear

def crearParametrosGetFiltroLista(D:DatosModelo):
    p=Imprimidor(3)

    LD = [D]
    CD = [""]
    for d in D.listaCampos:
        if d.esMany or d.esLlave:
            LD.append(d.modeloReferencia)
            CD.append(d.nombreCampo)

    for i, DD in enumerate(LD):
        prefijo = CD[i] + "__" if i != 0 else ""
        for d in DD.listaCampos:
            if d.esTexto or d.esNumero or d.esBoolean:
                parametros=[]
                if d.esTexto:
                    parametros=['contains','exact']
                    #p.pr0("'" + prefijo + d.nombreCampo + "' : ['contains','exact'],")
                elif d.esNumero:
                    parametros = ['gte', 'lte','exact']
                    #p.pr0("'" + prefijo + d.nombreCampo + "' : ['gte', 'lte','exact'],")
                elif d.esBoolean:
                    parametros = ['exact']
                    #p.pr0("'" + prefijo + d.nombreCampo + "' : ['exact'],")

                for pa in parametros:
                    extra="__"+pa if pa!='exact' else ""
                    descripcion=""
                    if pa == 'exact':
                        descripcion="que coincidan exactamente con el valor proporcionado"
                    elif pa == 'contains':
                        descripcion="que contengan el valor proporcionado"
                    elif pa == 'gte':
                        descripcion="que sean mayores o igual que el valor proporcionado"
                    elif pa == 'lte':
                        descripcion="que sean menores o igual que el valor proporcionado"
                    p.pr1("- '" + prefijo + d.nombreCampo+extra + "' : '"+descripcion+"',")

    return p.r

dicFuncionesCreadoras['paremetros_get_filtro_lista']=crearParametrosGetFiltroLista

def crearParametrosGetOrdenamientoLista(D:DatosModelo):
    p=Imprimidor(4)
    p.pr0("- 'pk': 'Ordena por su clave primaria (id)',")
    if D.hayUnCampoTexto or D.hayUnCampoNumero:

        for d in D.listaCampos:
            if d.esTexto or d.esNumero:
                if d.esTexto:
                    descripcion = "Ordena alfabéticamente por el "+d.nombreCampo
                else:
                    descripcion = "Ordena de forma asendente o desendente por el "+d.nombreCampo
                p.pr0("- '" +  d.nombreCampo + "' : '" + descripcion + "',")
    return p.r
dicFuncionesCreadoras['paremetros_get_ordenamiento_lista']=crearParametrosGetOrdenamientoLista


def crearParametrosGetBusquedaLista(D:DatosModelo):
    p=Imprimidor(4)
    if D.hayUnCampoTexto or D.hayUnCampoNumero:

        for d in D.listaCampos:
            if d.esTexto or d.esNumero:
                p.pr0("- '" +  d.nombreCampo + "',")
    return p.r
dicFuncionesCreadoras['paremetros_get_search_lista']=crearParametrosGetBusquedaLista

def crearAtributosExtras(D):
    p=Imprimidor(1)
    #D = DatosModelo(datosDeModelo)
    LD=[D]
    CD=[""]
    for d in D.listaCampos:
        if d.esMany or d.esLlave:
            LD.append(d.modeloReferencia)
            CD.append(d.nombreCampo)

    if D.hayUnCampoTexto or D.hayUnCampoNumero or D.hayUnCampoBoolean:
        p.pr0("filterset_fields = {")
        for i,DD in enumerate(LD):
            prefijo= CD[i]+"__" if i!=0 else ""
            for d in DD.listaCampos:
                if d.esTexto:
                    p.pr1("'"+prefijo + d.nombreCampo + "' : ['contains','exact'],")
                elif d.esNumero:
                    p.pr1("'" +prefijo + d.nombreCampo + "' : ['gte', 'lte','exact'],")
                elif d.esBoolean:
                    p.pr1("'" +prefijo + d.nombreCampo + "' : ['exact'],")#'contains',
        p.pr0("}")
    if D.hayUnCampoTexto or D.hayUnCampoNumero:
        p.pr0("search_fields=[")
        for i,DD in enumerate(LD):
            prefijo= CD[i]+"__" if i!=0 else ""
            for d in DD.listaCampos:
                if d.esTexto or d.esNumero:
                    p.pr("'"+prefijo + d.nombreCampo + "' ,")
        p.pr("]")

        p.pr0("ordering_fields=['pk' ,")
        for d in D.listaCampos:
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
        p.pr(d.nombreCampo + "']")
    else:
        p.pr("pk']")
    p.pr1("")
    return p.r

dicFuncionesCreadoras['atributosExtra']=crearAtributosExtras


def crearParametrosSalida_Get_RUD(D: DatosModelo):
    p = Imprimidor(4)

    for d in D.listaCampos:
        p.pr0("'" + d.nombreCampo + "' : '" + d.descripcion_salida + "',")

    return p.r
dicFuncionesCreadoras['parametros_salida_get_RUD']=crearParametrosSalida_Get_RUD

def crearParametrosEntrada_Put_RUD(D: DatosModelo):
    p = Imprimidor(4)

    for d in D.listaCampos:
        p.pr0("'" + d.nombreCampo + "' : '" + d.descripcion_entrada + "',")

    return p.r
dicFuncionesCreadoras['parametros_entrada_put_RUD']=crearParametrosEntrada_Put_RUD

def crearParametrosSalida_Put_RUD(D: DatosModelo):
    p = Imprimidor(4)

    for d in D.listaCampos:
        p.pr0("'" + d.nombreCampo + "' : '" + d.descripcion_salida + "',")

    return p.r
dicFuncionesCreadoras['parametros_salida_put_RUD']=crearParametrosSalida_Put_RUD

def crearParametrosSalida_Get_elemento_lista(D: DatosModelo):
    p = Imprimidor(4)

    for d in D.listaCampos:
        p.pr0("'" + d.nombreCampo + "' : '" + d.descripcion_salida + "',")

    return p.r
dicFuncionesCreadoras['parametros_salida_get_elmento_lista']=crearParametrosSalida_Get_elemento_lista

def crearParametrosSalida_Post_crear_lista(D: DatosModelo):
    p = Imprimidor(4)

    for d in D.listaCampos:
        p.pr0("'" + d.nombreCampo + "' : '" + d.descripcion_salida + "',")

    return p.r
dicFuncionesCreadoras['parametros_salida_post_descripcion_crear']=crearParametrosSalida_Post_crear_lista

SEPARACION_PERMISOS=1

def crear_Permisos_List(D:DatosModelo):
    p=Imprimidor(SEPARACION_PERMISOS)
    p.pr0(D.datosEnpoint.list.permiso.codigo)
    return p.r
dicFuncionesCreadoras['permisos_list']=crear_Permisos_List
def crear_Permisos_Create(D:DatosModelo):
    p=Imprimidor(SEPARACION_PERMISOS)
    p.pr0(D.datosEnpoint.create.permiso.codigo)
    return p.r
dicFuncionesCreadoras['permisos_create']=crear_Permisos_Create
def crear_Permisos_Retrieve(D:DatosModelo):
    p=Imprimidor(SEPARACION_PERMISOS)
    p.pr0(D.datosEnpoint.retrive.permiso.codigo)
    return p.r
dicFuncionesCreadoras['permisos_retrieve']=crear_Permisos_Retrieve
def crear_Permisos_Delete(D:DatosModelo):
    p=Imprimidor(SEPARACION_PERMISOS)
    p.pr0(D.datosEnpoint.delete.permiso.codigo)
    return p.r
dicFuncionesCreadoras['permisos_destroy']=crear_Permisos_Delete
def crear_Permisos_Update(D:DatosModelo):
    p=Imprimidor(SEPARACION_PERMISOS)
    p.pr0(D.datosEnpoint.update.permiso.codigo)
    return p.r
dicFuncionesCreadoras['permisos_update']=crear_Permisos_Update

#-----------------------------------------

SEPARACION_PERMISOS_DESCRIPCION=2

def crear_Permisos_descripcion_List(D:DatosModelo):
    p=Imprimidor(SEPARACION_PERMISOS_DESCRIPCION)
    p.pr0(D.datosEnpoint.list.permiso.descripcion)
    return p.r
dicFuncionesCreadoras['permisos_descripcion_list']=crear_Permisos_descripcion_List
def crear_Permisos_descripcion_Create(D:DatosModelo):
    p=Imprimidor(SEPARACION_PERMISOS_DESCRIPCION)
    p.pr0(D.datosEnpoint.create.permiso.descripcion)
    return p.r
dicFuncionesCreadoras['permisos_descripcion_create']=crear_Permisos_descripcion_Create
def crear_Permisos_descripcion_Retrieve(D:DatosModelo):
    p=Imprimidor(SEPARACION_PERMISOS_DESCRIPCION)
    p.pr0(D.datosEnpoint.retrive.permiso.descripcion)
    return p.r
dicFuncionesCreadoras['permisos_descripcion_retrieve']=crear_Permisos_descripcion_Retrieve
def crear_Permisos_descripcion_Delete(D:DatosModelo):
    p=Imprimidor(SEPARACION_PERMISOS_DESCRIPCION)
    p.pr0(D.datosEnpoint.delete.permiso.descripcion)
    return p.r
dicFuncionesCreadoras['permisos_descripcion_destroy']=crear_Permisos_descripcion_Delete
def crear_Permisos_descripcion_Update(D:DatosModelo):
    p=Imprimidor(SEPARACION_PERMISOS_DESCRIPCION)
    p.pr0(D.datosEnpoint.update.permiso.descripcion)
    return p.r
dicFuncionesCreadoras['permisos_descripcion_update']=crear_Permisos_descripcion_Update

dicFuncionesCreadoras['save_create']=lambda a:""
dicFuncionesCreadoras['save_update']=lambda a:""
dicFuncionesCreadoras['save_destroy']=lambda a:""

# def saltoExtra(d):
#     p = Imprimidor(1)
#     p.pr1("")
#     return p.r
# dicFuncionesCreadoras['se']=saltoExtra
#
# def saltoExtra0(d):
#     p = Imprimidor(1)
#     p.pr0("")
#     return p.r
# dicFuncionesCreadoras['se0']=saltoExtra
#
# def saltoExtra2(d):
#     p = Imprimidor(1)
#     p.pr2("")
#     return p.r
# dicFuncionesCreadoras['se2']=saltoExtra