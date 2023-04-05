from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import Product
from .serializers import ProductSerializer

class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

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
     




