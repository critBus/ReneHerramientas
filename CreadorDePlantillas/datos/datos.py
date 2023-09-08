key_valores={
    "models": {
        "RolNegocio": {
            "campos": [
                {
                    "name": "id",
                    "type": "BigAutoField"
                },
                {
                    "name": "rol",
                    "type": "ForeignKey"
                },
                {
                    "name": "user",
                    "type": "ForeignKey"
                }
            ],
            "modeloLower": "rolnegocio",
            "modelo_labelSingular": "RolNegocio",
            "modelo_labelPlurar": "RolNegocio",
            "modeloLower_labelSingular": "RolNegocio",
            "modeloLower_labelPlurar": "RolNegocio"
        },
        "PalabraClave": {
            "campos": [
                {
                    "name": "id",
                    "type": "BigAutoField"
                },
                {
                    "name": "nombre",
                    "type": "CharField"
                }
            ],
            "modeloLower": "palabraclave",
            "modelo_labelSingular": "PalabraClave",
            "modelo_labelPlurar": "PalabraClave",
            "modeloLower_labelSingular": "PalabraClave",
            "modeloLower_labelPlurar": "PalabraClave"
        },
        "TipoDeGestion": {
            "campos": [
                {
                    "name": "id",
                    "type": "BigAutoField"
                },
                {
                    "name": "nombre",
                    "type": "CharField"
                }
            ],
            "modeloLower": "tipodegestion",
            "modelo_labelSingular": "TipoDeGestion",
            "modelo_labelPlurar": "TipoDeGestion",
            "modeloLower_labelSingular": "TipoDeGestion",
            "modeloLower_labelPlurar": "TipoDeGestion"
        },
        "CategoriaDeNegocio": {
            "campos": [
                {
                    "name": "id",
                    "type": "BigAutoField"
                },
                {
                    "name": "nombre",
                    "type": "CharField"
                }
            ],
            "modeloLower": "categoriadenegocio",
            "modelo_labelSingular": "CategoriaDeNegocio",
            "modelo_labelPlurar": "CategoriaDeNegocio",
            "modeloLower_labelSingular": "CategoriaDeNegocio",
            "modeloLower_labelPlurar": "CategoriaDeNegocio"
        },
        "Negocio": {
            "campos": [
                {
                    "name": "id",
                    "type": "BigAutoField"
                },
                {
                    "name": "nombre",
                    "type": "CharField"
                },
                {
                    "name": "logo",
                    "type": "ImageField"
                },
                {
                    "name": "slogan",
                    "type": "CharField"
                },
                {
                    "name": "direccion",
                    "type": "CharField"
                },
                {
                    "name": "descripcion",
                    "type": "TextField"
                },
                {
                    "name": "TipoDeGestion",
                    "type": "ForeignKey"
                }
            ],
            "modeloLower": "negocio",
            "modelo_labelSingular": "Negocio",
            "modelo_labelPlurar": "Negocio",
            "modeloLower_labelSingular": "Negocio",
            "modeloLower_labelPlurar": "Negocio"
        },
        "TipoDeContacto": {
            "campos": [
                {
                    "name": "id",
                    "type": "BigAutoField"
                },
                {
                    "name": "nombre",
                    "type": "CharField"
                }
            ],
            "modeloLower": "tipodecontacto",
            "modelo_labelSingular": "TipoDeContacto",
            "modelo_labelPlurar": "TipoDeContacto",
            "modeloLower_labelSingular": "TipoDeContacto",
            "modeloLower_labelPlurar": "TipoDeContacto"
        },
        "Contacto": {
            "campos": [
                {
                    "name": "id",
                    "type": "BigAutoField"
                },
                {
                    "name": "nombre",
                    "type": "CharField"
                },
                {
                    "name": "TipoDeContacto",
                    "type": "ForeignKey"
                },
                {
                    "name": "Negocio",
                    "type": "ForeignKey"
                }
            ],
            "modeloLower": "contacto",
            "modelo_labelSingular": "Contacto",
            "modelo_labelPlurar": "Contacto",
            "modeloLower_labelSingular": "Contacto",
            "modeloLower_labelPlurar": "Contacto"
        },
        "CategoriaDeServicio": {
            "campos": [
                {
                    "name": "id",
                    "type": "BigAutoField"
                },
                {
                    "name": "nombre",
                    "type": "CharField"
                },
                {
                    "name": "Negocio",
                    "type": "ForeignKey"
                }
            ],
            "modeloLower": "categoriadeservicio",
            "modelo_labelSingular": "CategoriaDeServicio",
            "modelo_labelPlurar": "CategoriaDeServicio",
            "modeloLower_labelSingular": "CategoriaDeServicio",
            "modeloLower_labelPlurar": "CategoriaDeServicio"
        },
        "CategoriaDeProducto": {
            "campos": [
                {
                    "name": "id",
                    "type": "BigAutoField"
                },
                {
                    "name": "nombre",
                    "type": "CharField"
                },
                {
                    "name": "Negocio",
                    "type": "ForeignKey"
                }
            ],
            "modeloLower": "categoriadeproducto",
            "modelo_labelSingular": "CategoriaDeProducto",
            "modelo_labelPlurar": "CategoriaDeProducto",
            "modeloLower_labelSingular": "CategoriaDeProducto",
            "modeloLower_labelPlurar": "CategoriaDeProducto"
        },
        "Producto": {
            "campos": [
                {
                    "name": "id",
                    "type": "BigAutoField"
                },
                {
                    "name": "Nombre",
                    "type": "CharField"
                },
                {
                    "name": "Disponibilidad",
                    "type": "BooleanField"
                },
                {
                    "name": "Precio_actual",
                    "type": "FloatField"
                },
                {
                    "name": "Precio_anterior",
                    "type": "FloatField"
                },
                {
                    "name": "Descripcion",
                    "type": "TextField"
                },
                {
                    "name": "Categoria",
                    "type": "ForeignKey"
                }
            ],
            "modeloLower": "producto",
            "modelo_labelSingular": "Producto",
            "modelo_labelPlurar": "Producto",
            "modeloLower_labelSingular": "Producto",
            "modeloLower_labelPlurar": "Producto"
        },
        "TipoDeImagen": {
            "campos": [
                {
                    "name": "id",
                    "type": "BigAutoField"
                },
                {
                    "name": "nombre",
                    "type": "CharField"
                }
            ],
            "modeloLower": "tipodeimagen",
            "modelo_labelSingular": "TipoDeImagen",
            "modelo_labelPlurar": "TipoDeImagen",
            "modeloLower_labelSingular": "TipoDeImagen",
            "modeloLower_labelPlurar": "TipoDeImagen"
        },
        "Servicio": {
            "campos": [
                {
                    "name": "id",
                    "type": "BigAutoField"
                },
                {
                    "name": "Nombre",
                    "type": "CharField"
                },
                {
                    "name": "Disponibilidad",
                    "type": "BooleanField"
                },
                {
                    "name": "Precio_actual",
                    "type": "FloatField"
                },
                {
                    "name": "Precio_anterior",
                    "type": "FloatField"
                },
                {
                    "name": "Descripcion",
                    "type": "TextField"
                },
                {
                    "name": "Categoria",
                    "type": "ForeignKey"
                }
            ],
            "modeloLower": "servicio",
            "modelo_labelSingular": "Servicio",
            "modelo_labelPlurar": "Servicio",
            "modeloLower_labelSingular": "Servicio",
            "modeloLower_labelPlurar": "Servicio"
        },
        "Imagen": {
            "campos": [
                {
                    "name": "id",
                    "type": "BigAutoField"
                },
                {
                    "name": "Imagen",
                    "type": "ImageField"
                },
                {
                    "name": "TipoDeImagen",
                    "type": "ForeignKey"
                },
                {
                    "name": "Negocio",
                    "type": "ForeignKey"
                },
                {
                    "name": "Producto",
                    "type": "ForeignKey"
                },
                {
                    "name": "Servicio",
                    "type": "ForeignKey"
                }
            ],
            "modeloLower": "imagen",
            "modelo_labelSingular": "Imagen",
            "modelo_labelPlurar": "Imagen",
            "modeloLower_labelSingular": "Imagen",
            "modeloLower_labelPlurar": "Imagen"
        },
        "TipoDeResenna": {
            "campos": [
                {
                    "name": "id",
                    "type": "BigAutoField"
                },
                {
                    "name": "nombre",
                    "type": "CharField"
                }
            ],
            "modeloLower": "tipoderesenna",
            "modelo_labelSingular": "TipoDeResenna",
            "modelo_labelPlurar": "TipoDeResenna",
            "modeloLower_labelSingular": "TipoDeResenna",
            "modeloLower_labelPlurar": "TipoDeResenna"
        },
        "Resenna": {
            "campos": [
                {
                    "name": "id",
                    "type": "BigAutoField"
                },
                {
                    "name": "texto",
                    "type": "TextField"
                },
                {
                    "name": "Negocio",
                    "type": "ForeignKey"
                },
                {
                    "name": "Producto",
                    "type": "ForeignKey"
                },
                {
                    "name": "Servicio",
                    "type": "ForeignKey"
                },
                {
                    "name": "user",
                    "type": "ForeignKey"
                },
                {
                    "name": "TipoDeResenna",
                    "type": "ForeignKey"
                }
            ],
            "modeloLower": "resenna",
            "modelo_labelSingular": "Resenna",
            "modelo_labelPlurar": "Resenna",
            "modeloLower_labelSingular": "Resenna",
            "modeloLower_labelPlurar": "Resenna"
        },
        "TipoDeFavorito": {
            "campos": [
                {
                    "name": "id",
                    "type": "BigAutoField"
                },
                {
                    "name": "nombre",
                    "type": "CharField"
                }
            ],
            "modeloLower": "tipodefavorito",
            "modelo_labelSingular": "TipoDeFavorito",
            "modelo_labelPlurar": "TipoDeFavorito",
            "modeloLower_labelSingular": "TipoDeFavorito",
            "modeloLower_labelPlurar": "TipoDeFavorito"
        },
        "Favorito": {
            "campos": [
                {
                    "name": "id",
                    "type": "BigAutoField"
                },
                {
                    "name": "Negocio",
                    "type": "ForeignKey"
                },
                {
                    "name": "Producto",
                    "type": "ForeignKey"
                },
                {
                    "name": "Servicio",
                    "type": "ForeignKey"
                },
                {
                    "name": "user",
                    "type": "ForeignKey"
                },
                {
                    "name": "TipoDeFavorito",
                    "type": "ForeignKey"
                }
            ],
            "modeloLower": "favorito",
            "modelo_labelSingular": "Favorito",
            "modelo_labelPlurar": "Favorito",
            "modeloLower_labelSingular": "Favorito",
            "modeloLower_labelPlurar": "Favorito"
        },
        "DatosUsuario": {
            "campos": [
                {
                    "name": "id",
                    "type": "BigAutoField"
                },
                {
                    "name": "user",
                    "type": "ForeignKey"
                },
                {
                    "name": "imagenUsuario",
                    "type": "ImageField"
                },
                {
                    "name": "telefono",
                    "type": "CharField"
                },
                {
                    "name": "utilizoAppNegocio",
                    "type": "BooleanField"
                }
            ],
            "modeloLower": "datosusuario",
            "modelo_labelSingular": "DatosUsuario",
            "modelo_labelPlurar": "DatosUsuario",
            "modeloLower_labelSingular": "DatosUsuario",
            "modeloLower_labelPlurar": "DatosUsuario"
        }
    },
    "attribute_types": [
        "BigAutoField",
        "ForeignKey",
        "CharField",
        "ImageField",
        "TextField",
        "BooleanField",
        "FloatField"
    ]
}