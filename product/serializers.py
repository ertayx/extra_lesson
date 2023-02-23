from rest_framework import serializers
# from rest_framework.serializers import ModelSerializer

from .models import Product
# пишем сериалайзер для нашей модельки 
# сериалайзер - переводчик
class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product # указываем с какой моделькой наш сериалайзер работал
        fields = '__all__' # указываем с какими полями наш сериалайзер работал
        # fields = ['title', 'size', 'price']
        # exclude = ['title'] # это исключение

    def to_representation(self, instance):
        # этот метод отвечает за отображение нащей информации
        ret = super().to_representation(instance)
        ret['title'] = 'ertay'
        return ret
