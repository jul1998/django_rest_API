from rest_framework import generics, mixins, permissions, authentication
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import Product
from .serializers import ProductSerializer

class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.DjangoModelPermissions]

    def perform_create(self, serialzier):
        #serialzier.save()
        print(serialzier.validated_data)
        title = serialzier.validated_data.get('title')
        price = serialzier.validated_data.get('price')
        description = serialzier.validated_data.get('description')
        
        if description is None:
            description = 'No Description'
        serialzier.save(description=description)

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_update(self, serialzier):
        instance = serialzier.save() 
        if not instance.description:
            instance.description = 'No Description'
            

class ProductDeleteAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        instance.delete()

#---------------------Alternative---------------------

class ProductMixinView(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs,):
        print(args, kwargs)
        pk = kwargs.get('pk')
        if pk:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)    
    
    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
#---------------------Alternative---------------------

@api_view(['GET', 'POST'])
def product_alt_view(request, pk=None):
    method = request.method

    if method == 'GET':
        if pk is not None:
            qs = Product.objects.filter(pk=pk)
            if qs.exists():
                data = ProductSerializer(qs.first()).data
                return Response(data)
            else:
                return Response({'Error': "No product"}, status=404)
        else:
            qs = Product.objects.all()
            data = ProductSerializer(qs, many=True).data
            return Response(data)
    else:
        data = request.data
        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)
     




