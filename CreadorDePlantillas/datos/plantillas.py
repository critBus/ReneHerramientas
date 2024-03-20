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

urls="""
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

filtros_doc="""
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        {modelo}  
    

        Parámetros de filtro:
                Ejemplo: &parametro de filtor1=valor a buscar1&parametro de filtor2=valor a buscar2
       {paremetros_get_filtro_lista} 

        


--------------------------------------------------------------------------
"""

plantilla_serializer="""
class {modelo}Serializer(serializers.ModelSerializer):
    {parametrosSerializer}
    class Meta:
        model = {modelo}
        fields = '__all__'
    
class {modelo}Serializer_Representation(serializers.ModelSerializer):
    class Meta:
        model = {modelo}
        fields = '__all__'
    def to_representation(self, value):
        return {modelo}Serializer(value).data
class {modelo}Serializer_List(serializers.ModelSerializer):
    class Meta:
        model = {modelo}
        fields = '__all__'
    def to_representation(self, value):
        return {modelo}Serializer_Representation(value).data
class {modelo}Serializer_Retrieve(serializers.ModelSerializer):
    class Meta:
        model = {modelo}
        fields = '__all__'
    def to_representation(self, value):
        return {modelo}Serializer_Representation(value).data
class {modelo}Serializer_Create(serializers.ModelSerializer):
    class Meta:
        model = {modelo}
        fields = '__all__'
    def to_representation(self, value):
        return {modelo}Serializer_Representation(value).data
    
class {modelo}Serializer_Update(serializers.ModelSerializer):
    class Meta:
        model = {modelo}
        fields = '__all__'
    def to_representation(self, value):
        return {modelo}Serializer_Representation(value).data
    
class {modelo}Serializer_Destroy(serializers.ModelSerializer):
    class Meta:
        model = {modelo}
        fields = '__all__'
    def to_representation(self, value):
        return {modelo}Serializer_Representation(value).data
"""

plantilla_views="""

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
           
        - 404 (Not Found):
        - 400 (Bad Request): Los datos de entrada no son válidos
        - 500 (Internal Server Error): Error en el servidor
        {
            'status': 'error'
            'message': "descripción del error"
        }
        
        Paginación:
            Para el paginado, se puede utilizar el parámetro "page" en la URL para especificar la página que se desea mostrar. Por ejemplo, "/entidad?page=2" mostrará la segunda página de productos.
            El primer índice de la lista es ‘page=1’.
            Además para definir el tamaño del paginado se puede utilizar a el parámetro “page_size”. Por ejemplo, "/entidad? page_size=3"
            En la respuesta el parámetro "count" representa la cantidad total de elementos resultantes (no la cantidad de elementos en la lista productos del page_size )
        
        Rangos numéricos y cronológicos:
            "/entidad?nombre=nombreABuscar&atributo__gte=10& atributo__lt=16&ordering=nombre"
            "/entidad?nombre=nombreABuscar&atributo__gte=2024-01-09T20:16:01.825736Z& atributo__lt=2024-01-10T16:02:25.432273Z&ordering=nombre"
            Usar 'gte', 'lte','gt', 'lt'

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

        

        GET:
        Obtiene la entidad de {modelo_labelSingular} con el id proporcionado.

            Ejemplo de salida de solicitud GET:
            {
                {parametros_salida_get_RUD}
            }
            
        - 404 (Not Found):
        - 400 (Bad Request): Los datos de entrada no son válidos
        - 500 (Internal Server Error): Error en el servidor
        {
            'status': 'error'
            'message': "descripción del error"
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
        
        - 404 (Not Found):
        - 400 (Bad Request): Los datos de entrada no son válidos
        - 500 (Internal Server Error): Error en el servidor
        {
            'status': 'error'
            'message': "descripción del error"
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

        - 404 (Not Found):
        - 400 (Bad Request): Los datos de entrada no son válidos
        - 500 (Internal Server Error): Error en el servidor
        {
            'status': 'error'
            'message': "descripción del error"
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

        
        DELETE:
        Elimina la entidad de {modelo_labelSingular} con el id proporcionado.
        
        - 404 (Not Found):
        - 400 (Bad Request): Los datos de entrada no son válidos
        - 500 (Internal Server Error): Error en el servidor
        {
            'status': 'error'
            'message': "descripción del error"
        }
        
    \"\"\"
    {permisos_destroy} 
    serializer_class = {modeloSerializer_destroy}
    {save_destroy}




"""

plantilla_doc = """
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
        
        Paginación:
            Para el paginado, se puede utilizar el parámetro "page" en la URL para especificar la página que se desea mostrar. Por ejemplo, "/entidad?page=2" mostrará la segunda página de productos.
            El primer índice de la lista es ‘page=1’.
            Además para definir el tamaño del paginado se puede utilizar a el parámetro “page_size”. Por ejemplo, "/entidad? page_size=3"
            En la respuesta el parámetro "count" representa la cantidad total de elementos resultantes (no la cantidad de elementos en la lista productos del page_size )
            Si no se incluye el ‘page_size’ se retornaran todos los datos sin paginar 
            
        Rangos numéricos y cronológicos:
            "/entidad?nombre=nombreABuscar&atributo__gte=10& atributo__lt=16&ordering=nombre"
            "/entidad?nombre=nombreABuscar&atributo__gte=2024-01-09T20:16:01.825736Z& atributo__lt=2024-01-10T16:02:25.432273Z&ordering=nombre"
            Usar 'gte', 'lte','gt', 'lt'

        +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


        {modeloLower}/findById/<int:pk>/

        GET:


        {permisos_descripcion_retrieve}

        Endpoint para la obtención de una entidad de {modelo_labelSingular} específica.

        Parámetros de entrada:
        - id: Identificador único de la entidad a obtener, actualizar o eliminar.

        - 404 (Not Found):
        - 400 (Bad Request): Los datos de entrada no son válidos
        - 500 (Internal Server Error): Error en el servidor
        {
            'status': 'error'
            'message': "descripción del error"
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
            - 500 (Internal Server Error): Error en el servidor
            {
                'status': 'error'
                'message': "descripción del error"
            }



        +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


        {modeloLower}/update/<int:pk>/

        PUT o PATCH:
        En el caso PATCH de los campos que no se incluyan no serán modificados,
        Si se incluye una imagen pero su valor es null, entonces sera eliminada

        {permisos_descripcion_update}

        Endpoint para la actualización de una entidad de {modelo_labelSingular} específica.

        Parámetros de entrada:
        - id: Identificador único de la entidad a obtener, actualizar o eliminar.

        - 404 (Not Found):
        - 400 (Bad Request): Los datos de entrada no son válidos
        - 500 (Internal Server Error): Error en el servidor
        {
            'status': 'error'
            'message': "descripción del error"
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

            - 404 (Not Found):
            - 400 (Bad Request): Los datos de entrada no son válidos
            - 500 (Internal Server Error): Error en el servidor
            {
                'status': 'error'
                'message': "descripción del error"
            }



        +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


        {modeloLower}/delete/<int:pk>/

        DELETE:

        {permisos_descripcion_destroy}

        Endpoint para la eliminación de una entidad de {modelo_labelSingular} específica.

        Parámetros de entrada:
        - id: Identificador único de la entidad a obtener, actualizar o eliminar.

        - 404 (Not Found):
        - 400 (Bad Request): Los datos de entrada no son válidos
        - 500 (Internal Server Error): Error en el servidor
        {
            'status': 'error'
            'message': "descripción del error"
        }


        DELETE:
        Elimina la entidad de {modelo_labelSingular} con el id proporcionado.


        +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++



"""


plantilla_viewSets="""

class {modelo}_ViewSet(Base_List):
    
    serializer_class = {modelo}_Serializer
    filter_backends = [DjangoFilterBackend,
                       SearchFilter,
                       OrderingFilter,
                       ]
    {atributosExtra} 
"""

# Ejemplo de solicitud GET:
#        {ejemplo_get_lista}


plantilla_serializer_imagen = """

class {modelo}Serializer(serializers.ModelSerializer):
    class Meta:
        model = {modelo}
        fields = '__all__'
    def to_representation(self, value):
        request=self.context['request']
        return {modelo}RepresentationSerializer(value, context={'request': request}).data

"""

plantilla_viewset_own="""
class {modelo}ViewSet(viewsets.ModelViewSet):
    serializer_class = {modelo}_Serializer
    filter_backends = [DjangoFilterBackend,
                       SearchFilter,
                       OrderingFilter,
                       ]
    {atributosExtra}

    def get_permissions(self):
        \"\"\"
        Instantiates and returns the list of permissions that this
        view requires.
        \"\"\"
        if self.action == "list":
            permission_classes = [
                IsAuthenticated,
                IsTokenValid,
                EmailHasBeenConfirmed,
                IsSuperUserOrIsItTheOwner{modelo},
            ]
        elif self.action == "create":
            permission_classes = [
                IsAuthenticated,
                IsTokenValid,
                EmailHasBeenConfirmed,
            ]
        elif self.action == "update":
            permission_classes = [
                IsAuthenticated,
                IsTokenValid,
                EmailHasBeenConfirmed,
                IsSuperUserOrIsItTheOwnerObj{modelo},
            ]
        elif self.action == "retrieve":
            permission_classes = [
                IsAuthenticated,
                IsTokenValid,
                EmailHasBeenConfirmed,
            ]
        elif self.action == "partial_update":
            permission_classes = [
                IsAuthenticated,
                IsTokenValid,
                EmailHasBeenConfirmed,
                IsSuperUserOrIsItTheOwnerObj{modelo},
            ]
        elif self.action == "destroy":
            permission_classes = [
                IsAuthenticated,
                IsTokenValid,
                EmailHasBeenConfirmed,
                IsSuperUserOrIsItTheOwnerObj{modelo},
            ]
        else:
            permission_classes = []
        return [permission() for permission in permission_classes]

    @extend_schema(
        responses={201: {modelo}RepresentationSerializer},
    )
    def create(self, request, *args, **kwargs):
        \"\"\"
        This method requires the user to be authenticated in order to be
        used. Authentication is done by using a JWT (JSON Web Token)
        that is included in the header of the HTTP request. The JWT includes
        information about the authenticated user, such as their identity
        and the permissions they have been granted.

        The authenticated user must be a superuser or the creator of this
        entity
        \"\"\"
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = request.user
        user_id = serializer.validated_data["user"]
        if not user.is_superuser:
            if str(user_id.id) != str(user.id):
                error = {
                    "user": [
                        "The user ID must be the same as"
                        " the one who is authenticated"
                    ]
                }
                return JsonResponse(
                    {
                        "status": "error",
                        "message": error,
                    },
                    status=400,
                )

        card = self.perform_create(serializer)

        user_own_card = (
            user
            if str(user.id) == str(user_id.id)
            else User.objects.filter(id=user_id.id).first()
        )

        own_card = OwnCard()
        own_card.user = user_own_card
        own_card.card = card
        own_card.save()

        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

    @extend_schema(
        responses={200: {modelo}RepresentationSerializer},
    )
    def list(self, request, *args, **kwargs):
        \"\"\"
        This method requires the user to be authenticated in order to be
        used. Authentication is done by using a JWT (JSON Web Token)
        that is included in the header of the HTTP request. The JWT
        includes information about the authenticated user, such as their
        identity and the permissions they have been granted.

        The authenticated user must be a superuser or the creator of
        these entities

        If you are not a superuser, you must include in the query the
        following 'query parameter' that refers to the ID of the authenticated
        user, in this way only the information corresponding to this user is
        accessed, otherwise access will not be allowed

        user__id = id
        \"\"\"
        return super().list(request, *args, **kwargs)

    @extend_schema(
        responses={200: {modelo}RepresentationSerializer},
    )
    def update(self, request, *args, **kwargs):
        \"\"\"
        This method requires the user to be authenticated in order to be used.
        Authentication is done by using a JWT (JSON Web Token) that is included
        in the header of the HTTP request. The JWT includes information about
        the authenticated user, such as their identity and the permissions they
        have been granted.

        The authenticated user must be a superuser or the creator of this entity
        \"\"\"
        return super().update(request, *args, **kwargs)

    @extend_schema(
        responses={200: {modelo}RepresentationSerializer},
    )
    def retrieve(self, request, *args, **kwargs):
        \"\"\"
        This method requires the user to be authenticated in order to be used.
        Authentication is done by using a JWT (JSON Web Token) that is included
        in the header of the HTTP request. The JWT includes information about
        the authenticated user, such as their identity and the permissions they
        have been granted.

        The authenticated user must be a superuser or the creator of this entity
        \"\"\"
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        responses={200: {modelo}RepresentationSerializer},
    )
    def partial_update(self, request, *args, **kwargs):
        \"\"\"
        This method requires the user to be authenticated in order to be used.
        Authentication is done by using a JWT (JSON Web Token) that is included
        in the header of the HTTP request. The JWT includes information about
        the authenticated user, such as their identity and the permissions they
        have been granted.

        The authenticated user must be a superuser or the creator of this entity
        \"\"\"
        return super().partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        \"\"\"
        This method requires the user to be authenticated in order to be used.
        Authentication is done by using a JWT (JSON Web Token) that is included
        in the header of the HTTP request. The JWT includes information about
        the authenticated user, such as their identity and the permissions they
        have been granted.

        The authenticated user must be a superuser or the creator of this entity
        \"\"\"
        return super().destroy(request, *args, **kwargs)

    def get_queryset(self):
        own_cards = OwnCard.objects.all()
        cards = {modelo}.objects.filter(owncard__in=own_cards)
        return cards

    def perform_create(self, serializer):
        return serializer.save()

"""


plantilla_doc_parametros_list = """
        
        {modelo} ============================================================================================
        
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
        
        Paginación:
            Para el paginado, se puede utilizar el parámetro "page" en la URL para especificar la página que se desea mostrar. Por ejemplo, "/entidad?page=2" mostrará la segunda página de productos.
            El primer índice de la lista es ‘page=1’.
            Además para definir el tamaño del paginado se puede utilizar a el parámetro “page_size”. Por ejemplo, "/entidad? page_size=3"
            En la respuesta el parámetro "count" representa la cantidad total de elementos resultantes (no la cantidad de elementos en la lista productos del page_size )
        
        Rangos numéricos y cronológicos:
            "/entidad?nombre=nombreABuscar&atributo__gte=10& atributo__lt=16&ordering=nombre"
            "/entidad?nombre=nombreABuscar&atributo__gte=2024-01-09T20:16:01.825736Z& atributo__lt=2024-01-10T16:02:25.432273Z&ordering=nombre"
            Usar 'gte', 'lte','gt', 'lt'

        
        


        +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++




"""

plantillas_filtros="""
{modelo} ============================================================================================

    {atributosExtra}

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""

plantilla_views_list_retrieve = """

class {modelo}_List(Base_List):
    \"\"\"
        {permisos_descripcion_list} 

       Endpoint para el listado de {modelo_labelPlurar}.

       GET:
       Obtiene una lista de todas las entidades de {modelo_labelSingular} existentes, opcionalmente filtradas y ordenadas.

        **Parámetros de busqueda:**

    No utilizar junto a los parámetros de filtro

    Parametro Principial:

        "search", busca cualquier coincidencia que incluye el valor pasado en el parametro secundario
        Ejemplo: &search=valor a buscar

    Parametro Secundarios por los que busca:
           
        {paremetros_get_search_lista} 

    **Parámetros de ordenamiento:**

    Parametro Principial:

        "ordering", incluir un "-" delante del parametro secundario si se desea ordenar de forma desendiente
         Ejemplo: &ordering=-parametro secundario

    Parametro Secundarios:
    
        {paremetros_get_ordenamiento_lista} 

    **Paginación:**

    Para el paginado, se puede utilizar el parámetro "page" en la URL para especificar la página que se desea mostrar.

    Por ejemplo, "/entidad?page=2" mostrará la segunda página de productos.

    El primer índice de la lista es ‘page=1’.

    Además para definir el tamaño del paginado se puede utilizar a el parámetro “page_size”.

    Por ejemplo, "/entidad? page_size=3"

    En la respuesta el parámetro "count" representa la cantidad total de elementos resultantes (no la cantidad de elementos en la lista productos del page_size )

    Si no se incluye el ‘page_size’ se retornaran todos los datos sin paginar

    **Rangos numéricos y cronológicos:**

        "/entidad?nombre=nombreABuscar&atributo__gte=10& atributo__lt=16&ordering=nombre"
        "/entidad?nombre=nombreABuscar&atributo__gte=2024-01-09T20:16:01.825736Z& atributo__lt=2024-01-10T16:02:25.432273Z&ordering=nombre"
        Usar 'gte', 'lte','gt', 'lt'
        
    - 500 (Internal Server Error): Error en el servidor
    {
        'status': 'error'
        'message': "descripción del error"
    }

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
    
    GET:
    Obtiene la entidad de {modelo_labelSingular} con el id proporcionado.
    
    - 404 (Not Found):
    - 400 (Bad Request): Los datos de entrada no son válidos
    - 500 (Internal Server Error): Error en el servidor
    {
        'status': 'error'
        'message': "descripción del error"
    }


    \"\"\"
    {permisos_retrieve} 
    serializer_class = {modeloSerializer_retrieve}

"""

plantilla_serializer_list_retrieve = """

class {modelo}Serializer_Representation(serializers.ModelSerializer):
    {parametrosSerializer}
    class Meta:
        model = {modelo}
        fields = '__all__'
    
class {modelo}Serializer_List(serializers.ModelSerializer):
    class Meta:
        model = {modelo}
        fields = '__all__'
    def to_representation(self, value):
        return {modelo}Serializer_Representation(value).data
class {modelo}Serializer_Retrieve(serializers.ModelSerializer):
    class Meta:
        model = {modelo}
        fields = '__all__'
    def to_representation(self, value):
        return {modelo}Serializer_Representation(value).data

"""

plantilla_doc_list_retrieve = """
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

        Paginación:
            Para el paginado, se puede utilizar el parámetro "page" en la URL para especificar la página que se desea mostrar. Por ejemplo, "/entidad?page=2" mostrará la segunda página de productos.
            El primer índice de la lista es ‘page=1’.
            Además para definir el tamaño del paginado se puede utilizar a el parámetro “page_size”. Por ejemplo, "/entidad? page_size=3"
            En la respuesta el parámetro "count" representa la cantidad total de elementos resultantes (no la cantidad de elementos en la lista productos del page_size )

        Rangos numéricos y cronológicos:
            "/entidad?nombre=nombreABuscar&atributo__gte=10& atributo__lt=16&ordering=nombre"
            "/entidad?nombre=nombreABuscar&atributo__gte=2024-01-09T20:16:01.825736Z& atributo__lt=2024-01-10T16:02:25.432273Z&ordering=nombre"
            Usar 'gte', 'lte','gt', 'lt'

        +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


        {modeloLower}/findById/<int:pk>/

        GET:


        {permisos_descripcion_retrieve}

        Endpoint para la obtención de una entidad de {modelo_labelSingular} específica.

        Parámetros de entrada:
        - id: Identificador único de la entidad a obtener, actualizar o eliminar.

        - 404 (Not Found):
        - 400 (Bad Request): Los datos de entrada no son válidos
        - 500 (Internal Server Error): Error en el servidor
        {
            'status': 'error'
            'message': "descripción del error"
        }


        Obtiene la entidad de {modelo_labelSingular} con el id proporcionado.

            Ejemplo de salida de solicitud GET:
            {
                {parametros_salida_get_RUD}
            }



        ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++




"""

plantilla_resennas_serializable="""
class {modelo}RepresentationSerializer(serializers.ModelSerializer):
    {parametrosSerializer}
    class Meta:
        model = {modelo}
        fields = '__all__'
class {modelo}Serializer(serializers.ModelSerializer):
    class Meta:
        model = {modelo}
        fields = '__all__'
    def to_representation(self, instance):
        request = get_current_request()
        return {modelo}RepresentationSerializer(instance, context={'request': request}).data
    
class {modelo}UpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = {modelo}
        fields = ('texto','puntuacion',)
    def to_representation(self, instance):
        request = get_current_request()
        return {modelo}RepresentationSerializer(instance, context={'request': request}).data
"""

plantilla_views_serializer_update = """

class {modelo}_List(Base_List):
    \"\"\"
        {permisos_descripcion_list} 

       Endpoint para el listado de {modelo_labelPlurar}.

       GET:
       Obtiene una lista de todas las entidades de {modelo_labelSingular} existentes, opcionalmente filtradas y ordenadas.

        
        Paginación:
            Para el paginado, se puede utilizar el parámetro "page" en la URL para especificar la página que se desea mostrar. Por ejemplo, "/entidad?page=2" mostrará la segunda página de productos.
            El primer índice de la lista es ‘page=1’.
            Además para definir el tamaño del paginado se puede utilizar a el parámetro “page_size”. Por ejemplo, "/entidad? page_size=3"
            En la respuesta el parámetro "count" representa la cantidad total de elementos resultantes (no la cantidad de elementos en la lista productos del page_size )

        Rangos numéricos y cronológicos:
            "/entidad?nombre=nombreABuscar&atributo__gte=10& atributo__lt=16&ordering=nombre"
            "/entidad?nombre=nombreABuscar&atributo__gte=2024-01-09T20:16:01.825736Z& atributo__lt=2024-01-10T16:02:25.432273Z&ordering=nombre"
            Usar 'gte', 'lte','gt', 'lt'

    \"\"\"
    {permisos_list} 
    serializer_class = {modelo}RepresentationSerializer
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



        GET:
        Obtiene la entidad de {modelo_labelSingular} con el id proporcionado.

            


    \"\"\"
    {permisos_retrieve} 
    serializer_class = {modelo}RepresentationSerializer

class {modelo}_Create(Base_Create):
    \"\"\"
        {permisos_descripcion_create}

       Endpoint para la creación de {modelo_labelSingular}.

       POST:
       Crea una nueva entidad de {modelo_labelSingular} con los datos proporcionados en el cuerpo de la solicitud.
       


    \"\"\"
    {permisos_create} 
    serializer_class = {modelo}Serializer

    {save_create}
    @extend_schema(
        responses={201: {modelo}RepresentationSerializer},
    )
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class {modelo}_Update(Base_Update):
    \"\"\"
        {permisos_descripcion_update}

        Endpoint para la actualización de una entidad de {modelo_labelSingular} específica.

        Parámetros de entrada:
        - id: Identificador único de la entidad a obtener, actualizar o eliminar.

        Actualiza la entidad de {modelo_labelSingular} con el id proporcionado con los datos proporcionados en el cuerpo de la solicitud.

        
    \"\"\"

    serializer_class = {modelo}UpdateSerializer
    {permisos_update} 
    {save_update}
    @extend_schema(
        responses={200: {modelo}RepresentationSerializer},
    )
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    @extend_schema(
        responses={200: {modelo}RepresentationSerializer},
    )
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

class {modelo}_Destroy(Base_Destroy):
    \"\"\"
        {permisos_descripcion_destroy}

        Endpoint para la eliminación de una entidad de {modelo_labelSingular} específica.

        Parámetros de entrada:
        - id: Identificador único de la entidad a obtener, actualizar o eliminar.


        DELETE:
        Elimina la entidad de {modelo_labelSingular} con el id proporcionado.

        
    \"\"\"
    {permisos_destroy} 
    serializer_class = {modelo}Serializer
    {save_destroy}




"""

plantilla_views_serializer_update_resennas = """

class {modelo}_List(Base_List):
    \"\"\"
        {permisos_descripcion_list} 

       Endpoint para el listado de {modelo_labelPlurar}.

       GET:
       Obtiene una lista de todas las entidades de {modelo_labelSingular} existentes, opcionalmente filtradas y ordenadas.


        Paginación:
            Para el paginado, se puede utilizar el parámetro "page" en la URL para especificar la página que se desea mostrar. Por ejemplo, "/entidad?page=2" mostrará la segunda página de productos.
            El primer índice de la lista es ‘page=1’.
            Además para definir el tamaño del paginado se puede utilizar a el parámetro “page_size”. Por ejemplo, "/entidad? page_size=3"
            En la respuesta el parámetro "count" representa la cantidad total de elementos resultantes (no la cantidad de elementos en la lista productos del page_size )

        Rangos numéricos y cronológicos:
            "/entidad?nombre=nombreABuscar&atributo__gte=10& atributo__lt=16&ordering=nombre"
            "/entidad?nombre=nombreABuscar&atributo__gte=2024-01-09T20:16:01.825736Z& atributo__lt=2024-01-10T16:02:25.432273Z&ordering=nombre"
            Usar 'gte', 'lte','gt', 'lt'

    \"\"\"
    {permisos_list} 
    serializer_class = {modelo}RepresentationSerializer
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



        GET:
        Obtiene la entidad de {modelo_labelSingular} con el id proporcionado.




    \"\"\"
    {permisos_retrieve} 
    serializer_class = {modelo}RepresentationSerializer

class {modelo}_Create(Base_Create):
    \"\"\"
        {permisos_descripcion_create}

       Endpoint para la creación de {modelo_labelSingular}.

       POST:
       Crea una nueva entidad de {modelo_labelSingular} con los datos proporcionados en el cuerpo de la solicitud.



    \"\"\"
    permission_classes = (IsAuthenticated, IsItTheOwner,)
    serializer_class = {modelo}Serializer

    {save_create}
    @extend_schema(
        responses={201: {modelo}RepresentationSerializer},
    )
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class {modelo}_Update(Base_Update):
    \"\"\"
        {permisos_descripcion_update}

        Endpoint para la actualización de una entidad de {modelo_labelSingular} específica.

        Parámetros de entrada:
        - id: Identificador único de la entidad a obtener, actualizar o eliminar.

        Actualiza la entidad de {modelo_labelSingular} con el id proporcionado con los datos proporcionados en el cuerpo de la solicitud.


    \"\"\"

    serializer_class = {modelo}UpdateSerializer
    permission_classes = (IsAuthenticated, IsItTheOwnerObj,)
    {save_update}
    @extend_schema(
        responses={200: {modelo}RepresentationSerializer},
    )
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    @extend_schema(
        responses={200: {modelo}RepresentationSerializer},
    )
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

class {modelo}_Destroy(Base_Destroy):
    \"\"\"
        {permisos_descripcion_destroy}

        Endpoint para la eliminación de una entidad de {modelo_labelSingular} específica.

        Parámetros de entrada:
        - id: Identificador único de la entidad a obtener, actualizar o eliminar.


        DELETE:
        Elimina la entidad de {modelo_labelSingular} con el id proporcionado.


    \"\"\"
    permission_classes = (IsAuthenticated, IsItTheOwnerObj,)
    serializer_class = {modelo}Serializer
    {save_destroy}




"""


plantilla_serializer_Representation = """

class {modelo}Serializer_Representation(serializers.ModelSerializer):
    {parametrosSerializer}
    class Meta:
        model = {modelo}
        fields = '__all__'

"""
