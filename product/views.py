from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework import mixins
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser
from rest_framework import permissions
from .models import Product
from .serializers import ProductSerializer

class ProductCreateAPIView(generics.CreateAPIView):
    queryset = Product.objects.all() # указываем с каким набором данных наш клиент работал
    serializer_class = ProductSerializer # указываем с каким сералайзером(полями) наш клиент работал
    # permission_classes = [permissions.IsAdminUser, ] # это встроенный пермишн, только АДМИН может создать продукт

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
# до этой строчки мы пишем CRUD на generics

class ProductModelViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# до этой строчки мы написали CRUD на 3 строчки 





# class ProductCreateMixin(mixins.CreateModelMixin):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

# @api_view(['POST'])
# def creat_product(request):
#     title = request.data.get('title')
#     price = request.data.get('price')
#     description = request.data.get('description')

#     Product.objects.create(title=title, price=price, description=description)
