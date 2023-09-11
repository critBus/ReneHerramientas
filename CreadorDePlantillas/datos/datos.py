key_valores={
    "models": {
        "RolNegocio": {
            "campos": [
                {
                    "name": "id",
                    "type": "BigAutoField",
                    "related_model": "",
                    "descripcion_entrada":"",
                    "descripcion_salida":"",
                },
                {
                    "name": "rol",
                    "type": "ForeignKey",
                    "related_model": "Group",
                    "descripcion_entrada":"rol del usuario en el negocio",
                    "descripcion_salida":"",
                },
                {
                    "name": "user",
                    "type": "ForeignKey",
                    "related_model": "User",
                    "descripcion_entrada":"usuario que al pertenece esta entidad",
                    "descripcion_salida":"",
                }
            ],
            "modeloLower": "rolnegocio",
            "modelo_labelSingular": "RolNegocio",
            "modelo_labelPlurar": "RolNegocio",
            "modeloLower_labelSingular": "RolNegocio",
            "modeloLower_labelPlurar": "RolNegocio",
            "codigos":{
                "create":{
                    "save":"",
                    "permisos_descripcion":"{- IsAuthenticated -}\n{- SoloPuedeModificarseElMismo_OEsSuperusuario -}",
                    "permisos":"permission_classes = (IsAuthenticated, SoloPuedeModificarseElMismo_OEsSuperusuario,)"
                    
                    },
                "list":{
                        "save":"",
                    "permisos_descripcion":"",
                    "permisos":""
                    },
                "edit":{
                        "save":"",
                    "permisos_descripcion":"",
                    "permisos":""
                    },
                "destroy":{
                        "save":"",
                    "permisos_descripcion":"{- IsAuthenticated -}\n{- SoloPuedeModificarseElMismo_OEsSuperusuario -}",
                    "permisos":"permission_classes = (IsAuthenticated, SoloPuedeModificarseElMismo_OEsSuperusuario,)  #"
                    },
                "view":{
                    "save":"",
                    "permisos_descripcion":"",
                    "permisos":""
                    
                    }
            }
        },
        "PalabraClave": {
            "campos": [
                {
                    "name": "id",
                    "type": "BigAutoField",
                    "related_model": "",
                    "descripcion_entrada":"",
                    "descripcion_salida":"",
                },
                {
                    "name": "nombre",
                    "type": "CharField",
                    "related_model": "",
                    "descripcion_entrada":"palabra clave",
                    "descripcion_salida":"",
                }
            ],
            "modeloLower": "palabraclave",
            "modelo_labelSingular": "PalabraClave",
            "modelo_labelPlurar": "PalabraClave",
            "modeloLower_labelSingular": "PalabraClave",
            "modeloLower_labelPlurar": "PalabraClave",
            "codigos":{
                "create":{
                    "save":"",
                    "permisos_descripcion":"{- IsAuthenticated -}",
                    "permisos":"permission_classes = (IsAuthenticated,)"
                    
                    },
                "list":{
                        "save":"",
                    "permisos_descripcion":"",
                    "permisos":""
                    },
                "edit":{
                        "save":"",
                    "permisos_descripcion":"{- IsAuthenticated -}"
                                            +"{- EsSuperUsuario -}",
                    "permisos":"permission_classes = (IsAuthenticated,EsSuperUsuario,)"
                    },
                "destroy":{
                        "save":"",
                    "permisos_descripcion":"{- IsAuthenticated -}"
                                            +"{- EsSuperUsuario -}",
                    "permisos":"permission_classes = (IsAuthenticated, EsSuperUsuario,)"
                    },
                "view":{
                    "save":"",
                    "permisos_descripcion":"",
                    "permisos":""
                    
                    }
            }
        },
        "TipoDeGestion": {
            "campos": [
                {
                    "name": "id",
                    "type": "BigAutoField",
                    "related_model": "",
                    "descripcion_entrada":"",
                    "descripcion_salida":"",
                },
                {
                    "name": "nombre",
                    "type": "CharField",
                    "related_model": "",
                    "descripcion_entrada":"tipo de gestion",
                    "descripcion_salida":"",
                }
            ],
            "modeloLower": "tipodegestion",
            "modelo_labelSingular": "TipoDeGestion",
            "modelo_labelPlurar": "TipoDeGestion",
            "modeloLower_labelSingular": "TipoDeGestion",
            "modeloLower_labelPlurar": "TipoDeGestion",
            "codigos":{
                "create":{
                    "save":"",
                    "permisos_descripcion":"",
                    "permisos":""
                    
                    },
                "list":{
                        "save":"",
                    "permisos_descripcion":"",
                    "permisos":""
                    },
                "edit":{
                        "save":"",
                    "permisos_descripcion":"",
                    "permisos":""
                    },
                "destroy":{
                        "save":"",
                    "permisos_descripcion":"",
                    "permisos":""
                    },
                "view":{
                    "save":"",
                    "permisos_descripcion":"",
                    "permisos":""
                    
                    }
            }
        },
        "CategoriaDeNegocio": {
            "campos": [
                {
                    "name": "id",
                    "type": "BigAutoField",
                    "related_model": "",
                    "descripcion_entrada":"",
                    "descripcion_salida":"",
                },
                {
                    "name": "nombre",
                    "type": "CharField",
                    "related_model": "",
                    "descripcion_entrada":"categoria del negocio",
                    "descripcion_salida":"",
                }
            ],
            "modeloLower": "categoriadenegocio",
            "modelo_labelSingular": "CategoriaDeNegocio",
            "modelo_labelPlurar": "CategoriaDeNegocio",
            "modeloLower_labelSingular": "CategoriaDeNegocio",
            "modeloLower_labelPlurar": "CategoriaDeNegocio",
            "codigos":{
                "create":{
                    "save":"",
                    "permisos_descripcion":"",
                    "permisos":""
                    
                    },
                "list":{
                        "save":"",
                    "permisos_descripcion":"",
                    "permisos":""
                    },
                "edit":{
                        "save":"",
                    "permisos_descripcion":"",
                    "permisos":""
                    },
                "destroy":{
                        "save":"",
                    "permisos_descripcion":"",
                    "permisos":""
                    },
                "view":{
                    "save":"",
                    "permisos_descripcion":"",
                    "permisos":""
                    
                    }
            }
        },
        "Negocio": {
            "campos": [
                {
                    "name": "id",
                    "type": "BigAutoField",
                    "related_model": "",
                    "descripcion_entrada":"",
                    "descripcion_salida":"",
                },
                {
                    "name": "nombre",
                    "type": "CharField",
                    "related_model": "",
                    "descripcion_entrada":"nombre",
                    "descripcion_salida":"",
                },
                {
                    "name": "logo",
                    "type": "ImageField",
                    "related_model": "",
                    "descripcion_entrada":"imagen que representa al negocio",
                    "descripcion_salida":"",
                },
                {
                    "name": "slogan",
                    "type": "CharField",
                    "related_model": "",
                    "descripcion_entrada":"slogan que representa al negocio",
                    "descripcion_salida":"",
                },
                {
                    "name": "direccion",
                    "type": "CharField",
                    "related_model": "",
                    "descripcion_entrada":"dirección",
                    "descripcion_salida":"",
                },
                {
                    "name": "descripcion_entrada",
                    "type": "TextField",
                    "related_model": "",
                    "descripcion_entrada":"descripción",
                    "descripcion_salida":"",
                },
                {
                    "name": "TipoDeGestion",
                    "type": "ForeignKey",
                    "related_model": "TipoDeGestion",
                    "descripcion_entrada":"id del tipo de gestion",
                    "descripcion_salida":"",
                },
                {
                    "name": "responsabilidades",
                    "type": "ManyToManyField",
                    "related_model": "RolNegocio",
                    "descripcion_entrada":" [#,#,#,..] lista de id de los roles de negocio existentes en este negocio",
                    "descripcion_salida":"",
                },
                {
                    "name": "PalabrasClave",
                    "type": "ManyToManyField",
                    "related_model": "PalabraClave",
                    "descripcion_entrada":" [#,#,#,..] lista de id de las palabras claves relacionadas con este negocio",
                    "descripcion_salida":"",
                },
                {
                    "name": "CategoriasDeNegocio",
                    "type": "ManyToManyField",
                    "related_model": "CategoriaDeNegocio",
                    "descripcion_entrada":" [#,#,#,..] lista de id de las categorias del negocio relacionadas con este negocio",
                    "descripcion_salida":"",
                }
            ],
            "modeloLower": "negocio",
            "modelo_labelSingular": "Negocio",
            "modelo_labelPlurar": "Negocio",
            "modeloLower_labelSingular": "Negocio",
            "modeloLower_labelPlurar": "Negocio",
            "codigos":{
                "create":{
                    "save":"""
    def post(self, request, *args, **kwargs):
        try:
            data = getData(request)
            #print(data)
        except:
            print(traceback.format_exc())
            return JsonResponse({'status': 'error', 'message': 'Error de en servidor'}, status=500)

        # orginal
        response = self.create(request, *args, **kwargs)
        # fin original
        try:

            if response.status_code >= 200 and response.status_code <= 299:
                datos = response.data
                datos["nueva_clave"] = "nuevo_valor"
            return response
        except:
            print(traceback.format_exc())
            return JsonResponse({'status': 'error', 'message': 'Error de en servidor'}, status=500)

                    """,
                    "permisos_descripcion":"{- IsAuthenticated -}"
                                            +"",
                    "permisos":"permission_classes = (IsAuthenticated,)"
                    },
                "list":{
                        "save":"",
                    "permisos_descripcion":"",
                    "permisos":""
                    },
                "edit":{
                        "save":"",
                    "permisos_descripcion":"{- IsAuthenticated -}"
                                            +"{- getPermisoEnEndpointEntidad_Can_GET editado -}",
                    "permisos":"permission_classes = (IsAuthenticated,getPermisoEnEndpointEntidad_Can_GET('change'),)"
                    },
                "destroy":{
                        "save":"",
                    "permisos_descripcion":"{- IsAuthenticated -}"
                                            +"{- getPermisoEnEndpointEntidad_Can_GET delete -}",
                    "permisos":"permission_classes = (IsAuthenticated,getPermisoEnEndpointEntidad_Can_GET('delete'),)"
                    },
                "view":{
                    "save":"",
                    "permisos_descripcion":"",
                    "permisos":""
                    
                    }
            }
        },
        "TipoDeContacto": {
            "campos": [
                {
                    "name": "id",
                    "type": "BigAutoField",
                    "related_model": "",
                    "descripcion_entrada":"",
                    "descripcion_salida":"",
                },
                {
                    "name": "nombre",
                    "type": "CharField",
                    "related_model": "",
                    "descripcion_entrada":"tipo de contacto",
                    "descripcion_salida":"",
                }
            ],
            "modeloLower": "tipodecontacto",
            "modelo_labelSingular": "TipoDeContacto",
            "modelo_labelPlurar": "TipoDeContacto",
            "modeloLower_labelSingular": "TipoDeContacto",
            "modeloLower_labelPlurar": "TipoDeContacto",
            "codigos":{
                "create":{
                    "save":"",
                    "permisos_descripcion":"",
                    "permisos":""
                    
                    },
                "list":{
                        "save":"",
                    "permisos_descripcion":"",
                    "permisos":""
                    },
                "edit":{
                        "save":"",
                    "permisos_descripcion":"",
                    "permisos":""
                    },
                "destroy":{
                        "save":"",
                    "permisos_descripcion":"",
                    "permisos":""
                    },
                "view":{
                    "save":"",
                    "permisos_descripcion":"",
                    "permisos":""
                    
                    }
            }
        },
        "Contacto": {
            "campos": [
                {
                    "name": "id",
                    "type": "BigAutoField",
                    "related_model": "",
                    "descripcion_entrada":"",
                    "descripcion_salida":"",
                },
                {
                    "name": "nombre",
                    "type": "CharField",
                    "related_model": "",
                    "descripcion_entrada":"contacto",
                    "descripcion_salida":"",
                },
                {
                    "name": "TipoDeContacto",
                    "type": "ForeignKey",
                    "related_model": "TipoDeContacto",
                    "descripcion_entrada":"id de tipo de contacto",
                    "descripcion_salida":"",
                },
                {
                    "name": "Negocio",
                    "type": "ForeignKey",
                    "related_model": "Negocio",
                    "descripcion_entrada":"id del negocio",
                    "descripcion_salida":"",
                }
            ],
            "modeloLower": "contacto",
            "modelo_labelSingular": "Contacto",
            "modelo_labelPlurar": "Contacto",
            "modeloLower_labelSingular": "Contacto",
            "modeloLower_labelPlurar": "Contacto",
            "codigos":{
                "create":{
                    "save":"",
                    "permisos_descripcion":"",
                    "permisos":""
                    
                    },
                "list":{
                        "save":"",
                    "permisos_descripcion":"",
                    "permisos":""
                    },
                "edit":{
                        "save":"",
                    "permisos_descripcion":"",
                    "permisos":""
                    },
                "destroy":{
                        "save":"",
                    "permisos_descripcion":"",
                    "permisos":""
                    },
                "view":{
                    "save":"",
                    "permisos_descripcion":"",
                    "permisos":""
                    
                    }
            }
        },
        "CategoriaDeServicio": {
            "campos": [
                {
                    "name": "id",
                    "type": "BigAutoField",
                    "related_model": "",
                    "descripcion_entrada":"",
                    "descripcion_salida":"",
                },
                {
                    "name": "nombre",
                    "type": "CharField",
                    "related_model": "",
                    "descripcion_entrada":"categoria de servicio",
                    "descripcion_salida":"",
                },
                {
                    "name": "Negocio",
                    "type": "ForeignKey",
                    "related_model": "Negocio",
                    "descripcion_entrada":"id del negocio",
                    "descripcion_salida":"",
                }
            ],
            "modeloLower": "categoriadeservicio",
            "modelo_labelSingular": "CategoriaDeServicio",
            "modelo_labelPlurar": "CategoriaDeServicio",
            "modeloLower_labelSingular": "CategoriaDeServicio",
            "modeloLower_labelPlurar": "CategoriaDeServicio",
            "codigos":{
                "create":{
                    "save":"",
                    "permisos_descripcion":"Este método requiere que el usuario esté autenticado para poder ser utilizado. La autenticación se realiza mediante el uso de una JWT (JSON Web Token) que se incluye en la cabecera de la solicitud HTTP. La JWT incluye información sobre el usuario autenticado, como su identidad y los permisos que se le han otorgado."
                                            +"",
                    "permisos":"permission_classes = (IsAuthenticated,)"
                    },
                "list":{
                        "save":"",
                    "permisos_descripcion":"",
                    "permisos":""
                    },
                "edit":{
                        "save":"",
                    "permisos_descripcion":"Este método requiere que el usuario esté autenticado para poder ser utilizado. La autenticación se realiza mediante el uso de una JWT (JSON Web Token) que se incluye en la cabecera de la solicitud HTTP. La JWT incluye información sobre el usuario autenticado, como su identidad y los permisos que se le han otorgado."
                                            +"Solo puede ser editado por un usuario que tenga un Rol de Negocio asociado a al Negocio que le corresponde con este permiso ",
                    "permisos":"permission_classes = (IsAuthenticated,getPermisoEnEndpointEntidad_Can_GET('change'),)"
                    },
                "destroy":{
                        "save":"",
                    "permisos_descripcion":"Este método requiere que el usuario esté autenticado para poder ser utilizado. La autenticación se realiza mediante el uso de una JWT (JSON Web Token) que se incluye en la cabecera de la solicitud HTTP. La JWT incluye información sobre el usuario autenticado, como su identidad y los permisos que se le han otorgado."
                                            +"Solo puede ser eliminado por un usuario que tenga un Rol de Negocio asociado a al Negocio que le corresponde con este permiso ",
                    "permisos":"permission_classes = (IsAuthenticated,getPermisoEnEndpointEntidad_Can_GET('delete'),)"
                    },
                "view":{
                    "save":"",
                    "permisos_descripcion":"",
                    "permisos":""
                    
                    }
            }
        },
        "CategoriaDeProducto": {
            "campos": [
                {
                    "name": "id",
                    "type": "BigAutoField",
                    "related_model": "",
                    "descripcion_entrada":"",
                    "descripcion_salida":"",
                },
                {
                    "name": "nombre",
                    "type": "CharField",
                    "related_model": "",
                    "descripcion_entrada":"categoria del producto",
                    "descripcion_salida":"",
                },
                {
                    "name": "Negocio",
                    "type": "ForeignKey",
                    "related_model": "Negocio",
                    "descripcion_entrada":"id del negocio",
                    "descripcion_salida":"",
                }
            ],
            "modeloLower": "categoriadeproducto",
            "modelo_labelSingular": "CategoriaDeProducto",
            "modelo_labelPlurar": "CategoriaDeProducto",
            "modeloLower_labelSingular": "CategoriaDeProducto",
            "modeloLower_labelPlurar": "CategoriaDeProducto",
            "codigos":{
                "create":{
                    "save":"",
                    "permisos_descripcion":"Este método requiere que el usuario esté autenticado para poder ser utilizado. La autenticación se realiza mediante el uso de una JWT (JSON Web Token) que se incluye en la cabecera de la solicitud HTTP. La JWT incluye información sobre el usuario autenticado, como su identidad y los permisos que se le han otorgado."
                                            +"",
                    "permisos":"permission_classes = (IsAuthenticated,)"
                    },
                "list":{
                        "save":"",
                    "permisos_descripcion":"",
                    "permisos":""
                    },
                "edit":{
                        "save":"",
                    "permisos_descripcion":"Este método requiere que el usuario esté autenticado para poder ser utilizado. La autenticación se realiza mediante el uso de una JWT (JSON Web Token) que se incluye en la cabecera de la solicitud HTTP. La JWT incluye información sobre el usuario autenticado, como su identidad y los permisos que se le han otorgado."
                                            +"Solo puede ser editado por un usuario que tenga un Rol de Negocio asociado a al Negocio que le corresponde con este permiso ",
                    "permisos":"permission_classes = (IsAuthenticated,getPermisoEnEndpointEntidad_Can_GET('change'),)"
                    },
                "destroy":{
                        "save":"",
                    "permisos_descripcion":"Este método requiere que el usuario esté autenticado para poder ser utilizado. La autenticación se realiza mediante el uso de una JWT (JSON Web Token) que se incluye en la cabecera de la solicitud HTTP. La JWT incluye información sobre el usuario autenticado, como su identidad y los permisos que se le han otorgado."
                                            +"Solo puede ser eliminado por un usuario que tenga un Rol de Negocio asociado a al Negocio que le corresponde con este permiso ",
                    "permisos":"permission_classes = (IsAuthenticated,getPermisoEnEndpointEntidad_Can_GET('delete'),)"
                    },
                "view":{
                    "save":"",
                    "permisos_descripcion":"",
                    "permisos":""
                    
                    }
            }
        },
        "Producto": {
            "campos": [
                {
                    "name": "id",
                    "type": "BigAutoField",
                    "related_model": "",
                    "descripcion_entrada":"",
                    "descripcion_salida":"",
                },
                {
                    "name": "Nombre",
                    "type": "CharField",
                    "related_model": "",
                    "descripcion_entrada":"nombre del producto",
                    "descripcion_salida":"",
                },
                {
                    "name": "Disponibilidad",
                    "type": "BooleanField",
                    "related_model": "",
                    "descripcion_entrada":"True o False, representando la disponibilidad",
                    "descripcion_salida":"",
                },
                {
                    "name": "Precio_actual",
                    "type": "FloatField",
                    "related_model": "",
                    "descripcion_entrada":"precio actual",
                    "descripcion_salida":"",
                },
                {
                    "name": "Precio_anterior",
                    "type": "FloatField",
                    "related_model": "",
                    "descripcion_entrada":"precio anterior",
                    "descripcion_salida":"",
                },
                {
                    "name": "descripcion_entrada",
                    "type": "TextField",
                    "related_model": "",
                    "descripcion_entrada":"descripción",
                    "descripcion_salida":"",
                },
                {
                    "name": "Categoria",
                    "type": "ForeignKey",
                    "related_model": "CategoriaDeProducto",
                    "descripcion_entrada":"id de la categoria del producto",
                    "descripcion_salida":"",
                }
            ],
            "modeloLower": "producto",
            "modelo_labelSingular": "Producto",
            "modelo_labelPlurar": "Producto",
            "modeloLower_labelSingular": "Producto",
            "modeloLower_labelPlurar": "Producto",
            "codigos":{
                "create":{
                    "save":"",
                    "permisos_descripcion":"Este método requiere que el usuario esté autenticado para poder ser utilizado. La autenticación se realiza mediante el uso de una JWT (JSON Web Token) que se incluye en la cabecera de la solicitud HTTP. La JWT incluye información sobre el usuario autenticado, como su identidad y los permisos que se le han otorgado."
                                            +"",
                    "permisos":"permission_classes = (IsAuthenticated,)"
                    },
                "list":{
                        "save":"",
                    "permisos_descripcion":"",
                    "permisos":""
                    },
                "edit":{
                        "save":"",
                    "permisos_descripcion":"Este método requiere que el usuario esté autenticado para poder ser utilizado. La autenticación se realiza mediante el uso de una JWT (JSON Web Token) que se incluye en la cabecera de la solicitud HTTP. La JWT incluye información sobre el usuario autenticado, como su identidad y los permisos que se le han otorgado."
                                            +"Solo puede ser editado por un usuario que tenga un Rol de Negocio asociado a al Negocio que le corresponde con este permiso ",
                    "permisos":"permission_classes = (IsAuthenticated,getPermisoEnEndpointEntidad_Can_GET('change'),)"
                    },
                "destroy":{
                        "save":"",
                    "permisos_descripcion":"Este método requiere que el usuario esté autenticado para poder ser utilizado. La autenticación se realiza mediante el uso de una JWT (JSON Web Token) que se incluye en la cabecera de la solicitud HTTP. La JWT incluye información sobre el usuario autenticado, como su identidad y los permisos que se le han otorgado."
                                            +"Solo puede ser eliminado por un usuario que tenga un Rol de Negocio asociado a al Negocio que le corresponde con este permiso ",
                    "permisos":"permission_classes = (IsAuthenticated,getPermisoEnEndpointEntidad_Can_GET('delete'),)"
                    },
                "view":{
                    "save":"",
                    "permisos_descripcion":"",
                    "permisos":""
                    
                    }
            }
        },
        "TipoDeImagen": {
            "campos": [
                {
                    "name": "id",
                    "type": "BigAutoField",
                    "related_model": "",
                    "descripcion_entrada":"",
                    "descripcion_salida":"",
                },
                {
                    "name": "nombre",
                    "type": "CharField",
                    "related_model": "",
                    "descripcion_entrada":"tipo de imagen",
                    "descripcion_salida":"",
                }
            ],
            "modeloLower": "tipodeimagen",
            "modelo_labelSingular": "TipoDeImagen",
            "modelo_labelPlurar": "TipoDeImagen",
            "modeloLower_labelSingular": "TipoDeImagen",
            "modeloLower_labelPlurar": "TipoDeImagen",
            "codigos":{
                "create":{
                    "save":"",
                    "permisos_descripcion":"",
                    "permisos":""
                    
                    },
                "list":{
                        "save":"",
                    "permisos_descripcion":"",
                    "permisos":""
                    },
                "edit":{
                        "save":"",
                    "permisos_descripcion":"",
                    "permisos":""
                    },
                "destroy":{
                        "save":"",
                    "permisos_descripcion":"",
                    "permisos":""
                    },
                "view":{
                    "save":"",
                    "permisos_descripcion":"",
                    "permisos":""
                    
                    }
            }
        },
        "Servicio": {
            "campos": [
                {
                    "name": "id",
                    "type": "BigAutoField",
                    "related_model": "",
                    "descripcion_entrada":"",
                    "descripcion_salida":"",
                },
                {
                    "name": "Nombre",
                    "type": "CharField",
                    "related_model": "",
                    "descripcion_entrada":"nombre del servicio",
                    "descripcion_salida":"",
                },
                {
                    "name": "Disponibilidad",
                    "type": "BooleanField",
                    "related_model": "",
                    "descripcion_entrada":"True o False representando la disponibilidad",
                    "descripcion_salida":"",
                },
                {
                    "name": "Precio_actual",
                    "type": "FloatField",
                    "related_model": "",
                    "descripcion_entrada":"precio actual",
                    "descripcion_salida":"",
                },
                {
                    "name": "Precio_anterior",
                    "type": "FloatField",
                    "related_model": "",
                    "descripcion_entrada":"precio anterior",
                    "descripcion_salida":"",
                },
                {
                    "name": "descripcion_entrada",
                    "type": "TextField",
                    "related_model": "",
                    "descripcion_entrada":"descripción",
                    "descripcion_salida":"",
                },
                {
                    "name": "Categoria",
                    "type": "ForeignKey",
                    "related_model": "CategoriaDeServicio",
                    "descripcion_entrada":"id del la categoria del servicio",
                    "descripcion_salida":"",
                }
            ],
            "modeloLower": "servicio",
            "modelo_labelSingular": "Servicio",
            "modelo_labelPlurar": "Servicio",
            "modeloLower_labelSingular": "Servicio",
            "modeloLower_labelPlurar": "Servicio",
            "codigos":{
                "create":{
                    "save":"",
                    "permisos_descripcion":"Este método requiere que el usuario esté autenticado para poder ser utilizado. La autenticación se realiza mediante el uso de una JWT (JSON Web Token) que se incluye en la cabecera de la solicitud HTTP. La JWT incluye información sobre el usuario autenticado, como su identidad y los permisos que se le han otorgado."
                                            +"",
                    "permisos":"permission_classes = (IsAuthenticated,)"
                    },
                "list":{
                        "save":"",
                    "permisos_descripcion":"",
                    "permisos":""
                    },
                "edit":{
                        "save":"",
                    "permisos_descripcion":"Este método requiere que el usuario esté autenticado para poder ser utilizado. La autenticación se realiza mediante el uso de una JWT (JSON Web Token) que se incluye en la cabecera de la solicitud HTTP. La JWT incluye información sobre el usuario autenticado, como su identidad y los permisos que se le han otorgado."
                                            +"Solo puede ser editado por un usuario que tenga un Rol de Negocio asociado a al Negocio que le corresponde con este permiso ",
                    "permisos":"permission_classes = (IsAuthenticated,getPermisoEnEndpointEntidad_Can_GET('change'),)"
                    },
                "destroy":{
                        "save":"",
                    "permisos_descripcion":"Este método requiere que el usuario esté autenticado para poder ser utilizado. La autenticación se realiza mediante el uso de una JWT (JSON Web Token) que se incluye en la cabecera de la solicitud HTTP. La JWT incluye información sobre el usuario autenticado, como su identidad y los permisos que se le han otorgado."
                                            +"Solo puede ser eliminado por un usuario que tenga un Rol de Negocio asociado a al Negocio que le corresponde con este permiso ",
                    "permisos":"permission_classes = (IsAuthenticated,getPermisoEnEndpointEntidad_Can_GET('delete'),)"
                    },
                "view":{
                    "save":"",
                    "permisos_descripcion":"",
                    "permisos":""
                    
                    }
            }
        },
        "Imagen": {
            "campos": [
                {
                    "name": "id",
                    "type": "BigAutoField",
                    "related_model": "",
                    "descripcion_entrada":"",
                    "descripcion_salida":"",
                },
                {
                    "name": "Imagen",
                    "type": "ImageField",
                    "related_model": "",
                    "descripcion_entrada":"imagen",
                    "descripcion_salida":"",
                },
                {
                    "name": "TipoDeImagen",
                    "type": "ForeignKey",
                    "related_model": "TipoDeImagen",
                    "descripcion_entrada":"id del tipo de imagen",
                    "descripcion_salida":"",
                },
                {
                    "name": "Negocio",
                    "type": "ForeignKey",
                    "related_model": "Negocio",
                    "descripcion_entrada":"id del negocio, incluir si esta imagen pretenece a un negocio",
                    "descripcion_salida":"id del negocio, si esta imagen pretenece a un negocio si no es null",
                },
                {
                    "name": "Producto",
                    "type": "ForeignKey",
                    "related_model": "Producto",
                    "descripcion_entrada":"id del producto, incluir si esta imagen pretenece a un producto",
                    "descripcion_salida":"id del producto, si esta imagen pretenece a un producto si no es null",
                },
                {
                    "name": "Servicio",
                    "type": "ForeignKey",
                    "related_model": "Servicio",
                    "descripcion_entrada":"id del servicio, incluir si esta imagen pretenece a un servicio",
                    "descripcion_salida":"id del servicio, si esta imagen pretenece a un servicio si no es null",
                }
            ],
            "modeloLower": "imagen",
            "modelo_labelSingular": "Imagen",
            "modelo_labelPlurar": "Imagen",
            "modeloLower_labelSingular": "Imagen",
            "modeloLower_labelPlurar": "Imagen",
            "codigos":{
                "create":{
                    "save":"",
                    "permisos_descripcion":"",
                    "permisos":""
                    
                    },
                "list":{
                        "save":"",
                    "permisos_descripcion":"",
                    "permisos":""
                    },
                "edit":{
                        "save":"",
                    "permisos_descripcion":"",
                    "permisos":""
                    },
                "destroy":{
                        "save":"",
                    "permisos_descripcion":"",
                    "permisos":""
                    },
                "view":{
                    "save":"",
                    "permisos_descripcion":"",
                    "permisos":""
                    
                    }
            }
        },
        "TipoDeResenna": {
            "campos": [
                {
                    "name": "id",
                    "type": "BigAutoField",
                    "related_model": "",
                    "descripcion_entrada":"",
                    "descripcion_salida":"",
                },
                {
                    "name": "nombre",
                    "type": "CharField",
                    "related_model": "",
                    "descripcion_entrada":"tipo de reseña",
                    "descripcion_salida":"",
                }
            ],
            "modeloLower": "tipoderesenna",
            "modelo_labelSingular": "TipoDeResenna",
            "modelo_labelPlurar": "TipoDeResenna",
            "modeloLower_labelSingular": "TipoDeResenna",
            "modeloLower_labelPlurar": "TipoDeResenna",
            "codigos":{
                "create":{
                    "save":"",
                    "permisos_descripcion":"",
                    "permisos":""
                    
                    },
                "list":{
                        "save":"",
                    "permisos_descripcion":"",
                    "permisos":""
                    },
                "edit":{
                        "save":"",
                    "permisos_descripcion":"",
                    "permisos":""
                    },
                "destroy":{
                        "save":"",
                    "permisos_descripcion":"",
                    "permisos":""
                    },
                "view":{
                    "save":"",
                    "permisos_descripcion":"",
                    "permisos":""
                    
                    }
            }
        },
        "Resenna": {
            "campos": [
                {
                    "name": "id",
                    "type": "BigAutoField",
                    "related_model": "",
                    "descripcion_entrada":"",
                    "descripcion_salida":"",
                },
                {
                    "name": "texto",
                    "type": "TextField",
                    "related_model": "",
                    "descripcion_entrada":"texto de la reseña",
                    "descripcion_salida":"",
                },
                {
                    "name": "Negocio",
                    "type": "ForeignKey",
                    "related_model": "Negocio",
                    "descripcion_entrada":"id del negocio, incluir si pertenece a un negocio",
                    "descripcion_salida":"id del negocio, si pertenece a un negocio, si no es null",
                },
                {
                    "name": "Producto",
                    "type": "ForeignKey",
                    "related_model": "Producto",
                    "descripcion_entrada":"id del producto, incluir si pertenece a un producto",
                    "descripcion_salida":"id del producto, si pertenece a un producto, si no es null",
                },
                {
                    "name": "Servicio",
                    "type": "ForeignKey",
                    "related_model": "Servicio",
                    "descripcion_entrada":"id del servicio, incluir si pertenece a un servicio",
                    "descripcion_salida":"id del servicio, si pertenece a un servicio, si no es null",
                },
                {
                    "name": "user",
                    "type": "ForeignKey",
                    "related_model": "User",
                    "descripcion_entrada":"id del usuario",
                    "descripcion_salida":"",
                },
                {
                    "name": "TipoDeResenna",
                    "type": "ForeignKey",
                    "related_model": "TipoDeResenna",
                    "descripcion_entrada":"id del tipo de reseña",
                    "descripcion_salida":"",
                }
            ],
            "modeloLower": "resenna",
            "modelo_labelSingular": "Resenna",
            "modelo_labelPlurar": "Resenna",
            "modeloLower_labelSingular": "Resenna",
            "modeloLower_labelPlurar": "Resenna",
            "codigos":{
                "create":{
                    "save":"permission_classes = (IsAuthenticated,getPermisoEnEndpointEntidad_Tiene_GET(Resenna,'add'))",
                    "permisos_descripcion":"Este método requiere que el usuario esté autenticado para poder ser utilizado. La autenticación se realiza mediante el uso de una JWT (JSON Web Token) que se incluye en la cabecera de la solicitud HTTP. La JWT incluye información sobre el usuario autenticado, como su identidad y los permisos que se le han otorgado."
                    +"Requiere que el usuario tenga permitido realizar esta acción ",
                    "permisos":""
                    },
                "list":{
                        "save":"",
                    "permisos_descripcion":"",
                    "permisos":""
                    },
                "edit":{
                        "save":"permission_classes = (IsAuthenticated,getPermisoEnEndpointEntidad_Tiene_GET(Resenna,'change'))",
                    "permisos_descripcion":"Este método requiere que el usuario esté autenticado para poder ser utilizado. La autenticación se realiza mediante el uso de una JWT (JSON Web Token) que se incluye en la cabecera de la solicitud HTTP. La JWT incluye información sobre el usuario autenticado, como su identidad y los permisos que se le han otorgado."
                                           + "Requiere que el usuario tenga permitido realizar esta acción ",
                        "permisos":""
                    },
                "destroy":{
                        "save":"permission_classes = (IsAuthenticated,getPermisoEnEndpointEntidad_Tiene_GET(Resenna,'delete'))",
                    "permisos_descripcion":"Este método requiere que el usuario esté autenticado para poder ser utilizado. La autenticación se realiza mediante el uso de una JWT (JSON Web Token) que se incluye en la cabecera de la solicitud HTTP. La JWT incluye información sobre el usuario autenticado, como su identidad y los permisos que se le han otorgado."
                                           + "Requiere que el usuario tenga permitido realizar esta acción ",
                        "permisos":""
                    },
                "view":{
                    "save":"",
                    "permisos_descripcion":"",
                    "permisos":""
                    
                    }
            }
        },
        "TipoDeFavorito": {
            "campos": [
                {
                    "name": "id",
                    "type": "BigAutoField",
                    "related_model": "",
                    "descripcion_entrada":"",
                    "descripcion_salida":"",
                },
                {
                    "name": "nombre",
                    "type": "CharField",
                    "related_model": "",
                    "descripcion_entrada":"tipo de favorito",
                    "descripcion_salida":"",
                }
            ],
            "modeloLower": "tipodefavorito",
            "modelo_labelSingular": "TipoDeFavorito",
            "modelo_labelPlurar": "TipoDeFavorito",
            "modeloLower_labelSingular": "TipoDeFavorito",
            "modeloLower_labelPlurar": "TipoDeFavorito",
            "codigos":{
                "create":{
                    "save":"",
                    "permisos_descripcion":"",
                    "permisos":""
                    
                    },
                "list":{
                        "save":"",
                    "permisos_descripcion":"",
                    "permisos":""
                    },
                "edit":{
                        "save":"",
                    "permisos_descripcion":"",
                    "permisos":""
                    },
                "destroy":{
                        "save":"",
                    "permisos_descripcion":"",
                    "permisos":""
                    },
                "view":{
                    "save":"",
                    "permisos_descripcion":"",
                    "permisos":""
                    
                    }
            }
        },
        "Favorito": {
            "campos": [
                {
                    "name": "id",
                    "type": "BigAutoField",
                    "related_model": "",
                    "descripcion_entrada":"",
                    "descripcion_salida":"",
                },
                {
                    "name": "Negocio",
                    "type": "ForeignKey",
                    "related_model": "Negocio",
                    "descripcion_entrada": "id del negocio, incluir si pertenece a un negocio",
                    "descripcion_salida":"id del negocio, si pertenece a un negocio, si no s null",
                },
                {
                    "name": "Producto",
                    "type": "ForeignKey",
                    "related_model": "Producto",
                    "descripcion_entrada": "id del producto, incluir si pertenece a un producto",
                    "descripcion_salida":"id del producto, si pertenece a un producto, si no s null",
                },
                {
                    "name": "Servicio",
                    "type": "ForeignKey",
                    "related_model": "Servicio",
                    "descripcion_entrada": "id del servicio, incluir si pertenece a un servicio",
                    "descripcion_salida":"id del servicio, si pertenece a un servicio, si no s null",
                },
                {
                    "name": "user",
                    "type": "ForeignKey",
                    "related_model": "User",
                    "descripcion_entrada":"id del usuario",
                    "descripcion_salida":"",
                },
                {
                    "name": "TipoDeFavorito",
                    "type": "ForeignKey",
                    "related_model": "TipoDeFavorito",
                    "descripcion_entrada":"id del tipo de favorito",
                    "descripcion_salida":"",
                }
            ],
            "modeloLower": "favorito",
            "modelo_labelSingular": "Favorito",
            "modelo_labelPlurar": "Favorito",
            "modeloLower_labelSingular": "Favorito",
            "modeloLower_labelPlurar": "Favorito",
            "codigos":{
                "create":{
                    "save":"permission_classes = (IsAuthenticated,getPermisoEnEndpointEntidad_Tiene_GET(Resenna,'add'))",
                    "permisos_descripcion":"Este método requiere que el usuario esté autenticado para poder ser utilizado. La autenticación se realiza mediante el uso de una JWT (JSON Web Token) que se incluye en la cabecera de la solicitud HTTP. La JWT incluye información sobre el usuario autenticado, como su identidad y los permisos que se le han otorgado."
                    +"Requiere que el usuario tenga permitido realizar esta acción ",
                    "permisos":""
                    },
                "list":{
                        "save":"",
                    "permisos_descripcion":"",
                    "permisos":""
                    },
                "edit":{
                        "save":"permission_classes = (IsAuthenticated,getPermisoEnEndpointEntidad_Tiene_GET(Resenna,'change'))",
                    "permisos_descripcion":"Este método requiere que el usuario esté autenticado para poder ser utilizado. La autenticación se realiza mediante el uso de una JWT (JSON Web Token) que se incluye en la cabecera de la solicitud HTTP. La JWT incluye información sobre el usuario autenticado, como su identidad y los permisos que se le han otorgado."
                                           + "Requiere que el usuario tenga permitido realizar esta acción ",
                        "permisos":""
                    },
                "destroy":{
                        "save":"permission_classes = (IsAuthenticated,getPermisoEnEndpointEntidad_Tiene_GET(Resenna,'delete'))",
                    "permisos_descripcion":"Este método requiere que el usuario esté autenticado para poder ser utilizado. La autenticación se realiza mediante el uso de una JWT (JSON Web Token) que se incluye en la cabecera de la solicitud HTTP. La JWT incluye información sobre el usuario autenticado, como su identidad y los permisos que se le han otorgado."
                                           + "Requiere que el usuario tenga permitido realizar esta acción ",
                        "permisos":""
                    },
                "view":{
                    "save":"",
                    "permisos_descripcion":"",
                    "permisos":""
                    
                    }
            }
        },



    },
    "attribute_types": [
        "BigAutoField",
        "ForeignKey",
        "CharField",
        "ImageField",
        "TextField",
        "ManyToManyField",
        "BooleanField",
        "FloatField"
    ],
    "descripcionesAutomaticas":{
        "id":"id de la entidad en la base de datos"
    }
}
key_valores["models"]["User"]={
            "campos": [
                {
                    "name": "id",
                    "type": "BigAutoField",
                    "related_model": "",
                    "descripcion_entrada":"",
                    "descripcion_salida":"",
                },
                {
                    "name": "password",
                    "type": "CharField",
                    "related_model": "",
                    "descripcion_entrada":"contraseña",
                    "descripcion_salida":"",

                },
                {
                    "name": "last_login",
                    "type": "DateTimeField",
                    "related_model": "",
                    "descripcion_entrada":"último loguin",
                    "descripcion_salida":"",
                },
                {
                    "name": "is_superuser",
                    "type": "BooleanField",
                    "related_model": "",
                    "descripcion_entrada":"[True o False] es super usuario",
                    "descripcion_salida":"",
                },
                {
                    "name": "username",
                    "type": "CharField",
                    "related_model": "",
                    "descripcion_entrada":"username",
                    "descripcion_salida":"",
                },
                {
                    "name": "email",
                    "type": "EmailField",
                    "related_model": "",
                    "descripcion_entrada":"correo",
                    "descripcion_salida":"",
                },
                {
                    "name": "first_name",
                    "type": "CharField",
                    "related_model": "",
                    "descripcion_entrada":"primer nombre",
                    "descripcion_salida":"",
                },
                {
                    "name": "last_name",
                    "type": "CharField",
                    "related_model": "",
                    "descripcion_entrada":"apellidos",
                    "descripcion_salida":"",
                },
                {
                    "name": "image",
                    "type": "ImageField",
                    "related_model": "imagen de usuario",
                    "descripcion_entrada":"",
                    "descripcion_salida":"",
                },
                {
                    "name": "phone",
                    "type": "CharField",
                    "related_model": "",
                    "descripcion_entrada":"telefono",
                    "descripcion_salida":"",
                },
                {
                    "name": "is_active",
                    "type": "BooleanField",
                    "related_model": "",
                    "descripcion_entrada":"[enviar en True] esta activo",
                    "descripcion_salida":"esta activo",
                },
                {
                    "name": "is_staff",
                    "type": "BooleanField",
                    "related_model": "",
                    "descripcion_entrada":"[enviar en False] puede acceder a la administracion",
                    "descripcion_salida":"puede acceder a la administracion",
                },
                {
                    "name": "groups",
                    "type": "ManyToManyField",
                    "related_model": "Group",
                    "descripcion_entrada":"[enviar en vacio] id de Roles que puede tener por defecto",
                    "descripcion_salida":"id de Roles que puede tener por defecto",
                },
                {
                    "name": "user_permissions",
                    "type": "ManyToManyField",
                    "related_model": "Permission",
                    "descripcion_entrada":"[enviar en vacio] id de permisos que puede tener por defecto",
                    "descripcion_salida":"id de permisos que puede tener por defecto",
                }
            ],
            "modeloLower": "user",
            "modelo_labelSingular": "User",
            "modelo_labelPlurar": "User",
            "modeloLower_labelSingular": "User",
            "modeloLower_labelPlurar": "User",
            "codigos":{
                "create":{
                    "save":"",
                    "permisos_descripcion":"",
                    "permisos":""
                    
                    },
                "list":{
                        "save":"",
                    "permisos_descripcion":"",
                    "permisos":""
                    },
                "edit":{
                        "save":"",
                    "permisos_descripcion":"",
                    "permisos":""
                    },
                "destroy":{
                        "save":"",
                    "permisos_descripcion":"",
                    "permisos":""
                    },
                "view":{
                    "save":"",
                    "permisos_descripcion":"",
                    "permisos":""
                    
                    }
            }
        }
key_valores["models"]["Permission"]= {
            "campos": [
                {
                    "name": "id",
                    "type": "BigAutoField",
                    "related_model": "",
                    "descripcion_entrada":"",
                    "descripcion_salida":"",
                },
                {
                    "name": "name",
                    "type": "CharField",
                    "related_model": "",
                    "descripcion_entrada":"nombre del permiso",
                    "descripcion_salida":"",
                }
            ],
            "modeloLower": "permission",
            "modelo_labelSingular": "Permission",
            "modelo_labelPlurar": "Permission",
            "modeloLower_labelSingular": "Permission",
            "modeloLower_labelPlurar": "Permission",
            "codigos":{
                "create":{
                    "save":"",
                    "permisos_descripcion":"",
                    "permisos":""
                    
                    },
                "list":{
                        "save":"",
                    "permisos_descripcion":"",
                    "permisos":""
                    },
                "edit":{
                        "save":"",
                    "permisos_descripcion":"",
                    "permisos":""
                    },
                "destroy":{
                        "save":"",
                    "permisos_descripcion":"",
                    "permisos":""
                    },
                "view":{
                    "save":"",
                    "permisos_descripcion":"",
                    "permisos":""
                    
                    }
            }
        }
key_valores["models"]["Group"]= {
            "campos": [
                {
                    "name": "id",
                    "type": "BigAutoField",
                    "related_model": "",
                    "descripcion_entrada":"",
                    "descripcion_salida":"",
                },
                {
                    "name": "name",
                    "type": "CharField",
                    "related_model": "",
                    "descripcion_entrada":"nombre del Rol",
                    "descripcion_salida":"",
                },
                {
                    "name": "permissions",
                    "type": "ManyToManyField",
                    "related_model": "Permission",
                    "descripcion_entrada":"[#,#,#, ... ] lista de id de permisos realacionados a este rol",
                    "descripcion_salida":"",
                }
            ],
            "modeloLower": "group",
            "modelo_labelSingular": "Group",
            "modelo_labelPlurar": "Group",
            "modeloLower_labelSingular": "Group",
            "modeloLower_labelPlurar": "Group",
            "codigos":{
                "create":{
                    "save":"",
                    "permisos_descripcion":"",
                    "permisos":""
                    
                    },
                "list":{
                        "save":"",
                    "permisos_descripcion":"",
                    "permisos":""
                    },
                "edit":{
                        "save":"",
                    "permisos_descripcion":"",
                    "permisos":""
                    },
                "destroy":{
                        "save":"",
                    "permisos_descripcion":"",
                    "permisos":""
                    },
                "view":{
                    "save":"",
                    "permisos_descripcion":"",
                    "permisos":""
                    
                    }
            }
        }

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