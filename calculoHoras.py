def sumar_tiempos(tiempos):
    total_minutos = 0
    
    # Sumar todas las horas y minutos
    for horas, minutos in tiempos:
        total_minutos += horas * 60 + minutos
    
    # Convertir total de minutos a horas y minutos
    horas_totales = total_minutos // 60
    minutos_totales = total_minutos % 60
    
    return (horas_totales, minutos_totales)

# Ejemplo de uso
lista_tiempos = [
(1, 00), 
(0, 10), 
(0, 30), 
(1, 00),
(1, 00),

 (0,30),# - Separate GroupRouteCreateSerializer from GroupRouteSerializer (backend)
 (0,10),# - add loader to create role (backend)
 (1,00),# - Implement menu control according to RBAC (pzMenu) (frontend)
 (1,30),# - add frontend_menu_allowed_of_user_view (backend)
 (0,30),# - add getFrontendMenusOfUser service in rbac (frontend)
 (0,30),# - fix TestCreateGroup (backend)
 (0,30),# - fix TestUpdateGroup (backend)
 (0,30),# - fix TestListGroup (backend)
 (0,30),# - fix TestDeleteGroup (backend)
 (0,30),#- fix TestRetrieveGroup (backend)
 (0,30),# - add TestGroupsNames (backend)
]  # Lista de tuplas (horas, minutos)
resultado = sumar_tiempos(lista_tiempos)

print(f"Suma total: {resultado[0]} horas y {resultado[1]} minutos")


# data={
# 	"a":"c",
# 	"b":"d"
# }

# def asd(a,b,c):
# 	print(f"{a} {b} {c}")
# asd(**data,c="e")
# # import base64

# # number = 41070
# # byte_array = number.to_bytes(2, 'big')  # Convertimos a 2 bytes
# # base64_encoded = base64.b64encode(byte_array)
# # print(base64_encoded)  # Muestra el resultado
# def fun(x,y):
# 	if x==0:
# 		return y
# 	return fun(x-1,x+y)

# # print(fun(4,3))

# def fun3(n):
# 	if n==0 or n==1:
# 		return n
# 	if n%3!=0:
# 		return 0
# 	return fun3(n/3)

# print(fun3(9))
# print(fun3(10))
# print(fun3(11))
# print(fun3(1))
# print(fun3(3))