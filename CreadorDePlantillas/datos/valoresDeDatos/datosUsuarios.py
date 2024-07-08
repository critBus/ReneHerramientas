datos_usuarios = {"models": {}}

datos_usuarios["models"]["User"] = {
    "campos": [
        {
            "name": "id",
            "type": "BigAutoField",
            "related_model": "",
            "descripcion_entrada": "",
            "descripcion_salida": "",
        },
        {
            "name": "password",
            "type": "CharField",
            "related_model": "",
            "descripcion_entrada": "contraseña",
            "descripcion_salida": "",
        },
        {
            "name": "last_login",
            "type": "DateTimeField",
            "related_model": "",
            "descripcion_entrada": "último loguin",
            "descripcion_salida": "",
        },
        {
            "name": "is_superuser",
            "type": "BooleanField",
            "related_model": "",
            "descripcion_entrada": "[True o False] es super usuario",
            "descripcion_salida": "",
        },
        {
            "name": "username",
            "type": "CharField",
            "related_model": "",
            "descripcion_entrada": "username",
            "descripcion_salida": "",
        },
        {
            "name": "email",
            "type": "EmailField",
            "related_model": "",
            "descripcion_entrada": "correo",
            "descripcion_salida": "",
        },
        {
            "name": "first_name",
            "type": "CharField",
            "related_model": "",
            "descripcion_entrada": "primer nombre",
            "descripcion_salida": "",
        },
        {
            "name": "last_name",
            "type": "CharField",
            "related_model": "",
            "descripcion_entrada": "apellidos",
            "descripcion_salida": "",
        },
        {
            "name": "image",
            "type": "ImageField",
            "related_model": "imagen de usuario",
            "descripcion_entrada": "",
            "descripcion_salida": "",
        },
        {
            "name": "phone",
            "type": "CharField",
            "related_model": "",
            "descripcion_entrada": "telefono",
            "descripcion_salida": "",
        },
        {
            "name": "is_active",
            "type": "BooleanField",
            "related_model": "",
            "descripcion_entrada": "[enviar en True] esta activo",
            "descripcion_salida": "esta activo",
        },
        {
            "name": "is_staff",
            "type": "BooleanField",
            "related_model": "",
            "descripcion_entrada": "[enviar en False] puede acceder a la administracion",
            "descripcion_salida": "puede acceder a la administracion",
        },
        {
            "name": "groups",
            "type": "ManyToManyField",
            "related_model": "Group",
            "descripcion_entrada": "[enviar en vacio] id de Roles que puede tener por defecto",
            "descripcion_salida": "id de Roles que puede tener por defecto",
        },
        {
            "name": "user_permissions",
            "type": "ManyToManyField",
            "related_model": "Permission",
            "descripcion_entrada": "[enviar en vacio] id de permisos que puede tener por defecto",
            "descripcion_salida": "id de permisos que puede tener por defecto",
        },
    ],
    "modeloLower": "user",
    "modelo_labelSingular": "User",
    "modelo_labelPlurar": "User",
    "modeloLower_labelSingular": "User",
    "modeloLower_labelPlurar": "User",
    "codigos": {
        "create": {
            "save": """

        def post(self, request, *args, **kwargs):
        try:
            # for nombre_rol in NOMBRE_ROLES:
            #     grupo=get_group(nombre_grupo=nombre_rol)
            #     if not grupo:
            #
            #         return JsonResponse({'status': 'error', 'message': f'no se ha creado el rol {nombre_rol}'}, status=500)

            data=getData(request)
            username = None
            if data and "username" in data:
                username = data["username"]

            # esAppNegocio = esAppNegocioEnData(data)

        except:
            print(traceback.format_exc())
            return JsonResponse({'status': 'error', 'message': 'Error de en servidor'}, status=500)

        #orginal
        response=self.create(request, *args, **kwargs)
        #fin original

        try:
            if response.status_code >= 200 and response.status_code <= 299:
                if username:
                    usuario=User.objects.filter(username=username).first()
                    if usuario:

                        if usuario.password.startswith('pbkdf2'):
                            usuario.password = usuario.password
                        else:
                            usuario.set_password(usuario.password)
                            usuario.save()

                        # rolUsuarioCliente = RolNegocio()
                        # rolUsuarioCliente.user = usuario
                        # rolUsuarioCliente.rol = get_group(nombre_grupo=NOMBRE_ROL_CLIENTE)
                        # rolUsuarioCliente.nombre = NOMBRE_ROL_CLIENTE
                        # rolUsuarioCliente.save()
                        #
                        # if esAppNegocio:
                        #     for nombre_rol in [NOMBRE_ROL_TRABAJADOR
                        #         , NOMBRE_ROL_ADMINISTRADOR
                        #         , NOMBRE_ROL_PROPIETARIO]:
                        #         get_y_crear_rol_negocio_si_es_necesario(
                        #             usuario=usuario
                        #             ,nombre_rol=nombre_rol
                        #         )
                        #         # rolUsuario = RolNegocio()
                        #         # rolUsuario.user = usuario
                        #         # rolUsuario.rol = get_group(nombre_grupo=nombre_rol)
                        #         # rolUsuario.nombre = nombre_rol
                        #         # rolUsuario.save()

                        comprobarYmodificarSiEsAppNegocio( response=response
                                                          , data=data)
            response.data['password']=""
            return response
        except:
            print(traceback.format_exc())
            return JsonResponse({'status': 'error', 'message': 'Error de en servidor'}, status=500)

                    """,
            "permisos_descripcion": "",
            "permisos": "",
        },
        "list": {
            "save": "",
            "permisos_descripcion": "",
            "permisos": "",
            "serializer": "UserListSerializer",
        },
        "edit": {
            "save": """
    def put(self, request, *args, **kwargs):
        try:
            data = getData(request)
            username = None
            if data and "username" in data:
                username = data["username"]



        except:
            print(traceback.format_exc())
            return JsonResponse({'status': 'error', 'message': 'Error de en servidor'}, status=500)
        #original
        response=self.update(request, *args, **kwargs)
        #fin original
        try:
            if response.status_code >= 200 and response.status_code <= 299:
                if username:
                    usuario=User.objects.filter(username=username).first()
                    if usuario and 'password' in data:
                        password=data['password']
                        if not password.startswith('pbkdf2'):
                            print("modifico la contraseña")
                            usuario.set_password(password)
                            usuario.save()
            response.data['password'] = ""
            return response
        except:
            print(traceback.format_exc())
            return JsonResponse({'status': 'error', 'message': 'Error de en servidor'}, status=500)

                        """,
            "permisos_descripcion": "{- IsAuthenticated -}\n{- SoloPuedeModificarseElMismo_OEsSuperusuario -}",
            "permisos": "permission_classes = (IsAuthenticated,SoloPuedeModificarseElMismo_OEsSuperusuario,)",
            "serializer": "UserUpdateSerializer",
        },
        "destroy": {
            "save": "",
            "permisos_descripcion": "{- IsAuthenticated -}\n{- SoloPuedeModificarseElMismo_OEsSuperusuario -}",
            "permisos": "permission_classes = (IsAuthenticated, SoloPuedeModificarseElMismo_OEsSuperusuario,)",
        },
        "view": {
            "save": "",
            "permisos_descripcion": "",
            "permisos": "",
            "serializer": "UserRetrieveSerializer",
        },
    },
}
datos_usuarios["models"]["Permission"] = {
    "campos": [
        {
            "name": "id",
            "type": "BigAutoField",
            "related_model": "",
            "descripcion_entrada": "",
            "descripcion_salida": "",
        },
        {
            "name": "name",
            "type": "CharField",
            "related_model": "",
            "descripcion_entrada": "nombre del permiso",
            "descripcion_salida": "",
        },
    ],
    "modeloLower": "permission",
    "modelo_labelSingular": "Permission",
    "modelo_labelPlurar": "Permission",
    "modeloLower_labelSingular": "Permission",
    "modeloLower_labelPlurar": "Permission",
    "codigos": {
        "create": {
            "save": "",
            "permisos_descripcion": "{- IsAuthenticated -}" + "\n{- EsSuperUsuario -}",
            "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
        },
        "list": {"save": "", "permisos_descripcion": "", "permisos": ""},
        "edit": {
            "save": "",
            "permisos_descripcion": "{- IsAuthenticated -}" + "\n{- EsSuperUsuario -}",
            "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
        },
        "destroy": {
            "save": "",
            "permisos_descripcion": "{- IsAuthenticated -}" + "\n{- EsSuperUsuario -}",
            "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
        },
        "view": {"save": "", "permisos_descripcion": "", "permisos": ""},
    },
}
datos_usuarios["models"]["Group"] = {
    "campos": [
        {
            "name": "id",
            "type": "BigAutoField",
            "related_model": "",
            "descripcion_entrada": "",
            "descripcion_salida": "",
        },
        {
            "name": "name",
            "type": "CharField",
            "related_model": "",
            "descripcion_entrada": "nombre del Rol",
            "descripcion_salida": "",
        },
        {
            "name": "permissions",
            "type": "ManyToManyField",
            "related_model": "Permission",
            "descripcion_entrada": "[#,#,#, ... ] lista de id de permisos realacionados a este rol",
            "descripcion_salida": "",
        },
    ],
    "modeloLower": "group",
    "modelo_labelSingular": "Group",
    "modelo_labelPlurar": "Group",
    "modeloLower_labelSingular": "Group",
    "modeloLower_labelPlurar": "Group",
    "codigos": {
        "create": {
            "save": "",
            "permisos_descripcion": "{- IsAuthenticated -}" + "\n{- EsSuperUsuario -}",
            "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
        },
        "list": {"save": "", "permisos_descripcion": "", "permisos": ""},
        "edit": {
            "save": "",
            "permisos_descripcion": "{- IsAuthenticated -}" + "\n{- EsSuperUsuario -}",
            "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
        },
        "destroy": {
            "save": "",
            "permisos_descripcion": "{- IsAuthenticated -}" + "\n{- EsSuperUsuario -}",
            "permisos": "permission_classes = (IsAuthenticated,EsSuperUsuario,)",
        },
        "view": {"save": "", "permisos_descripcion": "", "permisos": ""},
    },
}
