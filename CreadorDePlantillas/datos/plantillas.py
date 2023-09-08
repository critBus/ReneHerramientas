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
class {modelo}_ListCreate(generics.ListCreateAPIView):
    serializer_class = {modelo}Serializer
    filter_backends = [DjangoFilterBackend,
                       SearchFilter,
                       OrderingFilter,
                       ]
    {atributosExtra}
    def get_queryset(self):
        return self.serializer_class.Meta.model.objects.all()

class {modelo}_RUD(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = {modelo}Serializer
"""

e="""
    path('{modeloLower}/', {modelo}_ListCreate.as_view(), name='{modeloLower}-list'),
    path('{modeloLower}/<int:pk>/', {modelo}_RUD.as_view(), name='{modeloLower}-detail'),
"""