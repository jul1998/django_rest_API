
from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status

from products.models import Product
from products.serializers import ProductSerializer
# Create your views here.


@api_view(['POST'])
def home(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        data = serializer.data
        return Response(data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
