datos={
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
                    "name": "None",
                    "type": "Extra_ForeignKey",
                    "related_model": "Card",
                    "descripcion_entrada": "Relacion Card",
                    "descripcion_salida": ""
                },
                {
                    "name": "None",
                    "type": "Extra_ForeignKey",
                    "related_model": "OwnCard",
                    "descripcion_entrada": "Relacion OwnCard",
                    "descripcion_salida": ""
                },
                {
                    "name": "None",
                    "type": "Extra_ForeignKey",
                    "related_model": "Contact",
                    "descripcion_entrada": "Relacion Contact",
                    "descripcion_salida": ""
                },
                {
                    "name": "None",
                    "type": "Extra_ForeignKey",
                    "related_model": "TypeRemittance",
                    "descripcion_entrada": "Relacion TypeRemittance",
                    "descripcion_salida": ""
                },
                {
                    "name": "None",
                    "type": "Extra_ForeignKey",
                    "related_model": "RemittanceOffer",
                    "descripcion_entrada": "Relacion RemittanceOffer",
                    "descripcion_salida": ""
                },
                {
                    "name": "sender_id_in_planned_remittance",
                    "type": "Extra_ForeignKey",
                    "related_model": "PlannedRemittance",
                    "descripcion_entrada": "Relacion PlannedRemittance",
                    "descripcion_salida": ""
                },
                {
                    "name": "reseller_id_in_planned_remittance",
                    "type": "Extra_ForeignKey",
                    "related_model": "PlannedRemittance",
                    "descripcion_entrada": "Relacion PlannedRemittance",
                    "descripcion_salida": ""
                },
                {
                    "name": "origin_user_in_card_transaction",
                    "type": "Extra_ForeignKey",
                    "related_model": "CardTransaction",
                    "descripcion_entrada": "Relacion CardTransaction",
                    "descripcion_salida": ""
                },
                {
                    "name": "destination_user_in_card_transaction",
                    "type": "Extra_ForeignKey",
                    "related_model": "CardTransaction",
                    "descripcion_entrada": "Relacion CardTransaction",
                    "descripcion_salida": ""
                },
                {
                    "name": "reseller_id_in_made_remittance",
                    "type": "Extra_ForeignKey",
                    "related_model": "MadeRemittance",
                    "descripcion_entrada": "Relacion MadeRemittance",
                    "descripcion_salida": ""
                },
                {
                    "name": "sender_id_in_made_remittance",
                    "type": "Extra_ForeignKey",
                    "related_model": "MadeRemittance",
                    "descripcion_entrada": "Relacion MadeRemittance",
                    "descripcion_salida": ""
                },
                {
                    "name": "reseller_id_in_payment_made",
                    "type": "Extra_ForeignKey",
                    "related_model": "PaymentMade",
                    "descripcion_entrada": "Relacion PaymentMade",
                    "descripcion_salida": ""
                },
                {
                    "name": "None",
                    "type": "Extra_ForeignKey",
                    "related_model": "ResellerApplication",
                    "descripcion_entrada": "Relacion ResellerApplication",
                    "descripcion_salida": ""
                },
                {
                    "name": "None",
                    "type": "Extra_ForeignKey",
                    "related_model": "RemittanceRefund",
                    "descripcion_entrada": "Relacion RemittanceRefund",
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
                },
                {
                    "name": "card_number",
                    "type": "CharField",
                    "related_model": "",
                    "descripcion_entrada": "card number",
                    "descripcion_salida": ""
                },
                {
                    "name": "None",
                    "type": "Extra_ForeignKey",
                    "related_model": "OwnCard",
                    "descripcion_entrada": "Relacion OwnCard",
                    "descripcion_salida": ""
                },
                {
                    "name": "None",
                    "type": "Extra_ForeignKey",
                    "related_model": "CardContact",
                    "descripcion_entrada": "Relacion CardContact",
                    "descripcion_salida": ""
                },
                {
                    "name": "None",
                    "type": "Extra_ManyToManyField",
                    "related_model": "RemittanceOffer",
                    "descripcion_entrada": "Relacion RemittanceOffer",
                    "descripcion_salida": ""
                },
                {
                    "name": "origin_card_in_card_transaction",
                    "type": "Extra_ForeignKey",
                    "related_model": "CardTransaction",
                    "descripcion_entrada": "Relacion CardTransaction",
                    "descripcion_salida": ""
                },
                {
                    "name": "destination_card_in_card_transaction",
                    "type": "Extra_ForeignKey",
                    "related_model": "CardTransaction",
                    "descripcion_entrada": "Relacion CardTransaction",
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
        "OwnCard": {
            "campos": [
                {
                    "name": "id",
                    "type": "BigAutoField",
                    "related_model": "",
                    "descripcion_entrada": "ID",
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
                    "name": "card",
                    "type": "ForeignKey",
                    "related_model": "Card",
                    "descripcion_entrada": "card",
                    "descripcion_salida": ""
                }
            ],
            "modeloLower": "owncard",
            "modelo_labelSingular": "OwnCard",
            "modelo_labelPlurar": "OwnCard",
            "modeloLower_labelSingular": "OwnCard",
            "modeloLower_labelPlurar": "OwnCard",
            "codigos": {
                "create": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "OwnCardSerializer_Create"
                },
                "list": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "OwnCardSerializer_List"
                },
                "edit": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "OwnCardSerializer_Update"
                },
                "destroy": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "OwnCardSerializer_Destroy"
                },
                "view": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "OwnCardSerializer_Retrieve"
                }
            }
        },
        "Contact": {
            "campos": [
                {
                    "name": "id",
                    "type": "BigAutoField",
                    "related_model": "",
                    "descripcion_entrada": "ID",
                    "descripcion_salida": ""
                },
                {
                    "name": "full_name",
                    "type": "CharField",
                    "related_model": "",
                    "descripcion_entrada": "full name",
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
                    "name": "phone",
                    "type": "CharField",
                    "related_model": "",
                    "descripcion_entrada": "phone",
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
                    "name": "None",
                    "type": "Extra_ForeignKey",
                    "related_model": "CardContact",
                    "descripcion_entrada": "Relacion CardContact",
                    "descripcion_salida": ""
                }
            ],
            "modeloLower": "contact",
            "modelo_labelSingular": "Contact",
            "modelo_labelPlurar": "Contact",
            "modeloLower_labelSingular": "Contact",
            "modeloLower_labelPlurar": "Contact",
            "codigos": {
                "create": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "ContactSerializer_Create"
                },
                "list": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "ContactSerializer_List"
                },
                "edit": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "ContactSerializer_Update"
                },
                "destroy": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "ContactSerializer_Destroy"
                },
                "view": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "ContactSerializer_Retrieve"
                }
            }
        },
        "CardContact": {
            "campos": [
                {
                    "name": "id",
                    "type": "BigAutoField",
                    "related_model": "",
                    "descripcion_entrada": "ID",
                    "descripcion_salida": ""
                },
                {
                    "name": "card",
                    "type": "ForeignKey",
                    "related_model": "Card",
                    "descripcion_entrada": "card",
                    "descripcion_salida": ""
                },
                {
                    "name": "contact",
                    "type": "ForeignKey",
                    "related_model": "Contact",
                    "descripcion_entrada": "contact",
                    "descripcion_salida": ""
                }
            ],
            "modeloLower": "cardcontact",
            "modelo_labelSingular": "CardContact",
            "modelo_labelPlurar": "CardContact",
            "modeloLower_labelSingular": "CardContact",
            "modeloLower_labelPlurar": "CardContact",
            "codigos": {
                "create": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "CardContactSerializer_Create"
                },
                "list": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "CardContactSerializer_List"
                },
                "edit": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "CardContactSerializer_Update"
                },
                "destroy": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "CardContactSerializer_Destroy"
                },
                "view": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "CardContactSerializer_Retrieve"
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
                },
                {
                    "name": "user",
                    "type": "ForeignKey",
                    "related_model": "User",
                    "descripcion_entrada": "user",
                    "descripcion_salida": ""
                },
                {
                    "name": "None",
                    "type": "Extra_ForeignKey",
                    "related_model": "CommissionTypePercentage",
                    "descripcion_entrada": "Relacion CommissionTypePercentage",
                    "descripcion_salida": ""
                },
                {
                    "name": "None",
                    "type": "Extra_ForeignKey",
                    "related_model": "CommissionTypeAmount",
                    "descripcion_entrada": "Relacion CommissionTypeAmount",
                    "descripcion_salida": ""
                },
                {
                    "name": "None",
                    "type": "Extra_ForeignKey",
                    "related_model": "RemittanceOffer",
                    "descripcion_entrada": "Relacion RemittanceOffer",
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
        "CommissionTypePercentage": {
            "campos": [
                {
                    "name": "id",
                    "type": "BigAutoField",
                    "related_model": "",
                    "descripcion_entrada": "ID",
                    "descripcion_salida": ""
                },
                {
                    "name": "percentage",
                    "type": "FloatField",
                    "related_model": "",
                    "descripcion_entrada": "percentage",
                    "descripcion_salida": ""
                },
                {
                    "name": "type_remittance",
                    "type": "ForeignKey",
                    "related_model": "TypeRemittance",
                    "descripcion_entrada": "type remittance",
                    "descripcion_salida": ""
                }
            ],
            "modeloLower": "commissiontypepercentage",
            "modelo_labelSingular": "CommissionTypePercentage",
            "modelo_labelPlurar": "CommissionTypePercentage",
            "modeloLower_labelSingular": "CommissionTypePercentage",
            "modeloLower_labelPlurar": "CommissionTypePercentage",
            "codigos": {
                "create": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "CommissionTypePercentageSerializer_Create"
                },
                "list": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "CommissionTypePercentageSerializer_List"
                },
                "edit": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "CommissionTypePercentageSerializer_Update"
                },
                "destroy": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "CommissionTypePercentageSerializer_Destroy"
                },
                "view": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "CommissionTypePercentageSerializer_Retrieve"
                }
            }
        },
        "CommissionTypeAmount": {
            "campos": [
                {
                    "name": "id",
                    "type": "BigAutoField",
                    "related_model": "",
                    "descripcion_entrada": "ID",
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
                    "name": "currency",
                    "type": "CharField",
                    "related_model": "",
                    "descripcion_entrada": "currency",
                    "descripcion_salida": ""
                },
                {
                    "name": "type_remittance",
                    "type": "ForeignKey",
                    "related_model": "TypeRemittance",
                    "descripcion_entrada": "type remittance",
                    "descripcion_salida": ""
                }
            ],
            "modeloLower": "commissiontypeamount",
            "modelo_labelSingular": "CommissionTypeAmount",
            "modelo_labelPlurar": "CommissionTypeAmount",
            "modeloLower_labelSingular": "CommissionTypeAmount",
            "modeloLower_labelPlurar": "CommissionTypeAmount",
            "codigos": {
                "create": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "CommissionTypeAmountSerializer_Create"
                },
                "list": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "CommissionTypeAmountSerializer_List"
                },
                "edit": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "CommissionTypeAmountSerializer_Update"
                },
                "destroy": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "CommissionTypeAmountSerializer_Destroy"
                },
                "view": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "CommissionTypeAmountSerializer_Retrieve"
                }
            }
        },
        "RemittanceOffer": {
            "campos": [
                {
                    "name": "id",
                    "type": "BigAutoField",
                    "related_model": "",
                    "descripcion_entrada": "ID",
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
                    "name": "type_remittance",
                    "type": "ForeignKey",
                    "related_model": "TypeRemittance",
                    "descripcion_entrada": "type remittance",
                    "descripcion_salida": ""
                },
                {
                    "name": "cards",
                    "type": "ManyToManyField",
                    "related_model": "Card",
                    "descripcion_entrada": "cards",
                    "descripcion_salida": ""
                },
                {
                    "name": "None",
                    "type": "Extra_ForeignKey",
                    "related_model": "RemittanceOfferDiscount",
                    "descripcion_entrada": "Relacion RemittanceOfferDiscount",
                    "descripcion_salida": ""
                },
                {
                    "name": "None",
                    "type": "Extra_ForeignKey",
                    "related_model": "PlannedRemittance",
                    "descripcion_entrada": "Relacion PlannedRemittance",
                    "descripcion_salida": ""
                }
            ],
            "modeloLower": "remittanceoffer",
            "modelo_labelSingular": "RemittanceOffer",
            "modelo_labelPlurar": "RemittanceOffer",
            "modeloLower_labelSingular": "RemittanceOffer",
            "modeloLower_labelPlurar": "RemittanceOffer",
            "codigos": {
                "create": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "RemittanceOfferSerializer_Create"
                },
                "list": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "RemittanceOfferSerializer_List"
                },
                "edit": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "RemittanceOfferSerializer_Update"
                },
                "destroy": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "RemittanceOfferSerializer_Destroy"
                },
                "view": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "RemittanceOfferSerializer_Retrieve"
                }
            }
        },
        "RemittanceOfferDiscount": {
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
                    "name": "description",
                    "type": "TextField",
                    "related_model": "",
                    "descripcion_entrada": "description",
                    "descripcion_salida": ""
                },
                {
                    "name": "remittance_offer",
                    "type": "ForeignKey",
                    "related_model": "RemittanceOffer",
                    "descripcion_entrada": "remittance offer",
                    "descripcion_salida": ""
                },
                {
                    "name": "only_automatic_remittances",
                    "type": "BooleanField",
                    "related_model": "",
                    "descripcion_entrada": "only automatic remittances",
                    "descripcion_salida": ""
                },
                {
                    "name": "None",
                    "type": "Extra_ForeignKey",
                    "related_model": "RemittanceOfferDiscountTypePercentage",
                    "descripcion_entrada": "Relacion RemittanceOfferDiscountTypePercentage",
                    "descripcion_salida": ""
                },
                {
                    "name": "None",
                    "type": "Extra_ForeignKey",
                    "related_model": "RemittanceOfferDiscountAmount",
                    "descripcion_entrada": "Relacion RemittanceOfferDiscountAmount",
                    "descripcion_salida": ""
                },
                {
                    "name": "None",
                    "type": "Extra_ForeignKey",
                    "related_model": "RemittanceDiscountTypeThresholdAmount",
                    "descripcion_entrada": "Relacion RemittanceDiscountTypeThresholdAmount",
                    "descripcion_salida": ""
                },
                {
                    "name": "None",
                    "type": "Extra_ForeignKey",
                    "related_model": "RemittanceOfferDiscountFrequency",
                    "descripcion_entrada": "Relacion RemittanceOfferDiscountFrequency",
                    "descripcion_salida": ""
                },
                {
                    "name": "None",
                    "type": "Extra_ForeignKey",
                    "related_model": "RemittanceOfferDiscountSchedule",
                    "descripcion_entrada": "Relacion RemittanceOfferDiscountSchedule",
                    "descripcion_salida": ""
                }
            ],
            "modeloLower": "remittanceofferdiscount",
            "modelo_labelSingular": "RemittanceOfferDiscount",
            "modelo_labelPlurar": "RemittanceOfferDiscount",
            "modeloLower_labelSingular": "RemittanceOfferDiscount",
            "modeloLower_labelPlurar": "RemittanceOfferDiscount",
            "codigos": {
                "create": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "RemittanceOfferDiscountSerializer_Create"
                },
                "list": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "RemittanceOfferDiscountSerializer_List"
                },
                "edit": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "RemittanceOfferDiscountSerializer_Update"
                },
                "destroy": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "RemittanceOfferDiscountSerializer_Destroy"
                },
                "view": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "RemittanceOfferDiscountSerializer_Retrieve"
                }
            }
        },
        "RemittanceOfferDiscountTypePercentage": {
            "campos": [
                {
                    "name": "id",
                    "type": "BigAutoField",
                    "related_model": "",
                    "descripcion_entrada": "ID",
                    "descripcion_salida": ""
                },
                {
                    "name": "percentage",
                    "type": "FloatField",
                    "related_model": "",
                    "descripcion_entrada": "percentage",
                    "descripcion_salida": ""
                },
                {
                    "name": "remittance_offer_discount",
                    "type": "ForeignKey",
                    "related_model": "RemittanceOfferDiscount",
                    "descripcion_entrada": "remittance offer discount",
                    "descripcion_salida": ""
                }
            ],
            "modeloLower": "remittanceofferdiscounttypepercentage",
            "modelo_labelSingular": "RemittanceOfferDiscountTypePercentage",
            "modelo_labelPlurar": "RemittanceOfferDiscountTypePercentage",
            "modeloLower_labelSingular": "RemittanceOfferDiscountTypePercentage",
            "modeloLower_labelPlurar": "RemittanceOfferDiscountTypePercentage",
            "codigos": {
                "create": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "RemittanceOfferDiscountTypePercentageSerializer_Create"
                },
                "list": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "RemittanceOfferDiscountTypePercentageSerializer_List"
                },
                "edit": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "RemittanceOfferDiscountTypePercentageSerializer_Update"
                },
                "destroy": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "RemittanceOfferDiscountTypePercentageSerializer_Destroy"
                },
                "view": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "RemittanceOfferDiscountTypePercentageSerializer_Retrieve"
                }
            }
        },
        "RemittanceOfferDiscountAmount": {
            "campos": [
                {
                    "name": "id",
                    "type": "BigAutoField",
                    "related_model": "",
                    "descripcion_entrada": "ID",
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
                    "name": "currency",
                    "type": "CharField",
                    "related_model": "",
                    "descripcion_entrada": "currency",
                    "descripcion_salida": ""
                },
                {
                    "name": "remittance_offer_discount",
                    "type": "ForeignKey",
                    "related_model": "RemittanceOfferDiscount",
                    "descripcion_entrada": "remittance offer discount",
                    "descripcion_salida": ""
                }
            ],
            "modeloLower": "remittanceofferdiscountamount",
            "modelo_labelSingular": "RemittanceOfferDiscountAmount",
            "modelo_labelPlurar": "RemittanceOfferDiscountAmount",
            "modeloLower_labelSingular": "RemittanceOfferDiscountAmount",
            "modeloLower_labelPlurar": "RemittanceOfferDiscountAmount",
            "codigos": {
                "create": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "RemittanceOfferDiscountAmountSerializer_Create"
                },
                "list": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "RemittanceOfferDiscountAmountSerializer_List"
                },
                "edit": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "RemittanceOfferDiscountAmountSerializer_Update"
                },
                "destroy": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "RemittanceOfferDiscountAmountSerializer_Destroy"
                },
                "view": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "RemittanceOfferDiscountAmountSerializer_Retrieve"
                }
            }
        },
        "RemittanceDiscountTypeThresholdAmount": {
            "campos": [
                {
                    "name": "id",
                    "type": "BigAutoField",
                    "related_model": "",
                    "descripcion_entrada": "ID",
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
                    "name": "threshold_currency",
                    "type": "CharField",
                    "related_model": "",
                    "descripcion_entrada": "threshold currency",
                    "descripcion_salida": ""
                },
                {
                    "name": "threshold_amount",
                    "type": "FloatField",
                    "related_model": "",
                    "descripcion_entrada": "threshold amount",
                    "descripcion_salida": ""
                },
                {
                    "name": "remittance_offer_discount",
                    "type": "ForeignKey",
                    "related_model": "RemittanceOfferDiscount",
                    "descripcion_entrada": "remittance offer discount",
                    "descripcion_salida": ""
                }
            ],
            "modeloLower": "remittancediscounttypethresholdamount",
            "modelo_labelSingular": "RemittanceDiscountTypeThresholdAmount",
            "modelo_labelPlurar": "RemittanceDiscountTypeThresholdAmount",
            "modeloLower_labelSingular": "RemittanceDiscountTypeThresholdAmount",
            "modeloLower_labelPlurar": "RemittanceDiscountTypeThresholdAmount",
            "codigos": {
                "create": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "RemittanceDiscountTypeThresholdAmountSerializer_Create"
                },
                "list": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "RemittanceDiscountTypeThresholdAmountSerializer_List"
                },
                "edit": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "RemittanceDiscountTypeThresholdAmountSerializer_Update"
                },
                "destroy": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "RemittanceDiscountTypeThresholdAmountSerializer_Destroy"
                },
                "view": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "RemittanceDiscountTypeThresholdAmountSerializer_Retrieve"
                }
            }
        },
        "RemittanceOfferDiscountFrequency": {
            "campos": [
                {
                    "name": "id",
                    "type": "BigAutoField",
                    "related_model": "",
                    "descripcion_entrada": "ID",
                    "descripcion_salida": ""
                },
                {
                    "name": "frequency",
                    "type": "FloatField",
                    "related_model": "",
                    "descripcion_entrada": "frequency",
                    "descripcion_salida": ""
                },
                {
                    "name": "remittance_offer_discount",
                    "type": "ForeignKey",
                    "related_model": "RemittanceOfferDiscount",
                    "descripcion_entrada": "remittance offer discount",
                    "descripcion_salida": ""
                }
            ],
            "modeloLower": "remittanceofferdiscountfrequency",
            "modelo_labelSingular": "RemittanceOfferDiscountFrequency",
            "modelo_labelPlurar": "RemittanceOfferDiscountFrequency",
            "modeloLower_labelSingular": "RemittanceOfferDiscountFrequency",
            "modeloLower_labelPlurar": "RemittanceOfferDiscountFrequency",
            "codigos": {
                "create": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "RemittanceOfferDiscountFrequencySerializer_Create"
                },
                "list": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "RemittanceOfferDiscountFrequencySerializer_List"
                },
                "edit": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "RemittanceOfferDiscountFrequencySerializer_Update"
                },
                "destroy": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "RemittanceOfferDiscountFrequencySerializer_Destroy"
                },
                "view": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "RemittanceOfferDiscountFrequencySerializer_Retrieve"
                }
            }
        },
        "RemittanceOfferDiscountSchedule": {
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
                    "name": "remittance_offer_discount",
                    "type": "ForeignKey",
                    "related_model": "RemittanceOfferDiscount",
                    "descripcion_entrada": "remittance offer discount",
                    "descripcion_salida": ""
                }
            ],
            "modeloLower": "remittanceofferdiscountschedule",
            "modelo_labelSingular": "RemittanceOfferDiscountSchedule",
            "modelo_labelPlurar": "RemittanceOfferDiscountSchedule",
            "modeloLower_labelSingular": "RemittanceOfferDiscountSchedule",
            "modeloLower_labelPlurar": "RemittanceOfferDiscountSchedule",
            "codigos": {
                "create": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "RemittanceOfferDiscountScheduleSerializer_Create"
                },
                "list": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "RemittanceOfferDiscountScheduleSerializer_List"
                },
                "edit": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "RemittanceOfferDiscountScheduleSerializer_Update"
                },
                "destroy": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "RemittanceOfferDiscountScheduleSerializer_Destroy"
                },
                "view": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "RemittanceOfferDiscountScheduleSerializer_Retrieve"
                }
            }
        },
        "PlannedRemittance": {
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
                    "name": "reseller_id",
                    "type": "ForeignKey",
                    "related_model": "User",
                    "descripcion_entrada": "reseller id",
                    "descripcion_salida": ""
                },
                {
                    "name": "remittance_offer",
                    "type": "ForeignKey",
                    "related_model": "RemittanceOffer",
                    "descripcion_entrada": "remittance offer",
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
                },
                {
                    "name": "its_cancelled",
                    "type": "BooleanField",
                    "related_model": "",
                    "descripcion_entrada": "its cancelled",
                    "descripcion_salida": ""
                },
                {
                    "name": "None",
                    "type": "Extra_ForeignKey",
                    "related_model": "PlannedAutomaticRemittance",
                    "descripcion_entrada": "Relacion PlannedAutomaticRemittance",
                    "descripcion_salida": ""
                },
                {
                    "name": "None",
                    "type": "Extra_ForeignKey",
                    "related_model": "PlannedAutomaticAlarmRemittance",
                    "descripcion_entrada": "Relacion PlannedAutomaticAlarmRemittance",
                    "descripcion_salida": ""
                },
                {
                    "name": "None",
                    "type": "Extra_ForeignKey",
                    "related_model": "MadeRemittance",
                    "descripcion_entrada": "Relacion MadeRemittance",
                    "descripcion_salida": ""
                }
            ],
            "modeloLower": "plannedremittance",
            "modelo_labelSingular": "PlannedRemittance",
            "modelo_labelPlurar": "PlannedRemittance",
            "modeloLower_labelSingular": "PlannedRemittance",
            "modeloLower_labelPlurar": "PlannedRemittance",
            "codigos": {
                "create": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "PlannedRemittanceSerializer_Create"
                },
                "list": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "PlannedRemittanceSerializer_List"
                },
                "edit": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "PlannedRemittanceSerializer_Update"
                },
                "destroy": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "PlannedRemittanceSerializer_Destroy"
                },
                "view": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "PlannedRemittanceSerializer_Retrieve"
                }
            }
        },
        "PlannedAutomaticRemittance": {
            "campos": [
                {
                    "name": "id",
                    "type": "BigAutoField",
                    "related_model": "",
                    "descripcion_entrada": "ID",
                    "descripcion_salida": ""
                },
                {
                    "name": "planned_remittance",
                    "type": "ForeignKey",
                    "related_model": "PlannedRemittance",
                    "descripcion_entrada": "planned remittance",
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
                    "name": "description",
                    "type": "TextField",
                    "related_model": "",
                    "descripcion_entrada": "description",
                    "descripcion_salida": ""
                },
                {
                    "name": "None",
                    "type": "Extra_ForeignKey",
                    "related_model": "PlannedAutomaticRemittanceFrequency",
                    "descripcion_entrada": "Relacion PlannedAutomaticRemittanceFrequency",
                    "descripcion_salida": ""
                },
                {
                    "name": "None",
                    "type": "Extra_ForeignKey",
                    "related_model": "PlannedAutomaticRemittanceSchedule",
                    "descripcion_entrada": "Relacion PlannedAutomaticRemittanceSchedule",
                    "descripcion_salida": ""
                }
            ],
            "modeloLower": "plannedautomaticremittance",
            "modelo_labelSingular": "PlannedAutomaticRemittance",
            "modelo_labelPlurar": "PlannedAutomaticRemittance",
            "modeloLower_labelSingular": "PlannedAutomaticRemittance",
            "modeloLower_labelPlurar": "PlannedAutomaticRemittance",
            "codigos": {
                "create": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "PlannedAutomaticRemittanceSerializer_Create"
                },
                "list": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "PlannedAutomaticRemittanceSerializer_List"
                },
                "edit": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "PlannedAutomaticRemittanceSerializer_Update"
                },
                "destroy": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "PlannedAutomaticRemittanceSerializer_Destroy"
                },
                "view": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "PlannedAutomaticRemittanceSerializer_Retrieve"
                }
            }
        },
        "PlannedAutomaticRemittanceFrequency": {
            "campos": [
                {
                    "name": "id",
                    "type": "BigAutoField",
                    "related_model": "",
                    "descripcion_entrada": "ID",
                    "descripcion_salida": ""
                },
                {
                    "name": "frequency",
                    "type": "DurationField",
                    "related_model": "",
                    "descripcion_entrada": "frequency",
                    "descripcion_salida": ""
                },
                {
                    "name": "planned_automatic_remittance",
                    "type": "ForeignKey",
                    "related_model": "PlannedAutomaticRemittance",
                    "descripcion_entrada": "planned automatic remittance",
                    "descripcion_salida": ""
                }
            ],
            "modeloLower": "plannedautomaticremittancefrequency",
            "modelo_labelSingular": "PlannedAutomaticRemittanceFrequency",
            "modelo_labelPlurar": "PlannedAutomaticRemittanceFrequency",
            "modeloLower_labelSingular": "PlannedAutomaticRemittanceFrequency",
            "modeloLower_labelPlurar": "PlannedAutomaticRemittanceFrequency",
            "codigos": {
                "create": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "PlannedAutomaticRemittanceFrequencySerializer_Create"
                },
                "list": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "PlannedAutomaticRemittanceFrequencySerializer_List"
                },
                "edit": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "PlannedAutomaticRemittanceFrequencySerializer_Update"
                },
                "destroy": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "PlannedAutomaticRemittanceFrequencySerializer_Destroy"
                },
                "view": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "PlannedAutomaticRemittanceFrequencySerializer_Retrieve"
                }
            }
        },
        "PlannedAutomaticRemittanceSchedule": {
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
                    "name": "planned_automatic_remittance",
                    "type": "ForeignKey",
                    "related_model": "PlannedAutomaticRemittance",
                    "descripcion_entrada": "planned automatic remittance",
                    "descripcion_salida": ""
                }
            ],
            "modeloLower": "plannedautomaticremittanceschedule",
            "modelo_labelSingular": "PlannedAutomaticRemittanceSchedule",
            "modelo_labelPlurar": "PlannedAutomaticRemittanceSchedule",
            "modeloLower_labelSingular": "PlannedAutomaticRemittanceSchedule",
            "modeloLower_labelPlurar": "PlannedAutomaticRemittanceSchedule",
            "codigos": {
                "create": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "PlannedAutomaticRemittanceScheduleSerializer_Create"
                },
                "list": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "PlannedAutomaticRemittanceScheduleSerializer_List"
                },
                "edit": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "PlannedAutomaticRemittanceScheduleSerializer_Update"
                },
                "destroy": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "PlannedAutomaticRemittanceScheduleSerializer_Destroy"
                },
                "view": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "PlannedAutomaticRemittanceScheduleSerializer_Retrieve"
                }
            }
        },
        "PlannedAutomaticAlarmRemittance": {
            "campos": [
                {
                    "name": "id",
                    "type": "BigAutoField",
                    "related_model": "",
                    "descripcion_entrada": "ID",
                    "descripcion_salida": ""
                },
                {
                    "name": "planned_remittance",
                    "type": "ForeignKey",
                    "related_model": "PlannedRemittance",
                    "descripcion_entrada": "planned remittance",
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
                    "name": "description",
                    "type": "TextField",
                    "related_model": "",
                    "descripcion_entrada": "description",
                    "descripcion_salida": ""
                },
                {
                    "name": "None",
                    "type": "Extra_ForeignKey",
                    "related_model": "PlannedAutomaticAlarmRemittanceFrequency",
                    "descripcion_entrada": "Relacion PlannedAutomaticAlarmRemittanceFrequency",
                    "descripcion_salida": ""
                },
                {
                    "name": "None",
                    "type": "Extra_ForeignKey",
                    "related_model": "PlannedAutomaticAlarmRemittanceSchedule",
                    "descripcion_entrada": "Relacion PlannedAutomaticAlarmRemittanceSchedule",
                    "descripcion_salida": ""
                }
            ],
            "modeloLower": "plannedautomaticalarmremittance",
            "modelo_labelSingular": "PlannedAutomaticAlarmRemittance",
            "modelo_labelPlurar": "PlannedAutomaticAlarmRemittance",
            "modeloLower_labelSingular": "PlannedAutomaticAlarmRemittance",
            "modeloLower_labelPlurar": "PlannedAutomaticAlarmRemittance",
            "codigos": {
                "create": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "PlannedAutomaticAlarmRemittanceSerializer_Create"
                },
                "list": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "PlannedAutomaticAlarmRemittanceSerializer_List"
                },
                "edit": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "PlannedAutomaticAlarmRemittanceSerializer_Update"
                },
                "destroy": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "PlannedAutomaticAlarmRemittanceSerializer_Destroy"
                },
                "view": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "PlannedAutomaticAlarmRemittanceSerializer_Retrieve"
                }
            }
        },
        "PlannedAutomaticAlarmRemittanceFrequency": {
            "campos": [
                {
                    "name": "id",
                    "type": "BigAutoField",
                    "related_model": "",
                    "descripcion_entrada": "ID",
                    "descripcion_salida": ""
                },
                {
                    "name": "frequency",
                    "type": "DurationField",
                    "related_model": "",
                    "descripcion_entrada": "frequency",
                    "descripcion_salida": ""
                },
                {
                    "name": "planned_automatic_alarm_remittance",
                    "type": "ForeignKey",
                    "related_model": "PlannedAutomaticAlarmRemittance",
                    "descripcion_entrada": "planned automatic alarm remittance",
                    "descripcion_salida": ""
                }
            ],
            "modeloLower": "plannedautomaticalarmremittancefrequency",
            "modelo_labelSingular": "PlannedAutomaticAlarmRemittanceFrequency",
            "modelo_labelPlurar": "PlannedAutomaticAlarmRemittanceFrequency",
            "modeloLower_labelSingular": "PlannedAutomaticAlarmRemittanceFrequency",
            "modeloLower_labelPlurar": "PlannedAutomaticAlarmRemittanceFrequency",
            "codigos": {
                "create": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "PlannedAutomaticAlarmRemittanceFrequencySerializer_Create"
                },
                "list": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "PlannedAutomaticAlarmRemittanceFrequencySerializer_List"
                },
                "edit": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "PlannedAutomaticAlarmRemittanceFrequencySerializer_Update"
                },
                "destroy": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "PlannedAutomaticAlarmRemittanceFrequencySerializer_Destroy"
                },
                "view": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "PlannedAutomaticAlarmRemittanceFrequencySerializer_Retrieve"
                }
            }
        },
        "PlannedAutomaticAlarmRemittanceSchedule": {
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
                    "name": "planned_automatic_alarm_remittance",
                    "type": "ForeignKey",
                    "related_model": "PlannedAutomaticAlarmRemittance",
                    "descripcion_entrada": "planned automatic alarm remittance",
                    "descripcion_salida": ""
                }
            ],
            "modeloLower": "plannedautomaticalarmremittanceschedule",
            "modelo_labelSingular": "PlannedAutomaticAlarmRemittanceSchedule",
            "modelo_labelPlurar": "PlannedAutomaticAlarmRemittanceSchedule",
            "modeloLower_labelSingular": "PlannedAutomaticAlarmRemittanceSchedule",
            "modeloLower_labelPlurar": "PlannedAutomaticAlarmRemittanceSchedule",
            "codigos": {
                "create": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "PlannedAutomaticAlarmRemittanceScheduleSerializer_Create"
                },
                "list": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "PlannedAutomaticAlarmRemittanceScheduleSerializer_List"
                },
                "edit": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "PlannedAutomaticAlarmRemittanceScheduleSerializer_Update"
                },
                "destroy": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "PlannedAutomaticAlarmRemittanceScheduleSerializer_Destroy"
                },
                "view": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "PlannedAutomaticAlarmRemittanceScheduleSerializer_Retrieve"
                }
            }
        },
        "CardTransaction": {
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
                    "name": "amount",
                    "type": "DecimalField",
                    "related_model": "",
                    "descripcion_entrada": "amount",
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
                    "name": "origin_user",
                    "type": "ForeignKey",
                    "related_model": "User",
                    "descripcion_entrada": "origin user",
                    "descripcion_salida": ""
                },
                {
                    "name": "origin_card",
                    "type": "ForeignKey",
                    "related_model": "Card",
                    "descripcion_entrada": "origin card",
                    "descripcion_salida": ""
                },
                {
                    "name": "origin_card_number",
                    "type": "CharField",
                    "related_model": "",
                    "descripcion_entrada": "origin card number",
                    "descripcion_salida": ""
                },
                {
                    "name": "origin_card_bank",
                    "type": "CharField",
                    "related_model": "",
                    "descripcion_entrada": "origin card bank",
                    "descripcion_salida": ""
                },
                {
                    "name": "origin_full_name",
                    "type": "CharField",
                    "related_model": "",
                    "descripcion_entrada": "origin full name",
                    "descripcion_salida": ""
                },
                {
                    "name": "origin_telephone_number",
                    "type": "CharField",
                    "related_model": "",
                    "descripcion_entrada": "origin telephone number",
                    "descripcion_salida": ""
                },
                {
                    "name": "origin_address",
                    "type": "CharField",
                    "related_model": "",
                    "descripcion_entrada": "origin address",
                    "descripcion_salida": ""
                },
                {
                    "name": "origin_postal_code",
                    "type": "CharField",
                    "related_model": "",
                    "descripcion_entrada": "origin postal code",
                    "descripcion_salida": ""
                },
                {
                    "name": "destination_user",
                    "type": "ForeignKey",
                    "related_model": "User",
                    "descripcion_entrada": "destination user",
                    "descripcion_salida": ""
                },
                {
                    "name": "destination_card",
                    "type": "ForeignKey",
                    "related_model": "Card",
                    "descripcion_entrada": "destination card",
                    "descripcion_salida": ""
                },
                {
                    "name": "destination_card_number",
                    "type": "CharField",
                    "related_model": "",
                    "descripcion_entrada": "destination card number",
                    "descripcion_salida": ""
                },
                {
                    "name": "destination_card_bank",
                    "type": "CharField",
                    "related_model": "",
                    "descripcion_entrada": "destination card bank",
                    "descripcion_salida": ""
                },
                {
                    "name": "destination_full_name",
                    "type": "CharField",
                    "related_model": "",
                    "descripcion_entrada": "destination full name",
                    "descripcion_salida": ""
                },
                {
                    "name": "destination_telephone_number",
                    "type": "CharField",
                    "related_model": "",
                    "descripcion_entrada": "destination telephone number",
                    "descripcion_salida": ""
                },
                {
                    "name": "destination_address",
                    "type": "CharField",
                    "related_model": "",
                    "descripcion_entrada": "destination address",
                    "descripcion_salida": ""
                },
                {
                    "name": "destination_postal_code",
                    "type": "CharField",
                    "related_model": "",
                    "descripcion_entrada": "destination postal code",
                    "descripcion_salida": ""
                },
                {
                    "name": "None",
                    "type": "Extra_ForeignKey",
                    "related_model": "MadeRemittance",
                    "descripcion_entrada": "Relacion MadeRemittance",
                    "descripcion_salida": ""
                },
                {
                    "name": "None",
                    "type": "Extra_ForeignKey",
                    "related_model": "PaymentMade",
                    "descripcion_entrada": "Relacion PaymentMade",
                    "descripcion_salida": ""
                },
                {
                    "name": "None",
                    "type": "Extra_ForeignKey",
                    "related_model": "RemittanceRefund",
                    "descripcion_entrada": "Relacion RemittanceRefund",
                    "descripcion_salida": ""
                }
            ],
            "modeloLower": "cardtransaction",
            "modelo_labelSingular": "CardTransaction",
            "modelo_labelPlurar": "CardTransaction",
            "modeloLower_labelSingular": "CardTransaction",
            "modeloLower_labelPlurar": "CardTransaction",
            "codigos": {
                "create": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "CardTransactionSerializer_Create"
                },
                "list": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "CardTransactionSerializer_List"
                },
                "edit": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "CardTransactionSerializer_Update"
                },
                "destroy": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "CardTransactionSerializer_Destroy"
                },
                "view": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "CardTransactionSerializer_Retrieve"
                }
            }
        },
        "MadeRemittance": {
            "campos": [
                {
                    "name": "id",
                    "type": "BigAutoField",
                    "related_model": "",
                    "descripcion_entrada": "ID",
                    "descripcion_salida": ""
                },
                {
                    "name": "remittance_id",
                    "type": "UUIDField",
                    "related_model": "",
                    "descripcion_entrada": "remittance id",
                    "descripcion_salida": ""
                },
                {
                    "name": "planned_remittance",
                    "type": "ForeignKey",
                    "related_model": "PlannedRemittance",
                    "descripcion_entrada": "planned remittance",
                    "descripcion_salida": ""
                },
                {
                    "name": "card_transaction",
                    "type": "ForeignKey",
                    "related_model": "CardTransaction",
                    "descripcion_entrada": "card transaction",
                    "descripcion_salida": ""
                },
                {
                    "name": "reseller_id",
                    "type": "ForeignKey",
                    "related_model": "User",
                    "descripcion_entrada": "reseller id",
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
                },
                {
                    "name": "None",
                    "type": "Extra_ForeignKey",
                    "related_model": "PaymentMade",
                    "descripcion_entrada": "Relacion PaymentMade",
                    "descripcion_salida": ""
                },
                {
                    "name": "None",
                    "type": "Extra_ForeignKey",
                    "related_model": "RemittanceState",
                    "descripcion_entrada": "Relacion RemittanceState",
                    "descripcion_salida": ""
                },
                {
                    "name": "None",
                    "type": "Extra_ForeignKey",
                    "related_model": "RemittanceRefund",
                    "descripcion_entrada": "Relacion RemittanceRefund",
                    "descripcion_salida": ""
                }
            ],
            "modeloLower": "maderemittance",
            "modelo_labelSingular": "MadeRemittance",
            "modelo_labelPlurar": "MadeRemittance",
            "modeloLower_labelSingular": "MadeRemittance",
            "modeloLower_labelPlurar": "MadeRemittance",
            "codigos": {
                "create": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "MadeRemittanceSerializer_Create"
                },
                "list": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "MadeRemittanceSerializer_List"
                },
                "edit": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "MadeRemittanceSerializer_Update"
                },
                "destroy": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "MadeRemittanceSerializer_Destroy"
                },
                "view": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "MadeRemittanceSerializer_Retrieve"
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
                    "name": "card_transaction",
                    "type": "ForeignKey",
                    "related_model": "CardTransaction",
                    "descripcion_entrada": "card transaction",
                    "descripcion_salida": ""
                },
                {
                    "name": "made_remittance",
                    "type": "ForeignKey",
                    "related_model": "MadeRemittance",
                    "descripcion_entrada": "made remittance",
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
                    "name": "reseller_id",
                    "type": "ForeignKey",
                    "related_model": "User",
                    "descripcion_entrada": "reseller id",
                    "descripcion_salida": ""
                },
                {
                    "name": "None",
                    "type": "Extra_ForeignKey",
                    "related_model": "RemittanceState",
                    "descripcion_entrada": "Relacion RemittanceState",
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
        },
        "RemittanceState": {
            "campos": [
                {
                    "name": "id",
                    "type": "BigAutoField",
                    "related_model": "",
                    "descripcion_entrada": "ID",
                    "descripcion_salida": ""
                },
                {
                    "name": "made_remittance",
                    "type": "ForeignKey",
                    "related_model": "MadeRemittance",
                    "descripcion_entrada": "made remittance",
                    "descripcion_salida": ""
                },
                {
                    "name": "payment_made",
                    "type": "ForeignKey",
                    "related_model": "PaymentMade",
                    "descripcion_entrada": "payment made",
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
                    "name": "date",
                    "type": "DateTimeField",
                    "related_model": "",
                    "descripcion_entrada": "date",
                    "descripcion_salida": ""
                },
                {
                    "name": "shipping_date",
                    "type": "DateTimeField",
                    "related_model": "",
                    "descripcion_entrada": "shipping date",
                    "descripcion_salida": ""
                },
                {
                    "name": "estimated_delivery_date",
                    "type": "DateTimeField",
                    "related_model": "",
                    "descripcion_entrada": "estimated delivery date",
                    "descripcion_salida": ""
                },
                {
                    "name": "current_location_latitude",
                    "type": "DecimalField",
                    "related_model": "",
                    "descripcion_entrada": "current location latitude",
                    "descripcion_salida": ""
                },
                {
                    "name": "current_location_longitude",
                    "type": "DecimalField",
                    "related_model": "",
                    "descripcion_entrada": "current location longitude",
                    "descripcion_salida": ""
                },
                {
                    "name": "carrier_information",
                    "type": "TextField",
                    "related_model": "",
                    "descripcion_entrada": "carrier information",
                    "descripcion_salida": ""
                }
            ],
            "modeloLower": "remittancestate",
            "modelo_labelSingular": "RemittanceState",
            "modelo_labelPlurar": "RemittanceState",
            "modeloLower_labelSingular": "RemittanceState",
            "modeloLower_labelPlurar": "RemittanceState",
            "codigos": {
                "create": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "RemittanceStateSerializer_Create"
                },
                "list": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "RemittanceStateSerializer_List"
                },
                "edit": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "RemittanceStateSerializer_Update"
                },
                "destroy": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "RemittanceStateSerializer_Destroy"
                },
                "view": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "RemittanceStateSerializer_Retrieve"
                }
            }
        },
        "ResellerApplication": {
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
                    "type": "DateTimeField",
                    "related_model": "",
                    "descripcion_entrada": "date",
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
                    "name": "user",
                    "type": "ForeignKey",
                    "related_model": "User",
                    "descripcion_entrada": "user",
                    "descripcion_salida": ""
                }
            ],
            "modeloLower": "resellerapplication",
            "modelo_labelSingular": "ResellerApplication",
            "modelo_labelPlurar": "ResellerApplication",
            "modeloLower_labelSingular": "ResellerApplication",
            "modeloLower_labelPlurar": "ResellerApplication",
            "codigos": {
                "create": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "ResellerApplicationSerializer_Create"
                },
                "list": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "ResellerApplicationSerializer_List"
                },
                "edit": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "ResellerApplicationSerializer_Update"
                },
                "destroy": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "ResellerApplicationSerializer_Destroy"
                },
                "view": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "ResellerApplicationSerializer_Retrieve"
                }
            }
        },
        "RemittanceRefund": {
            "campos": [
                {
                    "name": "id",
                    "type": "BigAutoField",
                    "related_model": "",
                    "descripcion_entrada": "ID",
                    "descripcion_salida": ""
                },
                {
                    "name": "admin",
                    "type": "ForeignKey",
                    "related_model": "User",
                    "descripcion_entrada": "admin",
                    "descripcion_salida": ""
                },
                {
                    "name": "made_remittance",
                    "type": "ForeignKey",
                    "related_model": "MadeRemittance",
                    "descripcion_entrada": "made remittance",
                    "descripcion_salida": ""
                },
                {
                    "name": "refund_card_transaction",
                    "type": "ForeignKey",
                    "related_model": "CardTransaction",
                    "descripcion_entrada": "refund card transaction",
                    "descripcion_salida": ""
                }
            ],
            "modeloLower": "remittancerefund",
            "modelo_labelSingular": "RemittanceRefund",
            "modelo_labelPlurar": "RemittanceRefund",
            "modeloLower_labelSingular": "RemittanceRefund",
            "modeloLower_labelPlurar": "RemittanceRefund",
            "codigos": {
                "create": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "RemittanceRefundSerializer_Create"
                },
                "list": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "RemittanceRefundSerializer_List"
                },
                "edit": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "RemittanceRefundSerializer_Update"
                },
                "destroy": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "RemittanceRefundSerializer_Destroy"
                },
                "view": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "RemittanceRefundSerializer_Retrieve"
                }
            }
        },
        "ExchangeRate": {
            "campos": [
                {
                    "name": "id",
                    "type": "BigAutoField",
                    "related_model": "",
                    "descripcion_entrada": "ID",
                    "descripcion_salida": ""
                },
                {
                    "name": "amount_sent",
                    "type": "IntegerField",
                    "related_model": "",
                    "descripcion_entrada": "amount sent",
                    "descripcion_salida": ""
                },
                {
                    "name": "sender_currency",
                    "type": "CharField",
                    "related_model": "",
                    "descripcion_entrada": "sender currency",
                    "descripcion_salida": ""
                },
                {
                    "name": "target_currency",
                    "type": "CharField",
                    "related_model": "",
                    "descripcion_entrada": "target currency",
                    "descripcion_salida": ""
                },
                {
                    "name": "exchange_rate",
                    "type": "FloatField",
                    "related_model": "",
                    "descripcion_entrada": "exchange rate",
                    "descripcion_salida": ""
                }
            ],
            "modeloLower": "exchangerate",
            "modelo_labelSingular": "ExchangeRate",
            "modelo_labelPlurar": "ExchangeRate",
            "modeloLower_labelSingular": "ExchangeRate",
            "modeloLower_labelPlurar": "ExchangeRate",
            "codigos": {
                "create": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "ExchangeRateSerializer_Create"
                },
                "list": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "ExchangeRateSerializer_List"
                },
                "edit": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "ExchangeRateSerializer_Update"
                },
                "destroy": {
                    "save": "",
                    "permisos_descripcion": "{- IsAuthenticated -}\n{- EsSuperUsuario -}",
                    "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
                    "serializer": "ExchangeRateSerializer_Destroy"
                },
                "view": {
                    "save": "",
                    "permisos_descripcion": "",
                    "permisos": "",
                    "serializer": "ExchangeRateSerializer_Retrieve"
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
        "DurationField",
        "DecimalField",
        "UUIDField"
    ]
}

