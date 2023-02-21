from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework import mixins
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser
from rest_framework import permissions
from .models import Product
from .serializers import ProductSerializer

class ProductCreateAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = [permissions.IsAdminUser, ]

class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDeleteAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductModelViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# class ProductCreateMixin(mixins.CreateModelMixin):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

# @api_view(['POST'])
# def creat_product(request):
#     title = request.data.get('title')
#     price = request.data.get('price')
#     description = request.data.get('description')

#     Product.objects.create(title=title, price=price, description=description)
