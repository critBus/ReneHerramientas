from datos.datos import *
from datos.plantillas import *
from datos.datosComplejos import *
from datos.datos_internos import *
from datos.funcionesCreadoras import *
from typing import TYPE_CHECKING, Dict, List, NoReturn, Optional, Union, Tuple, cast, ClassVar


def procesar_lineas(texto, funcion):
    lineas = texto.split('\n')
    for i, linea in enumerate(lineas):
        funcion(i, linea)

def procesar_string(dato):
    kv=datos_internos
    for key in kv:
        valor=kv[key]
        dato = dato.replace("{- " + key + " -}", valor)
    return dato

def procesar_dic(dic):
    for clave, valor in dic.items():
        if isinstance(valor, dict):
            procesar_dic(valor)
        elif isinstance(valor, list):
            for i in range(len(valor)):
                if isinstance(valor[i], dict):
                    procesar_dic(valor[i])
                elif isinstance(valor[i], str):
                    # Procesar el string aquí
                    valor[i] = procesar_string(valor[i])
        elif isinstance(valor, str):
            # Procesar el string aquí
            dic[clave] = procesar_string(valor)
procesar_dic(key_valores)

lista_DC:List[DatosModelo]=[]
dic_DC:Dict[str,DatosModelo]={}

for key in key_valores['models']:
    key_valores_actual=key_valores['models'][key].copy()
    key_valores_actual['modelo']=key
    D = DatosModelo(key_valores_actual)
    lista_DC.append(D)
    dic_DC[key]=D

for D in lista_DC:
    for campo in D.listaCampos:
        if campo.esMany or campo.esLlave or campo.esExtraReferencia:
            campo.modeloReferencia=dic_DC[campo.nombreModeloReferencia]
        if campo.nombreCampo in key_valores['descripcionesAutomaticas']:
            campo.descripcion_entrada=key_valores['descripcionesAutomaticas'][campo.nombreCampo]
        if campo.descripcion_salida=="":
            campo.descripcion_salida=campo.descripcion_entrada

def imprimir_linea(kv,i,linea):
    for key in kv:
        valor=kv[key]
        linea = linea.replace("{" + key + "}", valor)

    print(linea)



listAPintar=[plantillas_filtros]#[plantilla_doc_parametros_list]#[plantilla_viewset_own]#[plantilla_doc]#[g]#[plantilla_views]#[plantilla_serializer_imagen]#[plantilla_viewSets]#[plantilla_doc]#[plantilla_serializer]#[f]
def aplicar(key, key_valores):
    key_valores_actual = key_valores['models'][key].copy()
    key_valores_actual['modelo'] = key
    crearAtributosNuevos(key_valores_actual, dic_DC[key])
    key_valores_actual.pop("campos")

    key_valores_actual.pop("codigos")
    procesar_lineas(texto, lambda i, linea: imprimir_linea(key_valores_actual, i, linea))

modelos_seleccionados=[]#['CardContact']#['Contact']

for texto in listAPintar:
    if len(modelos_seleccionados)==0:
        for key in key_valores['models']:
            aplicar(key,key_valores)
    else:
        for key in modelos_seleccionados:
            aplicar(key, key_valores)



# for key_valores_actual in list_key_valores:
#     procesar_lineas(b,lambda i,linea:imprimir_linea(key_valores_actual,i,linea))