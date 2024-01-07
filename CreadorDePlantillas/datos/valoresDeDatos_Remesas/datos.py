datos_todo={
    "models": {
        "Permission": {
            "campos": [
                {
                    "name": "id",
                    "type": "AutoField",
                    "related_model": "",
                    "descripcion_entrada": "ID",
                    "descripcion_salida": ""
                },
                {
                    "name": "name",
                    "type": "CharField",
                    "related_model": "",
                    "descripcion_entrada": "nombre",
                    "descripcion_salida": ""
                },
                {
                    "name": "content_type",
                    "type": "ForeignKey",
                    "related_model": "ContentType",
                    "descripcion_entrada": "tipo de contenido",
                    "descripcion_salida": ""
                },
                {
                    "name": "codename",
                    "type": "CharField",
                    "related_model": "",
                    "descripcion_entrada": "nombre en c\u00f3digo",
                    "descripcion_salida": ""
                },
                {
                    "name": "None",
                    "type": "Extra_ManyToManyField",
                    "related_model": "Group",
                    "descripcion_entrada": "Relacion Group",
                    "descripcion_salida": ""
                },
                {
                    "name": "user_set",
                    "type": "Extra_ManyToManyField",
                    "related_model": "User",
                    "descripcion_entrada": "Relacion User",
                    "descripcion_salida": ""
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
                    "descripcion_salida": ""
                },
                {
                    "name": "name",
                    "type": "CharField",
                    "related_model": "",
                    "descripcion_entrada": "nombre",
                    "descripcion_salida": ""
                },
                {
                    "name": "permissions",
                    "type": "ManyToManyField",
                    "related_model": "Permission",
                    "descripcion_entrada": "permisos",
                    "descripcion_salida": ""
                },
                {
                    "name": "user_set",
                    "type": "Extra_ManyToManyField",
                    "related_model": "User",
                    "descripcion_entrada": "Relacion User",
                    "descripcion_salida": ""
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
                    "descripcion_salida": ""
                },
                {
                    "name": "app_label",
                    "type": "CharField",
                    "related_model": "",
                    "descripcion_entrada": "app label",
                    "descripcion_salida": ""
                },
                {
                    "name": "model",
                    "type": "CharField",
                    "related_model": "",
                    "descripcion_entrada": "nombre de la clase Python del modelo",
                    "descripcion_salida": ""
                },
                {
                    "name": "None",
                    "type": "Extra_ForeignKey",
                    "related_model": "Permission",
                    "descripcion_entrada": "Relacion Permission",
                    "descripcion_salida": ""
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
        "HistoricalUser": {
            "campos": [
                {
                    "name": "id",
                    "type": "BigIntegerField",
                    "related_model": "",
                    "descripcion_entrada": "ID",
                    "descripcion_salida": ""
                },
                {
                    "name": "password",
                    "type": "CharField",
                    "related_model": "",
                    "descripcion_entrada": "contrase\u00f1a",
                    "descripcion_salida": ""
                },
                {
                    "name": "last_login",
                    "type": "DateTimeField",
                    "related_model": "",
                    "descripcion_entrada": "\u00faltimo ingreso",
                    "descripcion_salida": ""
                },
                {
                    "name": "is_superuser",
                    "type": "BooleanField",
                    "related_model": "",
                    "descripcion_entrada": "es superusuario",
                    "descripcion_salida": ""
                },
                {
                    "name": "username",
                    "type": "CharField",
                    "related_model": "",
                    "descripcion_entrada": "username",
                    "descripcion_salida": ""
                },
                {
                    "name": "email",
                    "type": "EmailField",
                    "related_model": "",
                    "descripcion_entrada": "email",
                    "descripcion_salida": ""
                },
                {
                    "name": "first_name",
                    "type": "CharField",
                    "related_model": "",
                    "descripcion_entrada": "first name",
                    "descripcion_salida": ""
                },
                {
                    "name": "last_name",
                    "type": "CharField",
                    "related_model": "",
                    "descripcion_entrada": "last name",
                    "descripcion_salida": ""
                },
                {
                    "name": "phone",
                    "type": "CharField",
                    "related_model": "",
                    "descripcion_entrada": "phone",
                    "descripcion_salida": ""
                },
                {
                    "name": "address",
                    "type": "CharField",
                    "related_model": "",
                    "descripcion_entrada": "address",
                    "descripcion_salida": ""
                },
                {
                    "name": "postal_code",
                    "type": "CharField",
                    "related_model": "",
                    "descripcion_entrada": "postal code",
                    "descripcion_salida": ""
                },
                {
                    "name": "is_active",
                    "type": "BooleanField",
                    "related_model": "",
                    "descripcion_entrada": "is active",
                    "descripcion_salida": ""
                },
                {
                    "name": "is_staff",
                    "type": "BooleanField",
                    "related_model": "",
                    "descripcion_entrada": "is staff",
                    "descripcion_salida": ""
                },
                {
                    "name": "confirmed_email",
                    "type": "BooleanField",
                    "related_model": "",
                    "descripcion_entrada": "confirmed email",
                    "descripcion_salida": ""
                },
                {
                    "name": "history_id",
                    "type": "AutoField",
                    "related_model": "",
                    "descripcion_entrada": "history id",
                    "descripcion_salida": ""
                },
                {
                    "name": "history_date",
                    "type": "DateTimeField",
                    "related_model": "",
                    "descripcion_entrada": "history date",
                    "descripcion_salida": ""
                },
                {
                    "name": "history_change_reason",
                    "type": "CharField",
                    "related_model": "",
                    "descripcion_entrada": "history change reason",
                    "descripcion_salida": ""
                },
                {
                    "name": "history_type",
                    "type": "CharField",
                    "related_model": "",
                    "descripcion_entrada": "history type",
                    "descripcion_salida": ""
                },
                {
                    "name": "history_user",
                    "type": "ForeignKey",
                    "related_model": "User",
                    "descripcion_entrada": "history user",
                    "descripcion_salida": ""
                }
            ],
            "modeloLower": "historicaluser",
            "modelo_labelSingular": "HistoricalUser",
            "modelo_labelPlurar": "HistoricalUser",
            "modeloLower_labelSingular": "HistoricalUser",
            "modeloLower_labelPlurar": "HistoricalUser",
            "codigos": {
                "create": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "HistoricalUserSerializer_Create"
                },
                "list": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "HistoricalUserSerializer_List"
                },
                "edit": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "HistoricalUserSerializer_Update"
                },
                "destroy": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "HistoricalUserSerializer_Destroy"
                },
                "view": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "HistoricalUserSerializer_Retrieve"
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
                    "descripcion_salida": ""
                },
                {
                    "name": "password",
                    "type": "CharField",
                    "related_model": "",
                    "descripcion_entrada": "contrase\u00f1a",
                    "descripcion_salida": ""
                },
                {
                    "name": "last_login",
                    "type": "DateTimeField",
                    "related_model": "",
                    "descripcion_entrada": "\u00faltimo ingreso",
                    "descripcion_salida": ""
                },
                {
                    "name": "is_superuser",
                    "type": "BooleanField",
                    "related_model": "",
                    "descripcion_entrada": "es superusuario",
                    "descripcion_salida": ""
                },
                {
                    "name": "username",
                    "type": "CharField",
                    "related_model": "",
                    "descripcion_entrada": "username",
                    "descripcion_salida": ""
                },
                {
                    "name": "email",
                    "type": "EmailField",
                    "related_model": "",
                    "descripcion_entrada": "email",
                    "descripcion_salida": ""
                },
                {
                    "name": "first_name",
                    "type": "CharField",
                    "related_model": "",
                    "descripcion_entrada": "first name",
                    "descripcion_salida": ""
                },
                {
                    "name": "last_name",
                    "type": "CharField",
                    "related_model": "",
                    "descripcion_entrada": "last name",
                    "descripcion_salida": ""
                },
                {
                    "name": "phone",
                    "type": "CharField",
                    "related_model": "",
                    "descripcion_entrada": "phone",
                    "descripcion_salida": ""
                },
                {
                    "name": "address",
                    "type": "CharField",
                    "related_model": "",
                    "descripcion_entrada": "address",
                    "descripcion_salida": ""
                },
                {
                    "name": "postal_code",
                    "type": "CharField",
                    "related_model": "",
                    "descripcion_entrada": "postal code",
                    "descripcion_salida": ""
                },
                {
                    "name": "is_active",
                    "type": "BooleanField",
                    "related_model": "",
                    "descripcion_entrada": "is active",
                    "descripcion_salida": ""
                },
                {
                    "name": "is_staff",
                    "type": "BooleanField",
                    "related_model": "",
                    "descripcion_entrada": "is staff",
                    "descripcion_salida": ""
                },
                {
                    "name": "confirmed_email",
                    "type": "BooleanField",
                    "related_model": "",
                    "descripcion_entrada": "confirmed email",
                    "descripcion_salida": ""
                },
                {
                    "name": "groups",
                    "type": "ManyToManyField",
                    "related_model": "Group",
                    "descripcion_entrada": "grupos",
                    "descripcion_salida": ""
                },
                {
                    "name": "user_permissions",
                    "type": "ManyToManyField",
                    "related_model": "Permission",
                    "descripcion_entrada": "permisos de usuario",
                    "descripcion_salida": ""
                },
                {
                    "name": "+",
                    "type": "Extra_ForeignKey",
                    "related_model": "HistoricalUser",
                    "descripcion_entrada": "Relacion HistoricalUser",
                    "descripcion_salida": ""
                },
                {
                    "name": "token_user",
                    "type": "Extra_ForeignKey",
                    "related_model": "BlackListedTokenAccess",
                    "descripcion_entrada": "Relacion BlackListedTokenAccess",
                    "descripcion_salida": ""
                },
                {
                    "name": "email_token_user",
                    "type": "Extra_ForeignKey",
                    "related_model": "EmailConfirmationToken",
                    "descripcion_entrada": "Relacion EmailConfirmationToken",
                    "descripcion_salida": ""
                },
                {
                    "name": "email_change_password_token_user",
                    "type": "Extra_ForeignKey",
                    "related_model": "EmailChangePasswordToken",
                    "descripcion_entrada": "Relacion EmailChangePasswordToken",
                    "descripcion_salida": ""
                },
                {
                    "name": "user_in_remittance",
                    "type": "Extra_ForeignKey",
                    "related_model": "Card",
                    "descripcion_entrada": "Relacion Card",
                    "descripcion_salida": ""
                },
                {
                    "name": "sender_id_in_remittance",
                    "type": "Extra_ForeignKey",
                    "related_model": "Remittance",
                    "descripcion_entrada": "Relacion Remittance",
                    "descripcion_salida": ""
                },
                {
                    "name": "user_in_payment_made",
                    "type": "Extra_ForeignKey",
                    "related_model": "PaymentMade",
                    "descripcion_entrada": "Relacion PaymentMade",
                    "descripcion_salida": ""
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
        "BlackListedTokenAccess": {
            "campos": [
                {
                    "name": "id",
                    "type": "BigAutoField",
                    "related_model": "",
                    "descripcion_entrada": "ID",
                    "descripcion_salida": ""
                },
                {
                    "name": "token",
                    "type": "CharField",
                    "related_model": "",
                    "descripcion_entrada": "token",
                    "descripcion_salida": ""
                },
                {
                    "name": "user",
                    "type": "ForeignKey",
                    "related_model": "User",
                    "descripcion_entrada": "user",
                    "descripcion_salida": ""
                },
                {
                    "name": "timestamp",
                    "type": "DateTimeField",
                    "related_model": "",
                    "descripcion_entrada": "timestamp",
                    "descripcion_salida": ""
                }
            ],
            "modeloLower": "blacklistedtokenaccess",
            "modelo_labelSingular": "BlackListedTokenAccess",
            "modelo_labelPlurar": "BlackListedTokenAccess",
            "modeloLower_labelSingular": "BlackListedTokenAccess",
            "modeloLower_labelPlurar": "BlackListedTokenAccess",
            "codigos": {
                "create": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "BlackListedTokenAccessSerializer_Create"
                },
                "list": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "BlackListedTokenAccessSerializer_List"
                },
                "edit": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "BlackListedTokenAccessSerializer_Update"
                },
                "destroy": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "BlackListedTokenAccessSerializer_Destroy"
                },
                "view": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "BlackListedTokenAccessSerializer_Retrieve"
                }
            }
        },
        "EmailConfirmationToken": {
            "campos": [
                {
                    "name": "id",
                    "type": "BigAutoField",
                    "related_model": "",
                    "descripcion_entrada": "ID",
                    "descripcion_salida": ""
                },
                {
                    "name": "token",
                    "type": "CharField",
                    "related_model": "",
                    "descripcion_entrada": "token",
                    "descripcion_salida": ""
                },
                {
                    "name": "user",
                    "type": "ForeignKey",
                    "related_model": "User",
                    "descripcion_entrada": "user",
                    "descripcion_salida": ""
                },
                {
                    "name": "email",
                    "type": "EmailField",
                    "related_model": "",
                    "descripcion_entrada": "email",
                    "descripcion_salida": ""
                },
                {
                    "name": "created",
                    "type": "DateTimeField",
                    "related_model": "",
                    "descripcion_entrada": "created",
                    "descripcion_salida": ""
                },
                {
                    "name": "banned",
                    "type": "BooleanField",
                    "related_model": "",
                    "descripcion_entrada": "banned",
                    "descripcion_salida": ""
                }
            ],
            "modeloLower": "emailconfirmationtoken",
            "modelo_labelSingular": "EmailConfirmationToken",
            "modelo_labelPlurar": "EmailConfirmationToken",
            "modeloLower_labelSingular": "EmailConfirmationToken",
            "modeloLower_labelPlurar": "EmailConfirmationToken",
            "codigos": {
                "create": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "EmailConfirmationTokenSerializer_Create"
                },
                "list": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "EmailConfirmationTokenSerializer_List"
                },
                "edit": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "EmailConfirmationTokenSerializer_Update"
                },
                "destroy": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "EmailConfirmationTokenSerializer_Destroy"
                },
                "view": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "EmailConfirmationTokenSerializer_Retrieve"
                }
            }
        },
        "EmailChangePasswordToken": {
            "campos": [
                {
                    "name": "id",
                    "type": "BigAutoField",
                    "related_model": "",
                    "descripcion_entrada": "ID",
                    "descripcion_salida": ""
                },
                {
                    "name": "token",
                    "type": "CharField",
                    "related_model": "",
                    "descripcion_entrada": "token",
                    "descripcion_salida": ""
                },
                {
                    "name": "user",
                    "type": "ForeignKey",
                    "related_model": "User",
                    "descripcion_entrada": "user",
                    "descripcion_salida": ""
                },
                {
                    "name": "email",
                    "type": "EmailField",
                    "related_model": "",
                    "descripcion_entrada": "email",
                    "descripcion_salida": ""
                },
                {
                    "name": "created",
                    "type": "DateTimeField",
                    "related_model": "",
                    "descripcion_entrada": "created",
                    "descripcion_salida": ""
                },
                {
                    "name": "banned",
                    "type": "BooleanField",
                    "related_model": "",
                    "descripcion_entrada": "banned",
                    "descripcion_salida": ""
                }
            ],
            "modeloLower": "emailchangepasswordtoken",
            "modelo_labelSingular": "EmailChangePasswordToken",
            "modelo_labelPlurar": "EmailChangePasswordToken",
            "modeloLower_labelSingular": "EmailChangePasswordToken",
            "modeloLower_labelPlurar": "EmailChangePasswordToken",
            "codigos": {
                "create": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "EmailChangePasswordTokenSerializer_Create"
                },
                "list": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "EmailChangePasswordTokenSerializer_List"
                },
                "edit": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "EmailChangePasswordTokenSerializer_Update"
                },
                "destroy": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "EmailChangePasswordTokenSerializer_Destroy"
                },
                "view": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "EmailChangePasswordTokenSerializer_Retrieve"
                }
            }
        },
        "TypeCard": {
            "campos": [
                {
                    "name": "id",
                    "type": "BigAutoField",
                    "related_model": "",
                    "descripcion_entrada": "ID",
                    "descripcion_salida": ""
                },
                {
                    "name": "type",
                    "type": "CharField",
                    "related_model": "",
                    "descripcion_entrada": "type",
                    "descripcion_salida": ""
                },
                {
                    "name": "description",
                    "type": "TextField",
                    "related_model": "",
                    "descripcion_entrada": "description",
                    "descripcion_salida": ""
                },
                {
                    "name": "None",
                    "type": "Extra_ForeignKey",
                    "related_model": "Card",
                    "descripcion_entrada": "Relacion Card",
                    "descripcion_salida": ""
                }
            ],
            "modeloLower": "typecard",
            "modelo_labelSingular": "TypeCard",
            "modelo_labelPlurar": "TypeCard",
            "modeloLower_labelSingular": "TypeCard",
            "modeloLower_labelPlurar": "TypeCard",
            "codigos": {
                "create": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "TypeCardSerializer_Create"
                },
                "list": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "TypeCardSerializer_List"
                },
                "edit": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "TypeCardSerializer_Update"
                },
                "destroy": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "TypeCardSerializer_Destroy"
                },
                "view": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "TypeCardSerializer_Retrieve"
                }
            }
        },
        "Card": {
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
                    "descripcion_entrada": "name",
                    "descripcion_salida": ""
                },
                {
                    "name": "type",
                    "type": "ForeignKey",
                    "related_model": "TypeCard",
                    "descripcion_entrada": "type",
                    "descripcion_salida": ""
                },
                {
                    "name": "bank",
                    "type": "CharField",
                    "related_model": "",
                    "descripcion_entrada": "bank",
                    "descripcion_salida": ""
                },
                {
                    "name": "description",
                    "type": "TextField",
                    "related_model": "",
                    "descripcion_entrada": "description",
                    "descripcion_salida": ""
                },
                {
                    "name": "user",
                    "type": "ForeignKey",
                    "related_model": "User",
                    "descripcion_entrada": "user",
                    "descripcion_salida": ""
                },
                {
                    "name": "banned",
                    "type": "BooleanField",
                    "related_model": "",
                    "descripcion_entrada": "banned",
                    "descripcion_salida": ""
                }
            ],
            "modeloLower": "card",
            "modelo_labelSingular": "Card",
            "modelo_labelPlurar": "Card",
            "modeloLower_labelSingular": "Card",
            "modeloLower_labelPlurar": "Card",
            "codigos": {
                "create": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "CardSerializer_Create"
                },
                "list": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "CardSerializer_List"
                },
                "edit": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "CardSerializer_Update"
                },
                "destroy": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "CardSerializer_Destroy"
                },
                "view": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "CardSerializer_Retrieve"
                }
            }
        },
        "TypeRemittance": {
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
                    "descripcion_entrada": "description",
                    "descripcion_salida": ""
                },
                {
                    "name": "remittance_type",
                    "type": "CharField",
                    "related_model": "",
                    "descripcion_entrada": "remittance type",
                    "descripcion_salida": ""
                },
                {
                    "name": "destination",
                    "type": "CharField",
                    "related_model": "",
                    "descripcion_entrada": "destination",
                    "descripcion_salida": ""
                },
                {
                    "name": "currency",
                    "type": "CharField",
                    "related_model": "",
                    "descripcion_entrada": "currency",
                    "descripcion_salida": ""
                },
                {
                    "name": "minimum_amount",
                    "type": "IntegerField",
                    "related_model": "",
                    "descripcion_entrada": "minimum amount",
                    "descripcion_salida": ""
                },
                {
                    "name": "maximum_amount",
                    "type": "IntegerField",
                    "related_model": "",
                    "descripcion_entrada": "maximum amount",
                    "descripcion_salida": ""
                },
                {
                    "name": "commission",
                    "type": "FloatField",
                    "related_model": "",
                    "descripcion_entrada": "commission",
                    "descripcion_salida": ""
                },
                {
                    "name": "due_date",
                    "type": "DateField",
                    "related_model": "",
                    "descripcion_entrada": "due date",
                    "descripcion_salida": ""
                }
            ],
            "modeloLower": "typeremittance",
            "modelo_labelSingular": "TypeRemittance",
            "modelo_labelPlurar": "TypeRemittance",
            "modeloLower_labelSingular": "TypeRemittance",
            "modeloLower_labelPlurar": "TypeRemittance",
            "codigos": {
                "create": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "TypeRemittanceSerializer_Create"
                },
                "list": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "TypeRemittanceSerializer_List"
                },
                "edit": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "TypeRemittanceSerializer_Update"
                },
                "destroy": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "TypeRemittanceSerializer_Destroy"
                },
                "view": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "TypeRemittanceSerializer_Retrieve"
                }
            }
        },
        "Remittance": {
            "campos": [
                {
                    "name": "id",
                    "type": "BigAutoField",
                    "related_model": "",
                    "descripcion_entrada": "ID",
                    "descripcion_salida": ""
                },
                {
                    "name": "sender_id",
                    "type": "ForeignKey",
                    "related_model": "User",
                    "descripcion_entrada": "sender id",
                    "descripcion_salida": ""
                },
                {
                    "name": "reciver_name",
                    "type": "CharField",
                    "related_model": "",
                    "descripcion_entrada": "reciver name",
                    "descripcion_salida": ""
                },
                {
                    "name": "reciver_address",
                    "type": "CharField",
                    "related_model": "",
                    "descripcion_entrada": "reciver address",
                    "descripcion_salida": ""
                },
                {
                    "name": "reciver_postal_code",
                    "type": "CharField",
                    "related_model": "",
                    "descripcion_entrada": "reciver postal code",
                    "descripcion_salida": ""
                },
                {
                    "name": "reciver_phone",
                    "type": "CharField",
                    "related_model": "",
                    "descripcion_entrada": "reciver phone",
                    "descripcion_salida": ""
                },
                {
                    "name": "reciver_card",
                    "type": "CharField",
                    "related_model": "",
                    "descripcion_entrada": "reciver card",
                    "descripcion_salida": ""
                },
                {
                    "name": "ammount",
                    "type": "FloatField",
                    "related_model": "",
                    "descripcion_entrada": "ammount",
                    "descripcion_salida": ""
                },
                {
                    "name": "description",
                    "type": "TextField",
                    "related_model": "",
                    "descripcion_entrada": "description",
                    "descripcion_salida": ""
                },
                {
                    "name": "shipping_type",
                    "type": "CharField",
                    "related_model": "",
                    "descripcion_entrada": "shipping type",
                    "descripcion_salida": ""
                },
                {
                    "name": "delivery_type",
                    "type": "CharField",
                    "related_model": "",
                    "descripcion_entrada": "delivery type",
                    "descripcion_salida": ""
                }
            ],
            "modeloLower": "remittance",
            "modelo_labelSingular": "Remittance",
            "modelo_labelPlurar": "Remittance",
            "modeloLower_labelSingular": "Remittance",
            "modeloLower_labelPlurar": "Remittance",
            "codigos": {
                "create": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "RemittanceSerializer_Create"
                },
                "list": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "RemittanceSerializer_List"
                },
                "edit": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "RemittanceSerializer_Update"
                },
                "destroy": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "RemittanceSerializer_Destroy"
                },
                "view": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "RemittanceSerializer_Retrieve"
                }
            }
        },
        "PaymentMade": {
            "campos": [
                {
                    "name": "id",
                    "type": "BigAutoField",
                    "related_model": "",
                    "descripcion_entrada": "ID",
                    "descripcion_salida": ""
                },
                {
                    "name": "date",
                    "type": "DateField",
                    "related_model": "",
                    "descripcion_entrada": "date",
                    "descripcion_salida": ""
                },
                {
                    "name": "total_payment_amount",
                    "type": "DecimalField",
                    "related_model": "",
                    "descripcion_entrada": "total payment amount",
                    "descripcion_salida": ""
                },
                {
                    "name": "beneficiary_card_number",
                    "type": "CharField",
                    "related_model": "",
                    "descripcion_entrada": "beneficiary card number",
                    "descripcion_salida": ""
                },
                {
                    "name": "beneficiary_address",
                    "type": "CharField",
                    "related_model": "",
                    "descripcion_entrada": "beneficiary address",
                    "descripcion_salida": ""
                },
                {
                    "name": "beneficiary_total_amount",
                    "type": "IntegerField",
                    "related_model": "",
                    "descripcion_entrada": "beneficiary total amount",
                    "descripcion_salida": ""
                },
                {
                    "name": "beneficiary_full_name",
                    "type": "CharField",
                    "related_model": "",
                    "descripcion_entrada": "beneficiary full name",
                    "descripcion_salida": ""
                },
                {
                    "name": "beneficiary_telephone_number",
                    "type": "CharField",
                    "related_model": "",
                    "descripcion_entrada": "beneficiary telephone number",
                    "descripcion_salida": ""
                },
                {
                    "name": "currency",
                    "type": "CharField",
                    "related_model": "",
                    "descripcion_entrada": "currency",
                    "descripcion_salida": ""
                },
                {
                    "name": "commission",
                    "type": "DecimalField",
                    "related_model": "",
                    "descripcion_entrada": "commission",
                    "descripcion_salida": ""
                },
                {
                    "name": "status",
                    "type": "CharField",
                    "related_model": "",
                    "descripcion_entrada": "status",
                    "descripcion_salida": ""
                },
                {
                    "name": "shipping_type",
                    "type": "CharField",
                    "related_model": "",
                    "descripcion_entrada": "shipping type",
                    "descripcion_salida": ""
                },
                {
                    "name": "delivery_type",
                    "type": "CharField",
                    "related_model": "",
                    "descripcion_entrada": "delivery type",
                    "descripcion_salida": ""
                },
                {
                    "name": "exchange_rate",
                    "type": "IntegerField",
                    "related_model": "",
                    "descripcion_entrada": "exchange rate",
                    "descripcion_salida": ""
                },
                {
                    "name": "user",
                    "type": "ForeignKey",
                    "related_model": "User",
                    "descripcion_entrada": "user",
                    "descripcion_salida": ""
                }
            ],
            "modeloLower": "paymentmade",
            "modelo_labelSingular": "PaymentMade",
            "modelo_labelPlurar": "PaymentMade",
            "modeloLower_labelSingular": "PaymentMade",
            "modeloLower_labelPlurar": "PaymentMade",
            "codigos": {
                "create": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "PaymentMadeSerializer_Create"
                },
                "list": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "PaymentMadeSerializer_List"
                },
                "edit": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "PaymentMadeSerializer_Update"
                },
                "destroy": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "PaymentMadeSerializer_Destroy"
                },
                "view": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "PaymentMadeSerializer_Retrieve"
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
        "BigIntegerField",
        "DateTimeField",
        "BooleanField",
        "EmailField",
        "BigAutoField",
        "TextField",
        "IntegerField",
        "FloatField",
        "DateField",
        "DecimalField"
    ]
}




