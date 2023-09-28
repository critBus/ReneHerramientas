a="""

class {modelo}List(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = {modelo}Serializer
    model = {modelo}Serializer.Meta.model
    def get(self, request, format=None):
        \"\"\"
        Obtiene una lista de todos los {modeloLower_labelPlurar} registrados.

        Args:
            request: solicitud HTTP recibida.
            format: formato de la respuesta (opcional).

        Returns:
            Una respuesta HTTP con la lista de {modeloLower_labelPlurar} en formato JSON.
        \"\"\"
        entidad = self.model.objects.all()
        serializer =self.serializer_class(entidad, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        \"\"\"
        Crea un nuevo {modeloLower_labelSingular}.

        Args:
            request: solicitud HTTP recibida.
            format: formato de la respuesta (opcional).

        Returns:
            Si los datos son válidos, una respuesta HTTP con los datos del nuevo {modeloLower_labelSingular} en formato JSON y código de estado 201.
            Si los datos no son válidos, una respuesta HTTP con los errores de validación en formato JSON y código de estado 400.
        \"\"\"
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class {modelo}Detail(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = {modelo}Serializer
    model = {modelo}Serializer.Meta.model
    def get_object(self, pk):
        try:
            return self.model.objects.get(pk=pk)
        except self.model.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        entidad = self.get_object(pk)
        serializer = self.serializer_class(entidad)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        entidad = self.get_object(pk)
        serializer = self.serializer_class(entidad, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        entidad = self.get_object(pk)
        entidad.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
"""

b="""
    path('{modeloLower}/', {modelo}List.as_view(), name='{modeloLower}-list'),
    path('{modeloLower}/<int:pk>/', {modelo}Detail.as_view(), name='{modeloLower}-detail'),
"""

c="""
class {modelo}Serializer(serializers.ModelSerializer):
    class Meta:
        model = {modelo}
        fields = '__all__'
"""

d="""
class {modelo}_ListCreate(Base_ListCreate):
    \"\"\"
       Endpoint para la creación y listado de {modelo_labelPlurar}.

       POST:
       Crea una nueva entidad de {modelo_labelSingular} con los datos proporcionados en el cuerpo de la solicitud.
       Header: 'Content-Type': 'application/json'
       Formato de entrada POST:
            {
                {parametros_post_descripcion_crear} 

            }

        Formato de Salida POST:
            - 201 (Created): Creado con éxito
            {
                {parametros_salida_post_descripcion_crear}
            }
            - 400 (Bad Request): Los datos de entrada no son válidos
            {
                "campo erroneo": "descripción del error"
            }


       GET:
       Obtiene una lista de todas las entidades de {modelo_labelSingular} existentes, opcionalmente filtradas y ordenadas.

        Ejemplo de salida de solicitud GET:
           {
            "count": "cantidad de elementos en la lista",
            "next": "url del siguiente conjunto de elementos en la paginacion o null si no hay un siguinete conjunto de elementos",
            "previous": url del  conjunto anterior de elementos en la paginacion o null si no hay un conjunto anterior de elementos,
            "results": [
                    {
                        {parametros_salida_get_elmento_lista}
                    },

                    ...
                    
                ]
            }

       Parámetros de filtro:
                Ejemplo: &parametro de filtor1=valor a buscar1&parametro de filtor2=valor a buscar2
       {paremetros_get_filtro_lista} 

       Parámetros de busqueda:
            No utilizar junto a los parámetros de filtro  
           Parametro Principial: "search", busca cualquier coincidencia que incluye el valor pasado en el parametro secundario
                Ejemplo: &search=valor a buscar
           Parametro Secundarios por los que busca:
           {paremetros_get_search_lista} 

       Parámetros de ordenamiento: 
           Parametro Principial: "ordering", incluir un "-" delante del parametro secundario si se desea ordenar de forma desendiente
                Ejemplo: &ordering=-parametro secundario
           Parametro Secundarios:
           {paremetros_get_ordenamiento_lista} 

    \"\"\"
    serializer_class = {modelo}Serializer
    filter_backends = [DjangoFilterBackend,
                       SearchFilter,
                       OrderingFilter,
                       ]
    {atributosExtra} 
    

class {modelo}_RUD(Base_RUD):
    \"\"\"
        Endpoint para la obtención, actualización y eliminación de una entidad de {modelo_labelSingular} específica.

        Parámetros de entrada:
        - id: Identificador único de la entidad a obtener, actualizar o eliminar.

        - 404 (Not Found):
            {
                "detail": "No encontrado."
            }

        GET:
        Obtiene la entidad de {modelo_labelSingular} con el id proporcionado.

            Ejemplo de salida de solicitud GET:
            {
                {parametros_salida_get_RUD}
            }

        PUT:
        Actualiza la entidad de {modelo_labelSingular} con el id proporcionado con los datos proporcionados en el cuerpo de la solicitud.

            Ejemplo de solicitud PUT:
            {
                {parametros_entrada_put_RUD}
            }

            Ejemplo de salida de solicitud PUT:
            {
                {parametros_salida_put_RUD}
            }

            - 400 (Bad Request): Los datos de entrada no son válidos
            {
                "campo erroneo": "descripción del error"
            }

        DELETE:
        Elimina la entidad de {modelo_labelSingular} con el id proporcionado.

    \"\"\"
    serializer_class = {modelo}Serializer
"""

e="""
    path('{modeloLower}/', {modelo}_ListCreate.as_view(), name='{modeloLower}-list'),
    path('{modeloLower}/<int:pk>/', {modelo}_RUD.as_view(), name='{modeloLower}-detail'),
"""

f="""

class {modelo}_List(Base_List):
    \"\"\"
        {permisos_descripcion_list} 

       Endpoint para el listado de {modelo_labelPlurar}.

       GET:
       Obtiene una lista de todas las entidades de {modelo_labelSingular} existentes, opcionalmente filtradas y ordenadas.

        Ejemplo de salida de solicitud GET:
           {
            "count": "cantidad de elementos en la lista",
            "next": "url del siguiente conjunto de elementos en la paginacion o null si no hay un siguinete conjunto de elementos",
            "previous": url del  conjunto anterior de elementos en la paginacion o null si no hay un conjunto anterior de elementos,
            "results": [
                    {
                        {parametros_salida_get_elmento_lista}
                    },

                    ...
                    
                ]
            }

       Parámetros de filtro:
                Ejemplo: &parametro de filtor1=valor a buscar1&parametro de filtor2=valor a buscar2
       {paremetros_get_filtro_lista} 

       Parámetros de busqueda:
            No utilizar junto a los parámetros de filtro  
           Parametro Principial: "search", busca cualquier coincidencia que incluye el valor pasado en el parametro secundario
                Ejemplo: &search=valor a buscar
           Parametro Secundarios por los que busca:
           {paremetros_get_search_lista} 

       Parámetros de ordenamiento: 
           Parametro Principial: "ordering", incluir un "-" delante del parametro secundario si se desea ordenar de forma desendiente
                Ejemplo: &ordering=-parametro secundario
           Parametro Secundarios:
           {paremetros_get_ordenamiento_lista} 

    \"\"\"
    {permisos_list} 
    serializer_class = {modeloSerializer_list}
    filter_backends = [DjangoFilterBackend,
                       SearchFilter,
                       OrderingFilter,
                       ]
    {atributosExtra} 

class {modelo}_Retrieve(Base_Retrieve):
    \"\"\"
        {permisos_descripcion_retrieve}

        Endpoint para la obtención de una entidad de {modelo_labelSingular} específica.

        Parámetros de entrada:
        - id: Identificador único de la entidad a obtener, actualizar o eliminar.

        - 404 (Not Found):
            {
                "detail": "No encontrado."
            }

        GET:
        Obtiene la entidad de {modelo_labelSingular} con el id proporcionado.

            Ejemplo de salida de solicitud GET:
            {
                {parametros_salida_get_RUD}
            }

        
    \"\"\"
    {permisos_retrieve} 
    serializer_class = {modeloSerializer_retrieve}

class {modelo}_Create(Base_Create):
    \"\"\"
        {permisos_descripcion_create}

       Endpoint para la creación de {modelo_labelSingular}.

       POST:
       Crea una nueva entidad de {modelo_labelSingular} con los datos proporcionados en el cuerpo de la solicitud.
       Header: 'Content-Type': 'application/json'
       Formato de entrada POST:
            {
                {parametros_post_descripcion_crear} 

            }

        Formato de Salida POST:
            - 201 (Created): Creado con éxito
            {
                {parametros_salida_post_descripcion_crear}
            }
            - 400 (Bad Request): Los datos de entrada no son válidos
            {
                "campo erroneo": "descripción del error"
            }

        
    \"\"\"
    {permisos_create} 
    serializer_class = {modeloSerializer_create}

    {save_create}


class {modelo}_Update(Base_Update):
    \"\"\"
        {permisos_descripcion_update}

        Endpoint para la actualización de una entidad de {modelo_labelSingular} específica.

        Parámetros de entrada:
        - id: Identificador único de la entidad a obtener, actualizar o eliminar.

        - 404 (Not Found):
            {
                "detail": "No encontrado."
            }

        
        PUT:
        Actualiza la entidad de {modelo_labelSingular} con el id proporcionado con los datos proporcionados en el cuerpo de la solicitud.

            Ejemplo de solicitud PUT:
            {
                {parametros_entrada_put_RUD}
            }

            Ejemplo de salida de solicitud PUT:
            {
                {parametros_salida_put_RUD}
            }

            - 400 (Bad Request): Los datos de entrada no son válidos
            {
                "campo erroneo": "descripción del error"
            }

        

    \"\"\"

    serializer_class = {modeloSerializer_update}
    {permisos_update} 
    {save_update}

class {modelo}_Destroy(Base_Destroy):
    \"\"\"
        {permisos_descripcion_destroy}

        Endpoint para la eliminación de una entidad de {modelo_labelSingular} específica.

        Parámetros de entrada:
        - id: Identificador único de la entidad a obtener, actualizar o eliminar.

        - 404 (Not Found):
            {
                "detail": "No encontrado."
            }

        
        DELETE:
        Elimina la entidad de {modelo_labelSingular} con el id proporcionado.

    \"\"\"
    {permisos_destroy} 
    serializer_class = {modeloSerializer_destroy}
    {save_destroy}




"""

g="""
    path('{modeloLower}/findById/<int:pk>/', {modelo}_Retrieve.as_view()),
    path('{modeloLower}/delete/<int:pk>/', {modelo}_Destroy.as_view()),
    path('{modeloLower}/update/<int:pk>/', {modelo}_Update.as_view()),
    path('{modeloLower}/list/', {modelo}_List.as_view()),
    path('{modeloLower}/create/', {modelo}_Create.as_view()),

"""

h="""
        ----------------------------------------------------------------------------

        {modelo}

        ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

        {modeloLower}/list/

        GET:

        {permisos_descripcion_list} 

       Endpoint para el listado de {modelo_labelPlurar}.

       
       Obtiene una lista de todas las entidades de {modelo_labelSingular} existentes, opcionalmente filtradas y ordenadas.

        Ejemplo de salida de solicitud GET:
           {
            "count": "cantidad de elementos en la lista",
            "next": "url del siguiente conjunto de elementos en la paginacion o null si no hay un siguinete conjunto de elementos",
            "previous": url del  conjunto anterior de elementos en la paginacion o null si no hay un conjunto anterior de elementos,
            "results": [
                    {
                        {parametros_salida_get_elmento_lista}
                    },

                    ...
                    
                ]
            }

       Parámetros de filtro:
                Ejemplo: &parametro de filtor1=valor a buscar1&parametro de filtor2=valor a buscar2
       {paremetros_get_filtro_lista} 

       Parámetros de busqueda:
            No utilizar junto a los parámetros de filtro  
           Parametro Principial: "search", busca cualquier coincidencia que incluye el valor pasado en el parametro secundario
                Ejemplo: &search=valor a buscar
           Parametro Secundarios por los que busca:
           {paremetros_get_search_lista} 

       Parámetros de ordenamiento: 
           Parametro Principial: "ordering", incluir un "-" delante del parametro secundario si se desea ordenar de forma desendiente
                Ejemplo: &ordering=-parametro secundario
           Parametro Secundarios:
           {paremetros_get_ordenamiento_lista} 

   
        +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


        {modeloLower}/findById/<int:pk>/

        GET:


        {permisos_descripcion_retrieve}

        Endpoint para la obtención de una entidad de {modelo_labelSingular} específica.

        Parámetros de entrada:
        - id: Identificador único de la entidad a obtener, actualizar o eliminar.

        - 404 (Not Found):
            {
                "detail": "No encontrado."
            }

        
        Obtiene la entidad de {modelo_labelSingular} con el id proporcionado.

            Ejemplo de salida de solicitud GET:
            {
                {parametros_salida_get_RUD}
            }

        
  
        ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


        {modeloLower}/create/

        POST:


        {permisos_descripcion_create}

       Endpoint para la creación de {modelo_labelSingular}.

       
       Crea una nueva entidad de {modelo_labelSingular} con los datos proporcionados en el cuerpo de la solicitud.
       Header: 'Content-Type': 'application/json'
       Formato de entrada POST:
            {
                {parametros_post_descripcion_crear} 

            }

        Formato de Salida POST:
            - 201 (Created): Creado con éxito
            {
                {parametros_salida_post_descripcion_crear}
            }
            - 400 (Bad Request): Los datos de entrada no son válidos
            {
                "campo erroneo": "descripción del error"
            }

        

        +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


        {modeloLower}/update/<int:pk>/

        PUT:

        {permisos_descripcion_update}

        Endpoint para la actualización de una entidad de {modelo_labelSingular} específica.

        Parámetros de entrada:
        - id: Identificador único de la entidad a obtener, actualizar o eliminar.

        - 404 (Not Found):
            {
                "detail": "No encontrado."
            }

        
        
        Actualiza la entidad de {modelo_labelSingular} con el id proporcionado con los datos proporcionados en el cuerpo de la solicitud.

            Ejemplo de solicitud PUT:
            {
                {parametros_entrada_put_RUD}
            }

            Ejemplo de salida de solicitud PUT:
            {
                {parametros_salida_put_RUD}
            }

            - 400 (Bad Request): Los datos de entrada no son válidos
            {
                "campo erroneo": "descripción del error"
            }

        

        +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


        {modeloLower}/delete/<int:pk>/

        DELETE:

        {permisos_descripcion_destroy}

        Endpoint para la eliminación de una entidad de {modelo_labelSingular} específica.

        Parámetros de entrada:
        - id: Identificador único de la entidad a obtener, actualizar o eliminar.

        - 404 (Not Found):
            {
                "detail": "No encontrado."
            }

        
        DELETE:
        Elimina la entidad de {modelo_labelSingular} con el id proporcionado.

    
        +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++



"""

ij="""
{modelo}

{atributosExtra} 

"""
# Ejemplo de solicitud GET:
#        {ejemplo_get_lista} 