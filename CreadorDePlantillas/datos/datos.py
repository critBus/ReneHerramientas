# from .valoresDeDatos.datosNegocio import datos_negocio
# from .valoresDeDatos.datosVersiones import datos_versiones
# from .valoresDeDatos_Remesas.datos import datos_todo
# from .valoresDeDatos_2.datos2 import datos
from .valoresDeDatos.datos3 import datos

key_valores = datos


key_valores["attribute_types"] = [
    "BigAutoField",
    "ForeignKey",
    "CharField",
    "ImageField",
    "TextField",
    "ManyToManyField",
    "BooleanField",
    "FloatField",
]
key_valores["descripcionesAutomaticas"] = {"id": "id de la entidad en la base de datos"}

# "User": {
#             "campos": [
#                 {
#                     "name": "id",
#                     "type": "BigAutoField",
#                     "related_model": ""
#                 },
#                 {
#                     "name": "password",
#                     "type": "CharField",
#                     "related_model": ""
#                 },
#                 {
#                     "name": "last_login",
#                     "type": "DateTimeField",
#                     "related_model": ""
#                 },
#                 {
#                     "name": "is_superuser",
#                     "type": "BooleanField",
#                     "related_model": ""
#                 },
#                 {
#                     "name": "username",
#                     "type": "CharField",
#                     "related_model": ""
#                 },
#                 {
#                     "name": "email",
#                     "type": "EmailField",
#                     "related_model": ""
#                 },
#                 {
#                     "name": "first_name",
#                     "type": "CharField",
#                     "related_model": ""
#                 },
#                 {
#                     "name": "last_name",
#                     "type": "CharField",
#                     "related_model": ""
#                 },
#                 {
#                     "name": "image",
#                     "type": "ImageField",
#                     "related_model": ""
#                 },
#                 {
#                     "name": "phone",
#                     "type": "CharField",
#                     "related_model": ""
#                 },
#                 {
#                     "name": "is_active",
#                     "type": "BooleanField",
#                     "related_model": ""
#                 },
#                 {
#                     "name": "is_staff",
#                     "type": "BooleanField",
#                     "related_model": ""
#                 },
#                 {
#                     "name": "groups",
#                     "type": "ManyToManyField",
#                     "related_model": "Group"
#                 },
#                 {
#                     "name": "user_permissions",
#                     "type": "ManyToManyField",
#                     "related_model": "Permission"
#                 }
#             ],
#             "modeloLower": "user",
#             "modelo_labelSingular": "User",
#             "modelo_labelPlurar": "User",
#             "modeloLower_labelSingular": "User",
#             "modeloLower_labelPlurar": "User"
#         }
