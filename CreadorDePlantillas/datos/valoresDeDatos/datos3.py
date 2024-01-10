datos={
    "models": {
        "Permission": {
            "campos": [
                {
                    "name": "id",
                    "type": "AutoField",
                    "related_model": "",
                    "descripcion_entrada": "ID",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "name",
                    "type": "CharField",
                    "related_model": "",
                    "descripcion_entrada": "nombre",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "content_type",
                    "type": "ForeignKey",
                    "related_model": "ContentType",
                    "descripcion_entrada": "tipo de contenido",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "codename",
                    "type": "CharField",
                    "related_model": "",
                    "descripcion_entrada": "nombre en c\u00f3digo",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "permissions",
                    "type": "Extra_ManyToManyField",
                    "related_model": "Group",
                    "descripcion_entrada": "Relacion Group",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "user",
                    "type": "Extra_ManyToManyField",
                    "related_model": "User",
                    "descripcion_entrada": "Relacion User",
                    "descripcion_salida": "",
                    "related_name": "user_set"
                }
            ],
            "modeloLower": "permission",
            "modelo_labelSingular": "Permission",
            "modelo_labelPlurar": "Permission",
            "modeloLower_labelSingular": "Permission",
            "modeloLower_labelPlurar": "Permission",
            "codigos": {
                "create": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "PermissionSerializer_Create"
                },
                "list": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "PermissionSerializer_List"
                },
                "edit": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "PermissionSerializer_Update"
                },
                "destroy": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "PermissionSerializer_Destroy"
                },
                "view": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "PermissionSerializer_Retrieve"
                }
            }
        },
        "Group": {
            "campos": [
                {
                    "name": "id",
                    "type": "AutoField",
                    "related_model": "",
                    "descripcion_entrada": "ID",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "name",
                    "type": "CharField",
                    "related_model": "",
                    "descripcion_entrada": "nombre",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "permissions",
                    "type": "ManyToManyField",
                    "related_model": "Permission",
                    "descripcion_entrada": "permisos",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "user",
                    "type": "Extra_ManyToManyField",
                    "related_model": "User",
                    "descripcion_entrada": "Relacion User",
                    "descripcion_salida": "",
                    "related_name": "user_set"
                },
                {
                    "name": "rol",
                    "type": "Extra_ForeignKey",
                    "related_model": "RolNegocio",
                    "descripcion_entrada": "Relacion RolNegocio",
                    "descripcion_salida": "",
                    "related_name": None
                }
            ],
            "modeloLower": "group",
            "modelo_labelSingular": "Group",
            "modelo_labelPlurar": "Group",
            "modeloLower_labelSingular": "Group",
            "modeloLower_labelPlurar": "Group",
            "codigos": {
                "create": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "GroupSerializer_Create"
                },
                "list": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "GroupSerializer_List"
                },
                "edit": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "GroupSerializer_Update"
                },
                "destroy": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "GroupSerializer_Destroy"
                },
                "view": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "GroupSerializer_Retrieve"
                }
            }
        },
        "ContentType": {
            "campos": [
                {
                    "name": "id",
                    "type": "AutoField",
                    "related_model": "",
                    "descripcion_entrada": "ID",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "app_label",
                    "type": "CharField",
                    "related_model": "",
                    "descripcion_entrada": "app label",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "model",
                    "type": "CharField",
                    "related_model": "",
                    "descripcion_entrada": "nombre de la clase Python del modelo",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "content_type",
                    "type": "Extra_ForeignKey",
                    "related_model": "Permission",
                    "descripcion_entrada": "Relacion Permission",
                    "descripcion_salida": "",
                    "related_name": None
                }
            ],
            "modeloLower": "contenttype",
            "modelo_labelSingular": "ContentType",
            "modelo_labelPlurar": "ContentType",
            "modeloLower_labelSingular": "ContentType",
            "modeloLower_labelPlurar": "ContentType",
            "codigos": {
                "create": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "ContentTypeSerializer_Create"
                },
                "list": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "ContentTypeSerializer_List"
                },
                "edit": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "ContentTypeSerializer_Update"
                },
                "destroy": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "ContentTypeSerializer_Destroy"
                },
                "view": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "ContentTypeSerializer_Retrieve"
                }
            }
        },
        "User": {
            "campos": [
                {
                    "name": "id",
                    "type": "BigAutoField",
                    "related_model": "",
                    "descripcion_entrada": "ID",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "password",
                    "type": "CharField",
                    "related_model": "",
                    "descripcion_entrada": "contrase\u00f1a",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "last_login",
                    "type": "DateTimeField",
                    "related_model": "",
                    "descripcion_entrada": "\u00faltimo ingreso",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "is_superuser",
                    "type": "BooleanField",
                    "related_model": "",
                    "descripcion_entrada": "es superusuario",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "username",
                    "type": "CharField",
                    "related_model": "",
                    "descripcion_entrada": "username",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "email",
                    "type": "EmailField",
                    "related_model": "",
                    "descripcion_entrada": "Correo Electr\u00f3nico",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "first_name",
                    "type": "CharField",
                    "related_model": "",
                    "descripcion_entrada": "Nombres",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "last_name",
                    "type": "CharField",
                    "related_model": "",
                    "descripcion_entrada": "Apellidos",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "image",
                    "type": "ImageField",
                    "related_model": "",
                    "descripcion_entrada": "Imagen de perfil",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "phone",
                    "type": "CharField",
                    "related_model": "",
                    "descripcion_entrada": "phone",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "is_active",
                    "type": "BooleanField",
                    "related_model": "",
                    "descripcion_entrada": "is active",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "is_staff",
                    "type": "BooleanField",
                    "related_model": "",
                    "descripcion_entrada": "is staff",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "created",
                    "type": "DateTimeField",
                    "related_model": "",
                    "descripcion_entrada": "created",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "edited",
                    "type": "DateTimeField",
                    "related_model": "",
                    "descripcion_entrada": "edited",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "useAppBusiness",
                    "type": "BooleanField",
                    "related_model": "",
                    "descripcion_entrada": "useAppBusiness",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "groups",
                    "type": "ManyToManyField",
                    "related_model": "Group",
                    "descripcion_entrada": "grupos",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "user_permissions",
                    "type": "ManyToManyField",
                    "related_model": "Permission",
                    "descripcion_entrada": "permisos de usuario",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "user",
                    "type": "Extra_ForeignKey",
                    "related_model": "PalabraClave",
                    "descripcion_entrada": "Relacion PalabraClave",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "user",
                    "type": "Extra_ForeignKey",
                    "related_model": "Negocio",
                    "descripcion_entrada": "Relacion Negocio",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "user",
                    "type": "Extra_ForeignKey",
                    "related_model": "RolNegocio",
                    "descripcion_entrada": "Relacion RolNegocio",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "user",
                    "type": "Extra_ForeignKey",
                    "related_model": "CategoriaDeServicio",
                    "descripcion_entrada": "Relacion CategoriaDeServicio",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "user",
                    "type": "Extra_ForeignKey",
                    "related_model": "CategoriaDeProducto",
                    "descripcion_entrada": "Relacion CategoriaDeProducto",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "user",
                    "type": "Extra_ForeignKey",
                    "related_model": "Resenna",
                    "descripcion_entrada": "Relacion Resenna",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "user",
                    "type": "Extra_ForeignKey",
                    "related_model": "Favorito",
                    "descripcion_entrada": "Relacion Favorito",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "user",
                    "type": "Extra_ForeignKey",
                    "related_model": "RegisteredUserData",
                    "descripcion_entrada": "Relacion RegisteredUserData",
                    "descripcion_salida": "",
                    "related_name": None
                }
            ],
            "modeloLower": "user",
            "modelo_labelSingular": "User",
            "modelo_labelPlurar": "User",
            "modeloLower_labelSingular": "User",
            "modeloLower_labelPlurar": "User",
            "codigos": {
                "create": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "UserSerializer_Create"
                },
                "list": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "UserSerializer_List"
                },
                "edit": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "UserSerializer_Update"
                },
                "destroy": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "UserSerializer_Destroy"
                },
                "view": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "UserSerializer_Retrieve"
                }
            }
        },
        "PalabraClave": {
            "campos": [
                {
                    "name": "id",
                    "type": "BigAutoField",
                    "related_model": "",
                    "descripcion_entrada": "ID",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "nombre",
                    "type": "CharField",
                    "related_model": "",
                    "descripcion_entrada": "nombre",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "user",
                    "type": "ForeignKey",
                    "related_model": "User",
                    "descripcion_entrada": "user",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "esPublica",
                    "type": "BooleanField",
                    "related_model": "",
                    "descripcion_entrada": "esPublica",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "PalabrasClave",
                    "type": "Extra_ManyToManyField",
                    "related_model": "Negocio",
                    "descripcion_entrada": "Relacion Negocio",
                    "descripcion_salida": "",
                    "related_name": None
                }
            ],
            "modeloLower": "palabraclave",
            "modelo_labelSingular": "PalabraClave",
            "modelo_labelPlurar": "PalabraClave",
            "modeloLower_labelSingular": "PalabraClave",
            "modeloLower_labelPlurar": "PalabraClave",
            "codigos": {
                "create": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "PalabraClaveSerializer_Create"
                },
                "list": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "PalabraClaveSerializer_List"
                },
                "edit": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "PalabraClaveSerializer_Update"
                },
                "destroy": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "PalabraClaveSerializer_Destroy"
                },
                "view": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "PalabraClaveSerializer_Retrieve"
                }
            }
        },
        "TipoDeGestion": {
            "campos": [
                {
                    "name": "id",
                    "type": "BigAutoField",
                    "related_model": "",
                    "descripcion_entrada": "ID",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "nombre",
                    "type": "CharField",
                    "related_model": "",
                    "descripcion_entrada": "nombre",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "esPublica",
                    "type": "BooleanField",
                    "related_model": "",
                    "descripcion_entrada": "esPublica",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "TipoDeGestion",
                    "type": "Extra_ForeignKey",
                    "related_model": "Negocio",
                    "descripcion_entrada": "Relacion Negocio",
                    "descripcion_salida": "",
                    "related_name": None
                }
            ],
            "modeloLower": "tipodegestion",
            "modelo_labelSingular": "TipoDeGestion",
            "modelo_labelPlurar": "TipoDeGestion",
            "modeloLower_labelSingular": "TipoDeGestion",
            "modeloLower_labelPlurar": "TipoDeGestion",
            "codigos": {
                "create": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "TipoDeGestionSerializer_Create"
                },
                "list": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "TipoDeGestionSerializer_List"
                },
                "edit": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "TipoDeGestionSerializer_Update"
                },
                "destroy": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "TipoDeGestionSerializer_Destroy"
                },
                "view": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "TipoDeGestionSerializer_Retrieve"
                }
            }
        },
        "CategoriaDeNegocio": {
            "campos": [
                {
                    "name": "id",
                    "type": "BigAutoField",
                    "related_model": "",
                    "descripcion_entrada": "ID",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "nombre",
                    "type": "CharField",
                    "related_model": "",
                    "descripcion_entrada": "nombre",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "esPublica",
                    "type": "BooleanField",
                    "related_model": "",
                    "descripcion_entrada": "esPublica",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "CategoriasDeNegocio",
                    "type": "Extra_ManyToManyField",
                    "related_model": "Negocio",
                    "descripcion_entrada": "Relacion Negocio",
                    "descripcion_salida": "",
                    "related_name": None
                }
            ],
            "modeloLower": "categoriadenegocio",
            "modelo_labelSingular": "CategoriaDeNegocio",
            "modelo_labelPlurar": "CategoriaDeNegocio",
            "modeloLower_labelSingular": "CategoriaDeNegocio",
            "modeloLower_labelPlurar": "CategoriaDeNegocio",
            "codigos": {
                "create": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "CategoriaDeNegocioSerializer_Create"
                },
                "list": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "CategoriaDeNegocioSerializer_List"
                },
                "edit": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "CategoriaDeNegocioSerializer_Update"
                },
                "destroy": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "CategoriaDeNegocioSerializer_Destroy"
                },
                "view": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "CategoriaDeNegocioSerializer_Retrieve"
                }
            }
        },
        "Negocio": {
            "campos": [
                {
                    "name": "id",
                    "type": "BigAutoField",
                    "related_model": "",
                    "descripcion_entrada": "ID",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "nombre",
                    "type": "CharField",
                    "related_model": "",
                    "descripcion_entrada": "nombre",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "logo",
                    "type": "ImageField",
                    "related_model": "",
                    "descripcion_entrada": "logo",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "slogan",
                    "type": "CharField",
                    "related_model": "",
                    "descripcion_entrada": "slogan",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "direccion",
                    "type": "CharField",
                    "related_model": "",
                    "descripcion_entrada": "direccion",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "descripcion",
                    "type": "TextField",
                    "related_model": "",
                    "descripcion_entrada": "descripcion",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "TipoDeGestion",
                    "type": "ForeignKey",
                    "related_model": "TipoDeGestion",
                    "descripcion_entrada": "TipoDeGestion",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "user",
                    "type": "ForeignKey",
                    "related_model": "User",
                    "descripcion_entrada": "user",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "PalabrasClave",
                    "type": "ManyToManyField",
                    "related_model": "PalabraClave",
                    "descripcion_entrada": "PalabrasClave",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "CategoriasDeNegocio",
                    "type": "ManyToManyField",
                    "related_model": "CategoriaDeNegocio",
                    "descripcion_entrada": "CategoriasDeNegocio",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "rolnegocio",
                    "type": "Extra_ForeignKey",
                    "related_model": "RolNegocio",
                    "descripcion_entrada": "Relacion RolNegocio",
                    "descripcion_salida": "",
                    "related_name": "rolnegocio"
                },
                {
                    "name": "Negocio",
                    "type": "Extra_ForeignKey",
                    "related_model": "Contacto",
                    "descripcion_entrada": "Relacion Contacto",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "Negocio",
                    "type": "Extra_ForeignKey",
                    "related_model": "CategoriaDeServicio",
                    "descripcion_entrada": "Relacion CategoriaDeServicio",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "Negocio",
                    "type": "Extra_ForeignKey",
                    "related_model": "CategoriaDeProducto",
                    "descripcion_entrada": "Relacion CategoriaDeProducto",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "Negocio",
                    "type": "Extra_ForeignKey",
                    "related_model": "Producto",
                    "descripcion_entrada": "Relacion Producto",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "Negocio",
                    "type": "Extra_ForeignKey",
                    "related_model": "Servicio",
                    "descripcion_entrada": "Relacion Servicio",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "Negocio",
                    "type": "Extra_ForeignKey",
                    "related_model": "Resenna",
                    "descripcion_entrada": "Relacion Resenna",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "Negocio",
                    "type": "Extra_ForeignKey",
                    "related_model": "Favorito",
                    "descripcion_entrada": "Relacion Favorito",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "Negocio",
                    "type": "Extra_ForeignKey",
                    "related_model": "Imagen_Negocio",
                    "descripcion_entrada": "Relacion Imagen_Negocio",
                    "descripcion_salida": "",
                    "related_name": None
                }
            ],
            "modeloLower": "negocio",
            "modelo_labelSingular": "Negocio",
            "modelo_labelPlurar": "Negocio",
            "modeloLower_labelSingular": "Negocio",
            "modeloLower_labelPlurar": "Negocio",
            "codigos": {
                "create": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "NegocioSerializer_Create"
                },
                "list": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "NegocioSerializer_List"
                },
                "edit": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "NegocioSerializer_Update"
                },
                "destroy": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "NegocioSerializer_Destroy"
                },
                "view": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "NegocioSerializer_Retrieve"
                }
            }
        },
        "RolNegocio": {
            "campos": [
                {
                    "name": "id",
                    "type": "BigAutoField",
                    "related_model": "",
                    "descripcion_entrada": "ID",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "rol",
                    "type": "ForeignKey",
                    "related_model": "Group",
                    "descripcion_entrada": "rol",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "user",
                    "type": "ForeignKey",
                    "related_model": "User",
                    "descripcion_entrada": "user",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "Negocio",
                    "type": "ForeignKey",
                    "related_model": "Negocio",
                    "descripcion_entrada": "Negocio",
                    "descripcion_salida": "",
                    "related_name": None
                }
            ],
            "modeloLower": "rolnegocio",
            "modelo_labelSingular": "RolNegocio",
            "modelo_labelPlurar": "RolNegocio",
            "modeloLower_labelSingular": "RolNegocio",
            "modeloLower_labelPlurar": "RolNegocio",
            "codigos": {
                "create": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "RolNegocioSerializer_Create"
                },
                "list": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "RolNegocioSerializer_List"
                },
                "edit": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "RolNegocioSerializer_Update"
                },
                "destroy": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "RolNegocioSerializer_Destroy"
                },
                "view": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "RolNegocioSerializer_Retrieve"
                }
            }
        },
        "TipoDeContacto": {
            "campos": [
                {
                    "name": "id",
                    "type": "BigAutoField",
                    "related_model": "",
                    "descripcion_entrada": "ID",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "nombre",
                    "type": "CharField",
                    "related_model": "",
                    "descripcion_entrada": "nombre",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "TipoDeContacto",
                    "type": "Extra_ForeignKey",
                    "related_model": "Contacto",
                    "descripcion_entrada": "Relacion Contacto",
                    "descripcion_salida": "",
                    "related_name": None
                }
            ],
            "modeloLower": "tipodecontacto",
            "modelo_labelSingular": "TipoDeContacto",
            "modelo_labelPlurar": "TipoDeContacto",
            "modeloLower_labelSingular": "TipoDeContacto",
            "modeloLower_labelPlurar": "TipoDeContacto",
            "codigos": {
                "create": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "TipoDeContactoSerializer_Create"
                },
                "list": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "TipoDeContactoSerializer_List"
                },
                "edit": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "TipoDeContactoSerializer_Update"
                },
                "destroy": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "TipoDeContactoSerializer_Destroy"
                },
                "view": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "TipoDeContactoSerializer_Retrieve"
                }
            }
        },
        "Contacto": {
            "campos": [
                {
                    "name": "id",
                    "type": "BigAutoField",
                    "related_model": "",
                    "descripcion_entrada": "ID",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "nombre",
                    "type": "CharField",
                    "related_model": "",
                    "descripcion_entrada": "nombre",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "TipoDeContacto",
                    "type": "ForeignKey",
                    "related_model": "TipoDeContacto",
                    "descripcion_entrada": "TipoDeContacto",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "Negocio",
                    "type": "ForeignKey",
                    "related_model": "Negocio",
                    "descripcion_entrada": "Negocio",
                    "descripcion_salida": "",
                    "related_name": None
                }
            ],
            "modeloLower": "contacto",
            "modelo_labelSingular": "Contacto",
            "modelo_labelPlurar": "Contacto",
            "modeloLower_labelSingular": "Contacto",
            "modeloLower_labelPlurar": "Contacto",
            "codigos": {
                "create": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "ContactoSerializer_Create"
                },
                "list": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "ContactoSerializer_List"
                },
                "edit": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "ContactoSerializer_Update"
                },
                "destroy": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "ContactoSerializer_Destroy"
                },
                "view": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "ContactoSerializer_Retrieve"
                }
            }
        },
        "CategoriaDeServicio": {
            "campos": [
                {
                    "name": "id",
                    "type": "BigAutoField",
                    "related_model": "",
                    "descripcion_entrada": "ID",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "nombre",
                    "type": "CharField",
                    "related_model": "",
                    "descripcion_entrada": "nombre",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "user",
                    "type": "ForeignKey",
                    "related_model": "User",
                    "descripcion_entrada": "user",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "Negocio",
                    "type": "ForeignKey",
                    "related_model": "Negocio",
                    "descripcion_entrada": "Negocio",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "esPublica",
                    "type": "BooleanField",
                    "related_model": "",
                    "descripcion_entrada": "esPublica",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "Categoria",
                    "type": "Extra_ForeignKey",
                    "related_model": "Servicio",
                    "descripcion_entrada": "Relacion Servicio",
                    "descripcion_salida": "",
                    "related_name": None
                }
            ],
            "modeloLower": "categoriadeservicio",
            "modelo_labelSingular": "CategoriaDeServicio",
            "modelo_labelPlurar": "CategoriaDeServicio",
            "modeloLower_labelSingular": "CategoriaDeServicio",
            "modeloLower_labelPlurar": "CategoriaDeServicio",
            "codigos": {
                "create": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "CategoriaDeServicioSerializer_Create"
                },
                "list": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "CategoriaDeServicioSerializer_List"
                },
                "edit": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "CategoriaDeServicioSerializer_Update"
                },
                "destroy": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "CategoriaDeServicioSerializer_Destroy"
                },
                "view": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "CategoriaDeServicioSerializer_Retrieve"
                }
            }
        },
        "CategoriaDeProducto": {
            "campos": [
                {
                    "name": "id",
                    "type": "BigAutoField",
                    "related_model": "",
                    "descripcion_entrada": "ID",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "nombre",
                    "type": "CharField",
                    "related_model": "",
                    "descripcion_entrada": "nombre",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "user",
                    "type": "ForeignKey",
                    "related_model": "User",
                    "descripcion_entrada": "user",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "Negocio",
                    "type": "ForeignKey",
                    "related_model": "Negocio",
                    "descripcion_entrada": "Negocio",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "esPublica",
                    "type": "BooleanField",
                    "related_model": "",
                    "descripcion_entrada": "esPublica",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "Categoria",
                    "type": "Extra_ForeignKey",
                    "related_model": "Producto",
                    "descripcion_entrada": "Relacion Producto",
                    "descripcion_salida": "",
                    "related_name": None
                }
            ],
            "modeloLower": "categoriadeproducto",
            "modelo_labelSingular": "CategoriaDeProducto",
            "modelo_labelPlurar": "CategoriaDeProducto",
            "modeloLower_labelSingular": "CategoriaDeProducto",
            "modeloLower_labelPlurar": "CategoriaDeProducto",
            "codigos": {
                "create": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "CategoriaDeProductoSerializer_Create"
                },
                "list": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "CategoriaDeProductoSerializer_List"
                },
                "edit": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "CategoriaDeProductoSerializer_Update"
                },
                "destroy": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "CategoriaDeProductoSerializer_Destroy"
                },
                "view": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "CategoriaDeProductoSerializer_Retrieve"
                }
            }
        },
        "Producto": {
            "campos": [
                {
                    "name": "id",
                    "type": "BigAutoField",
                    "related_model": "",
                    "descripcion_entrada": "ID",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "Nombre",
                    "type": "CharField",
                    "related_model": "",
                    "descripcion_entrada": "Nombre",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "Disponibilidad",
                    "type": "BooleanField",
                    "related_model": "",
                    "descripcion_entrada": "Disponibilidad",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "Precio_actual",
                    "type": "FloatField",
                    "related_model": "",
                    "descripcion_entrada": "Precio actual",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "Precio_anterior",
                    "type": "FloatField",
                    "related_model": "",
                    "descripcion_entrada": "Precio anterior",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "Descripcion",
                    "type": "TextField",
                    "related_model": "",
                    "descripcion_entrada": "Descripcion",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "Categoria",
                    "type": "ForeignKey",
                    "related_model": "CategoriaDeProducto",
                    "descripcion_entrada": "Categoria",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "Negocio",
                    "type": "ForeignKey",
                    "related_model": "Negocio",
                    "descripcion_entrada": "Negocio",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "Producto",
                    "type": "Extra_ForeignKey",
                    "related_model": "Resenna",
                    "descripcion_entrada": "Relacion Resenna",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "Producto",
                    "type": "Extra_ForeignKey",
                    "related_model": "Favorito",
                    "descripcion_entrada": "Relacion Favorito",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "Producto",
                    "type": "Extra_ForeignKey",
                    "related_model": "Imagen_Producto",
                    "descripcion_entrada": "Relacion Imagen_Producto",
                    "descripcion_salida": "",
                    "related_name": None
                }
            ],
            "modeloLower": "producto",
            "modelo_labelSingular": "Producto",
            "modelo_labelPlurar": "Producto",
            "modeloLower_labelSingular": "Producto",
            "modeloLower_labelPlurar": "Producto",
            "codigos": {
                "create": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "ProductoSerializer_Create"
                },
                "list": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "ProductoSerializer_List"
                },
                "edit": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "ProductoSerializer_Update"
                },
                "destroy": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "ProductoSerializer_Destroy"
                },
                "view": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "ProductoSerializer_Retrieve"
                }
            }
        },
        "Servicio": {
            "campos": [
                {
                    "name": "id",
                    "type": "BigAutoField",
                    "related_model": "",
                    "descripcion_entrada": "ID",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "Nombre",
                    "type": "CharField",
                    "related_model": "",
                    "descripcion_entrada": "Nombre",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "Disponibilidad",
                    "type": "BooleanField",
                    "related_model": "",
                    "descripcion_entrada": "Disponibilidad",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "Precio_actual",
                    "type": "FloatField",
                    "related_model": "",
                    "descripcion_entrada": "Precio actual",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "Precio_anterior",
                    "type": "FloatField",
                    "related_model": "",
                    "descripcion_entrada": "Precio anterior",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "Descripcion",
                    "type": "TextField",
                    "related_model": "",
                    "descripcion_entrada": "Descripcion",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "Categoria",
                    "type": "ForeignKey",
                    "related_model": "CategoriaDeServicio",
                    "descripcion_entrada": "Categoria",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "Negocio",
                    "type": "ForeignKey",
                    "related_model": "Negocio",
                    "descripcion_entrada": "Negocio",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "Servicio",
                    "type": "Extra_ForeignKey",
                    "related_model": "Resenna",
                    "descripcion_entrada": "Relacion Resenna",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "Servicio",
                    "type": "Extra_ForeignKey",
                    "related_model": "Favorito",
                    "descripcion_entrada": "Relacion Favorito",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "Servicio",
                    "type": "Extra_ForeignKey",
                    "related_model": "Imagen_Servicio",
                    "descripcion_entrada": "Relacion Imagen_Servicio",
                    "descripcion_salida": "",
                    "related_name": None
                }
            ],
            "modeloLower": "servicio",
            "modelo_labelSingular": "Servicio",
            "modelo_labelPlurar": "Servicio",
            "modeloLower_labelSingular": "Servicio",
            "modeloLower_labelPlurar": "Servicio",
            "codigos": {
                "create": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "ServicioSerializer_Create"
                },
                "list": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "ServicioSerializer_List"
                },
                "edit": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "ServicioSerializer_Update"
                },
                "destroy": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "ServicioSerializer_Destroy"
                },
                "view": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "ServicioSerializer_Retrieve"
                }
            }
        },
        "TipoDeResenna": {
            "campos": [
                {
                    "name": "id",
                    "type": "BigAutoField",
                    "related_model": "",
                    "descripcion_entrada": "ID",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "nombre",
                    "type": "CharField",
                    "related_model": "",
                    "descripcion_entrada": "nombre",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "TipoDeResenna",
                    "type": "Extra_ForeignKey",
                    "related_model": "Resenna",
                    "descripcion_entrada": "Relacion Resenna",
                    "descripcion_salida": "",
                    "related_name": None
                }
            ],
            "modeloLower": "tipoderesenna",
            "modelo_labelSingular": "TipoDeResenna",
            "modelo_labelPlurar": "TipoDeResenna",
            "modeloLower_labelSingular": "TipoDeResenna",
            "modeloLower_labelPlurar": "TipoDeResenna",
            "codigos": {
                "create": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "TipoDeResennaSerializer_Create"
                },
                "list": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "TipoDeResennaSerializer_List"
                },
                "edit": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "TipoDeResennaSerializer_Update"
                },
                "destroy": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "TipoDeResennaSerializer_Destroy"
                },
                "view": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "TipoDeResennaSerializer_Retrieve"
                }
            }
        },
        "Resenna": {
            "campos": [
                {
                    "name": "id",
                    "type": "BigAutoField",
                    "related_model": "",
                    "descripcion_entrada": "ID",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "texto",
                    "type": "TextField",
                    "related_model": "",
                    "descripcion_entrada": "texto",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "puntuacion",
                    "type": "IntegerField",
                    "related_model": "",
                    "descripcion_entrada": "puntuacion",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "fecha_creacion",
                    "type": "DateTimeField",
                    "related_model": "",
                    "descripcion_entrada": "fecha creacion",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "fecha_edicion",
                    "type": "DateTimeField",
                    "related_model": "",
                    "descripcion_entrada": "fecha edicion",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "Negocio",
                    "type": "ForeignKey",
                    "related_model": "Negocio",
                    "descripcion_entrada": "Negocio",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "Producto",
                    "type": "ForeignKey",
                    "related_model": "Producto",
                    "descripcion_entrada": "Producto",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "Servicio",
                    "type": "ForeignKey",
                    "related_model": "Servicio",
                    "descripcion_entrada": "Servicio",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "user",
                    "type": "ForeignKey",
                    "related_model": "User",
                    "descripcion_entrada": "user",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "TipoDeResenna",
                    "type": "ForeignKey",
                    "related_model": "TipoDeResenna",
                    "descripcion_entrada": "TipoDeResenna",
                    "descripcion_salida": "",
                    "related_name": None
                }
            ],
            "modeloLower": "resenna",
            "modelo_labelSingular": "Resenna",
            "modelo_labelPlurar": "Resenna",
            "modeloLower_labelSingular": "Resenna",
            "modeloLower_labelPlurar": "Resenna",
            "codigos": {
                "create": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "ResennaSerializer_Create"
                },
                "list": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "ResennaSerializer_List"
                },
                "edit": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "ResennaSerializer_Update"
                },
                "destroy": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "ResennaSerializer_Destroy"
                },
                "view": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "ResennaSerializer_Retrieve"
                }
            }
        },
        "TipoDeFavorito": {
            "campos": [
                {
                    "name": "id",
                    "type": "BigAutoField",
                    "related_model": "",
                    "descripcion_entrada": "ID",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "nombre",
                    "type": "CharField",
                    "related_model": "",
                    "descripcion_entrada": "nombre",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "TipoDeFavorito",
                    "type": "Extra_ForeignKey",
                    "related_model": "Favorito",
                    "descripcion_entrada": "Relacion Favorito",
                    "descripcion_salida": "",
                    "related_name": None
                }
            ],
            "modeloLower": "tipodefavorito",
            "modelo_labelSingular": "TipoDeFavorito",
            "modelo_labelPlurar": "TipoDeFavorito",
            "modeloLower_labelSingular": "TipoDeFavorito",
            "modeloLower_labelPlurar": "TipoDeFavorito",
            "codigos": {
                "create": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "TipoDeFavoritoSerializer_Create"
                },
                "list": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "TipoDeFavoritoSerializer_List"
                },
                "edit": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "TipoDeFavoritoSerializer_Update"
                },
                "destroy": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "TipoDeFavoritoSerializer_Destroy"
                },
                "view": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "TipoDeFavoritoSerializer_Retrieve"
                }
            }
        },
        "Favorito": {
            "campos": [
                {
                    "name": "id",
                    "type": "BigAutoField",
                    "related_model": "",
                    "descripcion_entrada": "ID",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "fecha_creacion",
                    "type": "DateTimeField",
                    "related_model": "",
                    "descripcion_entrada": "fecha creacion",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "fecha_edicion",
                    "type": "DateTimeField",
                    "related_model": "",
                    "descripcion_entrada": "fecha edicion",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "Negocio",
                    "type": "ForeignKey",
                    "related_model": "Negocio",
                    "descripcion_entrada": "Negocio",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "Producto",
                    "type": "ForeignKey",
                    "related_model": "Producto",
                    "descripcion_entrada": "Producto",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "Servicio",
                    "type": "ForeignKey",
                    "related_model": "Servicio",
                    "descripcion_entrada": "Servicio",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "user",
                    "type": "ForeignKey",
                    "related_model": "User",
                    "descripcion_entrada": "user",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "TipoDeFavorito",
                    "type": "ForeignKey",
                    "related_model": "TipoDeFavorito",
                    "descripcion_entrada": "TipoDeFavorito",
                    "descripcion_salida": "",
                    "related_name": None
                }
            ],
            "modeloLower": "favorito",
            "modelo_labelSingular": "Favorito",
            "modelo_labelPlurar": "Favorito",
            "modeloLower_labelSingular": "Favorito",
            "modeloLower_labelPlurar": "Favorito",
            "codigos": {
                "create": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "FavoritoSerializer_Create"
                },
                "list": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "FavoritoSerializer_List"
                },
                "edit": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "FavoritoSerializer_Update"
                },
                "destroy": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "FavoritoSerializer_Destroy"
                },
                "view": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "FavoritoSerializer_Retrieve"
                }
            }
        },
        "Imagen_Negocio": {
            "campos": [
                {
                    "name": "id",
                    "type": "BigAutoField",
                    "related_model": "",
                    "descripcion_entrada": "ID",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "fecha_creacion",
                    "type": "DateTimeField",
                    "related_model": "",
                    "descripcion_entrada": "fecha creacion",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "Imagen",
                    "type": "ImageField",
                    "related_model": "",
                    "descripcion_entrada": "Imagen",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "Negocio",
                    "type": "ForeignKey",
                    "related_model": "Negocio",
                    "descripcion_entrada": "Negocio",
                    "descripcion_salida": "",
                    "related_name": None
                }
            ],
            "modeloLower": "imagen_negocio",
            "modelo_labelSingular": "Imagen_Negocio",
            "modelo_labelPlurar": "Imagen_Negocio",
            "modeloLower_labelSingular": "Imagen_Negocio",
            "modeloLower_labelPlurar": "Imagen_Negocio",
            "codigos": {
                "create": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "Imagen_NegocioSerializer_Create"
                },
                "list": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "Imagen_NegocioSerializer_List"
                },
                "edit": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "Imagen_NegocioSerializer_Update"
                },
                "destroy": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "Imagen_NegocioSerializer_Destroy"
                },
                "view": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "Imagen_NegocioSerializer_Retrieve"
                }
            }
        },
        "Imagen_Producto": {
            "campos": [
                {
                    "name": "id",
                    "type": "BigAutoField",
                    "related_model": "",
                    "descripcion_entrada": "ID",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "fecha_creacion",
                    "type": "DateTimeField",
                    "related_model": "",
                    "descripcion_entrada": "fecha creacion",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "Imagen",
                    "type": "ImageField",
                    "related_model": "",
                    "descripcion_entrada": "Imagen",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "Producto",
                    "type": "ForeignKey",
                    "related_model": "Producto",
                    "descripcion_entrada": "Producto",
                    "descripcion_salida": "",
                    "related_name": None
                }
            ],
            "modeloLower": "imagen_producto",
            "modelo_labelSingular": "Imagen_Producto",
            "modelo_labelPlurar": "Imagen_Producto",
            "modeloLower_labelSingular": "Imagen_Producto",
            "modeloLower_labelPlurar": "Imagen_Producto",
            "codigos": {
                "create": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "Imagen_ProductoSerializer_Create"
                },
                "list": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "Imagen_ProductoSerializer_List"
                },
                "edit": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "Imagen_ProductoSerializer_Update"
                },
                "destroy": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "Imagen_ProductoSerializer_Destroy"
                },
                "view": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "Imagen_ProductoSerializer_Retrieve"
                }
            }
        },
        "Imagen_Servicio": {
            "campos": [
                {
                    "name": "id",
                    "type": "BigAutoField",
                    "related_model": "",
                    "descripcion_entrada": "ID",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "fecha_creacion",
                    "type": "DateTimeField",
                    "related_model": "",
                    "descripcion_entrada": "fecha creacion",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "Imagen",
                    "type": "ImageField",
                    "related_model": "",
                    "descripcion_entrada": "Imagen",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "Servicio",
                    "type": "ForeignKey",
                    "related_model": "Servicio",
                    "descripcion_entrada": "Servicio",
                    "descripcion_salida": "",
                    "related_name": None
                }
            ],
            "modeloLower": "imagen_servicio",
            "modelo_labelSingular": "Imagen_Servicio",
            "modelo_labelPlurar": "Imagen_Servicio",
            "modeloLower_labelSingular": "Imagen_Servicio",
            "modeloLower_labelPlurar": "Imagen_Servicio",
            "codigos": {
                "create": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "Imagen_ServicioSerializer_Create"
                },
                "list": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "Imagen_ServicioSerializer_List"
                },
                "edit": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "Imagen_ServicioSerializer_Update"
                },
                "destroy": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "Imagen_ServicioSerializer_Destroy"
                },
                "view": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "Imagen_ServicioSerializer_Retrieve"
                }
            }
        },
        "ZdsmsSessions": {
            "campos": [
                {
                    "name": "id",
                    "type": "BigAutoField",
                    "related_model": "",
                    "descripcion_entrada": "ID",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "token",
                    "type": "CharField",
                    "related_model": "",
                    "descripcion_entrada": "token",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "type",
                    "type": "CharField",
                    "related_model": "",
                    "descripcion_entrada": "type",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "expire",
                    "type": "DateTimeField",
                    "related_model": "",
                    "descripcion_entrada": "expire",
                    "descripcion_salida": "",
                    "related_name": None
                }
            ],
            "modeloLower": "zdsmssessions",
            "modelo_labelSingular": "ZdsmsSessions",
            "modelo_labelPlurar": "ZdsmsSessions",
            "modeloLower_labelSingular": "ZdsmsSessions",
            "modeloLower_labelPlurar": "ZdsmsSessions",
            "codigos": {
                "create": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "ZdsmsSessionsSerializer_Create"
                },
                "list": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "ZdsmsSessionsSerializer_List"
                },
                "edit": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "ZdsmsSessionsSerializer_Update"
                },
                "destroy": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "ZdsmsSessionsSerializer_Destroy"
                },
                "view": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "ZdsmsSessionsSerializer_Retrieve"
                }
            }
        },
        "ValidationType": {
            "campos": [
                {
                    "name": "id",
                    "type": "BigIntegerField",
                    "related_model": "",
                    "descripcion_entrada": "id",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "name",
                    "type": "CharField",
                    "related_model": "",
                    "descripcion_entrada": "Nombre",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "validation_type",
                    "type": "Extra_ForeignKey",
                    "related_model": "ValidationRequest",
                    "descripcion_entrada": "Relacion ValidationRequest",
                    "descripcion_salida": "",
                    "related_name": None
                }
            ],
            "modeloLower": "validationtype",
            "modelo_labelSingular": "ValidationType",
            "modelo_labelPlurar": "ValidationType",
            "modeloLower_labelSingular": "ValidationType",
            "modeloLower_labelPlurar": "ValidationType",
            "codigos": {
                "create": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "ValidationTypeSerializer_Create"
                },
                "list": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "ValidationTypeSerializer_List"
                },
                "edit": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "ValidationTypeSerializer_Update"
                },
                "destroy": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "ValidationTypeSerializer_Destroy"
                },
                "view": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "ValidationTypeSerializer_Retrieve"
                }
            }
        },
        "ValidationRequest": {
            "campos": [
                {
                    "name": "id",
                    "type": "BigAutoField",
                    "related_model": "",
                    "descripcion_entrada": "ID",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "phone",
                    "type": "CharField",
                    "related_model": "",
                    "descripcion_entrada": "Telefono",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "expiration_date",
                    "type": "DateTimeField",
                    "related_model": "",
                    "descripcion_entrada": "Fecha de Expiraci\u00f3n",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "code",
                    "type": "CharField",
                    "related_model": "",
                    "descripcion_entrada": "C\u00f3digo",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "checked",
                    "type": "BooleanField",
                    "related_model": "",
                    "descripcion_entrada": "Verificado",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "defeated",
                    "type": "BooleanField",
                    "related_model": "",
                    "descripcion_entrada": "Vencido",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "validation_type",
                    "type": "ForeignKey",
                    "related_model": "ValidationType",
                    "descripcion_entrada": "Tipo de Validaci\u00f3n",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "validation_request",
                    "type": "Extra_ForeignKey",
                    "related_model": "RegisteredUserData",
                    "descripcion_entrada": "Relacion RegisteredUserData",
                    "descripcion_salida": "",
                    "related_name": None
                }
            ],
            "modeloLower": "validationrequest",
            "modelo_labelSingular": "ValidationRequest",
            "modelo_labelPlurar": "ValidationRequest",
            "modeloLower_labelSingular": "ValidationRequest",
            "modeloLower_labelPlurar": "ValidationRequest",
            "codigos": {
                "create": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "ValidationRequestSerializer_Create"
                },
                "list": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "ValidationRequestSerializer_List"
                },
                "edit": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "ValidationRequestSerializer_Update"
                },
                "destroy": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "ValidationRequestSerializer_Destroy"
                },
                "view": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "ValidationRequestSerializer_Retrieve"
                }
            }
        },
        "RegisteredUserData": {
            "campos": [
                {
                    "name": "id",
                    "type": "BigAutoField",
                    "related_model": "",
                    "descripcion_entrada": "ID",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "validation_request",
                    "type": "ForeignKey",
                    "related_model": "ValidationRequest",
                    "descripcion_entrada": "Validaci\u00f3n SMS",
                    "descripcion_salida": "",
                    "related_name": None
                },
                {
                    "name": "user",
                    "type": "ForeignKey",
                    "related_model": "User",
                    "descripcion_entrada": "user",
                    "descripcion_salida": "",
                    "related_name": None
                }
            ],
            "modeloLower": "registereduserdata",
            "modelo_labelSingular": "RegisteredUserData",
            "modelo_labelPlurar": "RegisteredUserData",
            "modeloLower_labelSingular": "RegisteredUserData",
            "modeloLower_labelPlurar": "RegisteredUserData",
            "codigos": {
                "create": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "RegisteredUserDataSerializer_Create"
                },
                "list": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "RegisteredUserDataSerializer_List"
                },
                "edit": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "RegisteredUserDataSerializer_Update"
                },
                "destroy": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "RegisteredUserDataSerializer_Destroy"
                },
                "view": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "RegisteredUserDataSerializer_Retrieve"
                }
            }
        }
    },
    "attribute_types": [
        "AutoField",
        "CharField",
        "ForeignKey",
        "Extra_ForeignKey",
        "Extra_ManyToManyField",
        "ManyToManyField",
        "BigAutoField",
        "DateTimeField",
        "BooleanField",
        "EmailField",
        "ImageField",
        "TextField",
        "FloatField",
        "IntegerField",
        "BigIntegerField"
    ]
}

