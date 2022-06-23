from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


# Create your models here.
class Item(models.Model):
    type = models.CharField( verbose_name='Type', max_length=64)
    name = models.CharField(verbose_name='Name', max_length=64)
    id = models.CharField(verbose_name='ID', primary_key=True, db_index=True, unique=True, max_length=64)
    parentId = models.CharField(verbose_name='ParentID', max_length=64)
    price = models.fields.PositiveIntegerField(verbose_name='Price')
    date = models.fields.DateField(verbose_name='Date')
    children = models.CharField(verbose_name='Children', max_length=64)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
