from datos.datos import *
from datos.plantillas import *
from datos.datosComplejos import *
from datos.funcionesCreadoras import *
from typing import TYPE_CHECKING, Dict, List, NoReturn, Optional, Union, Tuple, cast, ClassVar


def procesar_lineas(texto, funcion):
    lineas = texto.split('\n')
    for i, linea in enumerate(lineas):
        funcion(i, linea)



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
        if campo.esMany or campo.esLlave:
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



listAPintar=[g]
for texto in listAPintar:
    for key in key_valores['models']:
        key_valores_actual=key_valores['models'][key].copy()
        key_valores_actual['modelo']=key
        crearAtributosNuevos(key_valores_actual,dic_DC[key])
        key_valores_actual.pop("campos")

        key_valores_actual.pop("codigos")
        procesar_lineas(texto,lambda i,linea:imprimir_linea(key_valores_actual,i,linea))



# for key_valores_actual in list_key_valores:
#     procesar_lineas(b,lambda i,linea:imprimir_linea(key_valores_actual,i,linea))