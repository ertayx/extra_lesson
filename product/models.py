from django.db import models
from django.contrib.auth import get_user_model
# from account.models import CustomUser

User = get_user_model()

# Create your models here.

# создаем модельку продукта что бы в базе данных появилась таблица
class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)
    date_of_end = models.DateField()
    description = models.TextField()
    # size = models.IntegerField()
    owner = models.ForeignKey(User, related_name='product_user', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.title}'
