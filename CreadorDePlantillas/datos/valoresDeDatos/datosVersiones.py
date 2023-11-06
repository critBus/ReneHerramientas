datos_versiones={
    "models": {
        "Platform": {
            "campos": [
                {
                    "name": "id",
                    "type": "BigIntegerField",
                    "related_model": "",
                    "descripcion_entrada": "id",
                    "descripcion_salida": ""
                },
                {
                    "name": "name",
                    "type": "CharField",
                    "related_model": "",
                    "descripcion_entrada": "Nombre",
                    "descripcion_salida": ""
                }
            ],
            "modeloLower": "platform",
            "modelo_labelSingular": "Platform",
            "modelo_labelPlurar": "Platform",
            "modeloLower_labelSingular": "Platform",
            "modeloLower_labelPlurar": "Platform",
            "codigos": {
                "create": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "PlatformSerializer_Create"
                },
                "list": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "PlatformSerializer_List"
                },
                "edit": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "PlatformSerializer_Update"
                },
                "destroy": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "PlatformSerializer_Destroy"
                },
                "view": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "PlatformSerializer_Retrieve"
                }
            }
        },
        "Application": {
            "campos": [
                {
                    "name": "id",
                    "type": "BigIntegerField",
                    "related_model": "",
                    "descripcion_entrada": "id",
                    "descripcion_salida": ""
                },
                {
                    "name": "name",
                    "type": "CharField",
                    "related_model": "",
                    "descripcion_entrada": "Nombre",
                    "descripcion_salida": ""
                }
            ],
            "modeloLower": "application",
            "modelo_labelSingular": "Application",
            "modelo_labelPlurar": "Application",
            "modeloLower_labelSingular": "Application",
            "modeloLower_labelPlurar": "Application",
            "codigos": {
                "create": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "ApplicationSerializer_Create"
                },
                "list": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "ApplicationSerializer_List"
                },
                "edit": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "ApplicationSerializer_Update"
                },
                "destroy": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "ApplicationSerializer_Destroy"
                },
                "view": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "ApplicationSerializer_Retrieve"
                }
            }
        },
        "VersionStatus": {
            "campos": [
                {
                    "name": "id",
                    "type": "BigIntegerField",
                    "related_model": "",
                    "descripcion_entrada": "id",
                    "descripcion_salida": ""
                },
                {
                    "name": "status",
                    "type": "CharField",
                    "related_model": "",
                    "descripcion_entrada": "Estado",
                    "descripcion_salida": ""
                }
            ],
            "modeloLower": "versionstatus",
            "modelo_labelSingular": "VersionStatus",
            "modelo_labelPlurar": "VersionStatus",
            "modeloLower_labelSingular": "VersionStatus",
            "modeloLower_labelPlurar": "VersionStatus",
            "codigos": {
                "create": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "VersionStatusSerializer_Create"
                },
                "list": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "VersionStatusSerializer_List"
                },
                "edit": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "VersionStatusSerializer_Update"
                },
                "destroy": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "VersionStatusSerializer_Destroy"
                },
                "view": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "VersionStatusSerializer_Retrieve"
                }
            }
        },
        "Version": {
            "campos": [
                {
                    "name": "id",
                    "type": "BigAutoField",
                    "related_model": "",
                    "descripcion_entrada": "ID",
                    "descripcion_salida": ""
                },
                {
                    "name": "name",
                    "type": "CharField",
                    "related_model": "",
                    "descripcion_entrada": "Nombre",
                    "descripcion_salida": ""
                },
                {
                    "name": "build_number",
                    "type": "IntegerField",
                    "related_model": "",
                    "descripcion_entrada": "build number",
                    "descripcion_salida": ""
                },
                {
                    "name": "platform",
                    "type": "ForeignKey",
                    "related_model": "Platform",
                    "descripcion_entrada": "Plataforma",
                    "descripcion_salida": ""
                },
                {
                    "name": "status",
                    "type": "ForeignKey",
                    "related_model": "VersionStatus",
                    "descripcion_entrada": "Estado",
                    "descripcion_salida": ""
                },
                {
                    "name": "application",
                    "type": "ForeignKey",
                    "related_model": "Application",
                    "descripcion_entrada": "Aplicaci\u00f3n",
                    "descripcion_salida": ""
                }
            ],
            "modeloLower": "version",
            "modelo_labelSingular": "Version",
            "modelo_labelPlurar": "Version",
            "modeloLower_labelSingular": "Version",
            "modeloLower_labelPlurar": "Version",
            "codigos": {
                "create": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "VersionSerializer_Create"
                },
                "list": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "VersionSerializer_List"
                },
                "edit": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "VersionSerializer_Update"
                },
                "destroy": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "VersionSerializer_Destroy"
                },
                "view": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "VersionSerializer_Retrieve"
                }
            }
        },
        "Version_Feature": {
            "campos": [
                {
                    "name": "id",
                    "type": "BigAutoField",
                    "related_model": "",
                    "descripcion_entrada": "ID",
                    "descripcion_salida": ""
                },
                {
                    "name": "description",
                    "type": "TextField",
                    "related_model": "",
                    "descripcion_entrada": "Descripci\u00f3n",
                    "descripcion_salida": ""
                },
                {
                    "name": "version",
                    "type": "ForeignKey",
                    "related_model": "Version",
                    "descripcion_entrada": "Versi\u00f3n",
                    "descripcion_salida": ""
                }
            ],
            "modeloLower": "version_feature",
            "modelo_labelSingular": "Version_Feature",
            "modelo_labelPlurar": "Version_Feature",
            "modeloLower_labelSingular": "Version_Feature",
            "modeloLower_labelPlurar": "Version_Feature",
            "codigos": {
                "create": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "Version_FeatureSerializer_Create"
                },
                "list": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "Version_FeatureSerializer_List"
                },
                "edit": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "Version_FeatureSerializer_Update"
                },
                "destroy": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "Version_FeatureSerializer_Destroy"
                },
                "view": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "Version_FeatureSerializer_Retrieve"
                }
            }
        },
        "Store": {
            "campos": [
                {
                    "name": "id",
                    "type": "BigIntegerField",
                    "related_model": "",
                    "descripcion_entrada": "id",
                    "descripcion_salida": ""
                },
                {
                    "name": "name",
                    "type": "CharField",
                    "related_model": "",
                    "descripcion_entrada": "Nombre",
                    "descripcion_salida": ""
                },
                {
                    "name": "download_url",
                    "type": "CharField",
                    "related_model": "",
                    "descripcion_entrada": "Direcci\u00f3n de descarga",
                    "descripcion_salida": ""
                },
                {
                    "name": "platform",
                    "type": "ForeignKey",
                    "related_model": "Platform",
                    "descripcion_entrada": "Plataforma",
                    "descripcion_salida": ""
                },
                {
                    "name": "versions",
                    "type": "ManyToManyField",
                    "related_model": "Version",
                    "descripcion_entrada": "Versiones",
                    "descripcion_salida": ""
                }
            ],
            "modeloLower": "store",
            "modelo_labelSingular": "Store",
            "modelo_labelPlurar": "Store",
            "modeloLower_labelSingular": "Store",
            "modeloLower_labelPlurar": "Store",
            "codigos": {
                "create": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "StoreSerializer_Create"
                },
                "list": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "StoreSerializer_List"
                },
                "edit": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "StoreSerializer_Update"
                },
                "destroy": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "StoreSerializer_Destroy"
                },
                "view": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "StoreSerializer_Retrieve"
                }
            }
        }
    },
    "attribute_types": [
        "BigIntegerField",
        "CharField",
        "BigAutoField",
        "IntegerField",
        "ForeignKey",
        "TextField",
        "ManyToManyField"
    ]
}