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

from .datosComplejos import *

con_postgres = True


def crearParametrosPostCrear(D: DatosModelo):
    p = Imprimidor(4)

    for d in D.listaCampos:
        if not d.esExtraReferencia:
            p.pr0("'" + d.nombreCampo + "' : '" + d.descripcion_entrada + "',")

    return p.r


dicFuncionesCreadoras["parametros_post_descripcion_crear"] = crearParametrosPostCrear

produndidadMaxima = 2


def crearParametrosGetFiltroLista(D: DatosModelo):
    p = Imprimidor(3)

    LD = [D]
    CD = [""]
    # for d in D.listaCampos:
    #     if d.esMany or d.esLlave or d.esExtraReferencia:
    #         LD.append(d.modeloReferencia)
    #         CD.append(d.nombreCampo)

    def agregarCampos(nombreCampo, modelo, nivel, prefijo):
        if nombreCampo in saltar_campos:  # modelo.nombreModelo==D.nombreModelo or
            return
        prefijo = prefijo + nombreCampo + "__" if nivel != 0 else ""  # i != 0 else ""
        for d in modelo.listaCampos:
            if d.nombreCampo in saltar_campos:
                continue
            if (
                d.esTexto
                or d.esNumero
                or d.esBoolean
                or d.esID
                or d.esDate
                or d.esLlave
            ):
                parametros = []
                if d.esTexto:
                    parametros = ["contains", "exact", "icontains"]
                    if con_postgres:
                        parametros += ["search"]
                    # p.pr0("'" + prefijo + d.nombreCampo + "' : " + str(parametros) + ",")
                elif d.esNumero or d.esDate:
                    parametros = ["gte", "lte", "gt", "lt", "exact"]
                    # p.pr0("'" + prefijo + d.nombreCampo + "' : ['gte', 'lte','gt', 'lt','exact'],")
                elif d.esBoolean:
                    parametros = ["exact"]
                    # p.pr0("'" + prefijo + d.nombreCampo + "' : ['exact'],")
                elif d.esID:
                    parametros = ["exact"]
                    # p.pr0("'" + prefijo + d.nombreCampo + "' : ['exact'],")
                elif d.esLlave:
                    parametros = ["isnull"]

                for pa in parametros:
                    extra = "__" + pa if pa != "exact" else ""
                    descripcion = ""
                    if pa == "exact":
                        descripcion = (
                            "que coincidan exactamente con el valor proporcionado"
                        )
                    elif pa == "contains":
                        descripcion = "que contengan el valor proporcionado"
                    elif pa == "icontains":
                        descripcion = "que contengan el valor proporcionado ignorando mayusculas y minusculas"
                    elif pa == "search":
                        descripcion = "se realiza una búsqueda de texto completo básica en el campo especificado. Esto significa que se buscarán todas las instancias que contengan al menos una palabra que coincida parcial o completamente con el término de búsqueda proporcionado. No se tienen en cuenta las diferencias de mayúsculas y minúsculas, ni las tildes"
                    elif pa == "gte":
                        descripcion = (
                            "que sean mayores o igual que el valor proporcionado"
                        )
                    elif pa == "lte":
                        descripcion = (
                            "que sean menores o igual que el valor proporcionado"
                        )
                    elif pa == "gt":
                        descripcion = "que sean mayores que el valor proporcionado"
                    elif pa == "lt":
                        descripcion = "que sean menores que el valor proporcionado"
                    elif pa == "isnull":
                        descripcion = "que sean nulos"
                    p.pr1(
                        "- '"
                        + prefijo
                        + d.nombreCampo
                        + extra
                        + "' : '"
                        + descripcion
                        + "',"
                    )

            if nivel < produndidadMaxima and (
                d.esMany or d.esLlave or (d.esExtraReferencia and d.related_name)
            ):
                if (
                    d.nombreCampo != nombreCampo
                    and d.modeloReferencia.nombreModelo != D.nombreModelo
                ):
                    prefijo = nombreCampo + "__" if nivel > 0 else ""
                    agregarCampos(
                        d.nombreCampo, d.modeloReferencia, nivel + 1, prefijo
                    )  # "nombreCampo+"__""

    agregarCampos(CD[0], LD[0], 0, "")

    return p.r


dicFuncionesCreadoras["paremetros_get_filtro_lista"] = crearParametrosGetFiltroLista


def crearParametrosGetOrdenamientoLista(D: DatosModelo):
    p = Imprimidor(4)
    p.pr0("- 'pk': 'Ordena por su clave primaria (id)',")
    if D.hayUnCampoTexto or D.hayUnCampoNumero or D.hayUnCampoDate:
        for d in D.listaCampos:
            if d.esTexto or d.esNumero or d.esDate:
                descripcion = ""
                if d.esTexto:
                    descripcion = "Ordena alfabéticamente por el " + d.nombreCampo
                elif d.esNumero:
                    descripcion = (
                        "Ordena de forma asendente o desendente por el " + d.nombreCampo
                    )
                elif d.esDate:
                    descripcion = (
                        "Ordena de forma cronológica asendente o desendente por la "
                        + d.nombreCampo
                    )
                p.pr0("- '" + d.nombreCampo + "' : '" + descripcion + "',")
    return p.r


dicFuncionesCreadoras["paremetros_get_ordenamiento_lista"] = (
    crearParametrosGetOrdenamientoLista
)


def crearParametrosGetBusquedaLista(D: DatosModelo):
    p = Imprimidor(4)
    if D.hayUnCampoTexto or D.hayUnCampoNumero:
        for d in D.listaCampos:
            if d.esTexto or d.esNumero:
                p.pr0("- '" + d.nombreCampo + "',")
    return p.r


dicFuncionesCreadoras["paremetros_get_search_lista"] = crearParametrosGetBusquedaLista


def crearAtributosExtras(D):
    p = Imprimidor(1)
    LD = [D]
    CD = [""]
    #    LNombreRelacion=[None]
    for d in D.listaCampos:
        if d.esMany or d.esLlave or (d.esExtraReferencia and d.related_name):
            LD.append(d.modeloReferencia)
            CD.append(d.nombreCampo)
    p.pr0("filterset_fields = {")

    def agregarCampos(nombreCampo, modelo, nivel, prefijo):
        if nombreCampo in saltar_campos:  # modelo.nombreModelo==D.nombreModelo or
            return
        prefijo = prefijo + nombreCampo + "__" if nivel != 0 else ""  # i != 0 else ""
        for d in modelo.listaCampos:
            if d.nombreCampo in saltar_campos:
                continue
            if (
                d.esTexto
                or d.esNumero
                or d.esBoolean
                or d.esID
                or d.esDate
                or d.esLlave
            ):
                parametros = []
                if d.esTexto:
                    parametros = ["contains", "exact", "icontains"]
                    if con_postgres:
                        parametros += ["search"]
                    p.pr0(
                        "'" + prefijo + d.nombreCampo + "' : " + str(parametros) + ","
                    )
                elif d.esNumero or d.esDate:
                    parametros = ["gte", "lte", "gt", "lt", "exact"]
                    p.pr0(
                        "'"
                        + prefijo
                        + d.nombreCampo
                        + "' : ['gte', 'lte','gt', 'lt','exact'],"
                    )
                elif d.esBoolean:
                    parametros = ["exact"]
                    p.pr0("'" + prefijo + d.nombreCampo + "' : ['exact'],")
                elif d.esID:
                    parametros = ["exact"]
                    p.pr0("'" + prefijo + d.nombreCampo + "' : ['exact'],")
                elif d.esLlave:
                    parametros = ["isnull"]
                    p.pr0("'" + prefijo + d.nombreCampo + "' : ['isnull'],")

            if nivel < produndidadMaxima and (
                d.esMany or d.esLlave or (d.esExtraReferencia and d.related_name)
            ):
                if (
                    d.nombreCampo != nombreCampo
                    and d.modeloReferencia.nombreModelo != D.nombreModelo
                ):
                    prefijo = nombreCampo + "__" if nivel > 0 else ""
                    agregarCampos(
                        d.nombreCampo, d.modeloReferencia, nivel + 1, prefijo
                    )  # "nombreCampo+"__""

    agregarCampos(CD[0], LD[0], 0, "")

    p.pr0("}")

    if D.hayUnCampoTexto or D.hayUnCampoNumero:
        p.pr0("search_fields=[")
        for d in D.listaCampos:
            if d.nombreCampo in saltar_campos:
                continue
            if d.esTexto or d.esNumero:
                p.pr("'" + d.nombreCampo + "' ,")
        p.pr("]")

    if D.hayUnCampoTexto or D.hayUnCampoNumero or D.hayUnCampoDate:
        p.pr0("ordering_fields=['pk' ,")
        for d in D.listaCampos:
            if d.nombreCampo in saltar_campos:
                continue
            if d.esTexto or d.esNumero or d.esDate:
                p.pr("'" + d.nombreCampo + "' ,")
        p.pr("]")
    # if D.nombreModelo == "User":
    #     print("aqui")
    p.pr0("ordering = ['")
    d = None
    if D.hayUnCampoDate:
        d = D.primerCampoDate
    elif D.hayUnCampoTexto:
        d = D.primerCampoTexto
    elif D.hayUnCampoNumero:
        d = D.primerCampoNumero

    if d:
        p.pr(d.nombreCampo + "']")
    else:
        p.pr("pk']")
    p.pr1("")
    return p.r


dicFuncionesCreadoras["atributosExtra"] = crearAtributosExtras


def crearParametrosSalida_Get_RUD(D: DatosModelo):
    p = Imprimidor(4)

    for d in D.listaCampos:
        if not d.esExtraReferencia:
            p.pr0("'" + d.nombreCampo + "' : '" + d.descripcion_salida + "',")

    return p.r


dicFuncionesCreadoras["parametros_salida_get_RUD"] = crearParametrosSalida_Get_RUD


def crearParametrosEntrada_Put_RUD(D: DatosModelo):
    p = Imprimidor(4)

    for d in D.listaCampos:
        if not d.esExtraReferencia:
            p.pr0("'" + d.nombreCampo + "' : '" + d.descripcion_entrada + "',")

    return p.r


dicFuncionesCreadoras["parametros_entrada_put_RUD"] = crearParametrosEntrada_Put_RUD


def crearParametrosSalida_Put_RUD(D: DatosModelo):
    p = Imprimidor(4)

    for d in D.listaCampos:
        if not d.esExtraReferencia:
            p.pr0("'" + d.nombreCampo + "' : '" + d.descripcion_salida + "',")

    return p.r


dicFuncionesCreadoras["parametros_salida_put_RUD"] = crearParametrosSalida_Put_RUD


def crearParametrosSalida_Get_elemento_lista(D: DatosModelo):
    p = Imprimidor(4)

    for d in D.listaCampos:
        if not d.esExtraReferencia:
            p.pr0("'" + d.nombreCampo + "' : '" + d.descripcion_salida + "',")

    return p.r


dicFuncionesCreadoras["parametros_salida_get_elmento_lista"] = (
    crearParametrosSalida_Get_elemento_lista
)


def crearParametrosSalida_Post_crear_lista(D: DatosModelo):
    p = Imprimidor(4)

    for d in D.listaCampos:
        if not d.esExtraReferencia:
            p.pr0("'" + d.nombreCampo + "' : '" + d.descripcion_salida + "',")

    return p.r


dicFuncionesCreadoras["parametros_salida_post_descripcion_crear"] = (
    crearParametrosSalida_Post_crear_lista
)

SEPARACION_PERMISOS = 1


def crear_Permisos_List(D: DatosModelo):
    p = Imprimidor(SEPARACION_PERMISOS)
    p.pr(D.datosEnpoint.list.permiso.codigo)
    return p.r


dicFuncionesCreadoras["permisos_list"] = crear_Permisos_List


def crear_Permisos_Create(D: DatosModelo):
    p = Imprimidor(SEPARACION_PERMISOS)
    p.pr(D.datosEnpoint.create.permiso.codigo)
    return p.r


dicFuncionesCreadoras["permisos_create"] = crear_Permisos_Create


def crear_Permisos_Retrieve(D: DatosModelo):
    p = Imprimidor(SEPARACION_PERMISOS)
    p.pr(D.datosEnpoint.retrive.permiso.codigo)
    return p.r


dicFuncionesCreadoras["permisos_retrieve"] = crear_Permisos_Retrieve


def crear_Permisos_Delete(D: DatosModelo):
    p = Imprimidor(SEPARACION_PERMISOS)
    p.pr(D.datosEnpoint.delete.permiso.codigo)
    return p.r


dicFuncionesCreadoras["permisos_destroy"] = crear_Permisos_Delete


def crear_Permisos_Update(D: DatosModelo):
    p = Imprimidor(SEPARACION_PERMISOS)
    p.pr(D.datosEnpoint.update.permiso.codigo)
    return p.r


dicFuncionesCreadoras["permisos_update"] = crear_Permisos_Update

# -----------------------------------------

SEPARACION_PERMISOS_DESCRIPCION = 2


def crear_Permisos_descripcion_List(D: DatosModelo):
    p = Imprimidor(SEPARACION_PERMISOS_DESCRIPCION)
    permiso_str = D.datosEnpoint.list.permiso.descripcion
    l = permiso_str.split("\n")
    for ps in l:
        p.pr0(ps)
    return p.r


dicFuncionesCreadoras["permisos_descripcion_list"] = crear_Permisos_descripcion_List


def crear_Permisos_descripcion_Create(D: DatosModelo):
    p = Imprimidor(SEPARACION_PERMISOS_DESCRIPCION)
    # p.pr0(D.datosEnpoint.create.permiso.descripcion)
    permiso_str = D.datosEnpoint.create.permiso.descripcion
    l = permiso_str.split("\n")
    for ps in l:
        p.pr0(ps)
    return p.r


dicFuncionesCreadoras["permisos_descripcion_create"] = crear_Permisos_descripcion_Create


def crear_Permisos_descripcion_Retrieve(D: DatosModelo):
    p = Imprimidor(SEPARACION_PERMISOS_DESCRIPCION)
    # p.pr0(D.datosEnpoint.retrive.permiso.descripcion)
    permiso_str = D.datosEnpoint.retrive.permiso.descripcion
    l = permiso_str.split("\n")
    for ps in l:
        p.pr0(ps)
    return p.r


dicFuncionesCreadoras["permisos_descripcion_retrieve"] = (
    crear_Permisos_descripcion_Retrieve
)


def crear_Permisos_descripcion_Delete(D: DatosModelo):
    p = Imprimidor(SEPARACION_PERMISOS_DESCRIPCION)
    # p.pr0(D.datosEnpoint.delete.permiso.descripcion)
    permiso_str = D.datosEnpoint.delete.permiso.descripcion
    l = permiso_str.split("\n")
    for ps in l:
        p.pr0(ps)
    return p.r


dicFuncionesCreadoras["permisos_descripcion_destroy"] = (
    crear_Permisos_descripcion_Delete
)


def crear_Permisos_descripcion_Update(D: DatosModelo):
    p = Imprimidor(SEPARACION_PERMISOS_DESCRIPCION)
    # p.pr0(D.datosEnpoint.update.permiso.descripcion)
    permiso_str = D.datosEnpoint.update.permiso.descripcion
    l = permiso_str.split("\n")
    for ps in l:
        p.pr0(ps)
    return p.r


dicFuncionesCreadoras["permisos_descripcion_update"] = crear_Permisos_descripcion_Update

# ----------------------------------------------------
SEPARACION_SAVE = 2


def crear_save_codigo_create(D: DatosModelo):
    c = D.datosEnpoint.create.pre_save
    if len(c) > 0:
        p = Imprimidor(SEPARACION_SAVE)
        p.pr0(c)
        return p.r
    return ""


dicFuncionesCreadoras["save_create"] = crear_save_codigo_create


def crear_save_codigo_Update(D: DatosModelo):
    c = D.datosEnpoint.update.pre_save
    if len(c) > 0:
        p = Imprimidor(SEPARACION_SAVE)
        p.pr0(c)
        return p.r
    return ""


dicFuncionesCreadoras["save_update"] = crear_save_codigo_Update


def crear_save_codigo_delete(D: DatosModelo):
    c = D.datosEnpoint.delete.pre_save
    if len(c) > 0:
        p = Imprimidor(SEPARACION_SAVE)
        p.pr0(c)
        return p.r
    return ""


dicFuncionesCreadoras["save_destroy"] = crear_save_codigo_delete


# ----------------------------------------
SEPARACION_SERIALIZER = 1


def crear_Serrializer_List(D: DatosModelo):
    p = Imprimidor(SEPARACION_SERIALIZER)
    p.pr(D.datosEnpoint.list.serializer)
    return p.r


dicFuncionesCreadoras["modeloSerializer_list"] = crear_Serrializer_List


def crear_Serrializer_Create(D: DatosModelo):
    p = Imprimidor(SEPARACION_SERIALIZER)
    p.pr(D.datosEnpoint.create.serializer)
    return p.r


dicFuncionesCreadoras["modeloSerializer_create"] = crear_Serrializer_Create


def crear_Serrializer_Retrieve(D: DatosModelo):
    p = Imprimidor(SEPARACION_SERIALIZER)
    p.pr(D.datosEnpoint.retrive.serializer)
    return p.r


dicFuncionesCreadoras["modeloSerializer_retrieve"] = crear_Serrializer_Retrieve


def crear_Serrializer_Delete(D: DatosModelo):
    p = Imprimidor(SEPARACION_SERIALIZER)
    p.pr(D.datosEnpoint.delete.serializer)
    return p.r


dicFuncionesCreadoras["modeloSerializer_destroy"] = crear_Serrializer_Delete


def crear_Serrializer_Update(D: DatosModelo):
    p = Imprimidor(SEPARACION_SERIALIZER)
    p.pr(D.datosEnpoint.update.serializer)
    return p.r


dicFuncionesCreadoras["modeloSerializer_update"] = crear_Serrializer_Update


def crearParametrosSerializer(D: DatosModelo):
    p = Imprimidor(1)
    for d in D.listaCampos:
        if d.esLlave:
            p.pr0(
                ""
                + d.nombreCampo
                + "="
                + d.modeloReferencia.serializerDefault
                + "_Representation"
                + "()"
            )

    return p.r  # +"\n"


dicFuncionesCreadoras["parametrosSerializer"] = crearParametrosSerializer


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
