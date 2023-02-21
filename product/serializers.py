from rest_framework import serializers
# from rest_framework.serializers import ModelSerializer

from .models import Product

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'
        # fields = ['title', 'size', 'price']
        # exclude = ['title']

    # def to_representation(self, instance):
    #     ret = super().to_representation(instance)
    #     ret['title'] = 'ertay'
    #     return ret

# QueryDict[{'title':'Ertay'}]