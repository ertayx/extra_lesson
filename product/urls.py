from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter
# в этом файлике мы пишем наши адреса для манипуляции с нашим продуктом
router = DefaultRouter()
router.register('', ProductModelViewSet)

# роутеры нужны нам что бы мы могли распаковать на вьюсет(CRUD на 3 строчки)
# начиная с 13 по 17 мы сами указывали пути а роутеры делают это все за нас

urlpatterns = [
    # наяиная с этой строчки
    path('create/', ProductCreateAPIView.as_view()),
    path('read/', ProductListAPIView.as_view()),
    path('read/<int:pk>/', ProductDetailAPIView.as_view()),
    path('update/<int:pk>/', ProductUpdateAPIView.as_view()),
    path('delete/<int:pk>/', ProductDeleteAPIView.as_view()),
    # до этой мы пишем адреса для каждого действия

    path('', include(router.urls)) # перенапровление запроса на роутеры
]