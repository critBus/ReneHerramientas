from datos.datos import *
from datos.plantillas import *
from datos.datosComplejos import *
from datos.funcionesCreadoras import *

def procesar_lineas(texto, funcion):
    lineas = texto.split('\n')
    for i, linea in enumerate(lineas):
        funcion(i, linea)





# for modelo in key_valores["modelo"]:
#     key_valores["modeloLower"].append(modelo.lower())

def imprimir_linea(kv,i,linea):
    for key in kv:
        valor=kv[key]
        linea = linea.replace("{" + key + "}", valor)
        # for valor in valores:
        #     linea=linea.replace("{"+key+"}",valor)
    print(linea)

# list_key_valores=[]
# for key in key_valores['models']:
#     valores=key_valores[key]
#     for i,valor in enumerate(valores):
#         if len(list_key_valores)==i:
#             list_key_valores.append({})
#         list_key_valores[i][key]=valor

listAPintar=[e]
for texto in listAPintar:
    for key in key_valores['models']:
        key_valores_actual=key_valores['models'][key].copy()
        key_valores_actual['modelo']=key
        crearAtributosNuevos(key_valores_actual)
        key_valores_actual.pop("campos")
        procesar_lineas(texto,lambda i,linea:imprimir_linea(key_valores_actual,i,linea))



# for key_valores_actual in list_key_valores:
#     procesar_lineas(b,lambda i,linea:imprimir_linea(key_valores_actual,i,linea))