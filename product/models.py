from django.db import models

from account.models import User


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(models.Model):
    name = models.CharField(unique=True, max_length=32)
    parent_category = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, default=None)

    class Meta:
        managed = True
        db_table = 'category'


class Product(TimestampedModel):
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=64)
    price = models.PositiveIntegerField()
    description = models.CharField(max_length=256)

    class Meta:
        managed = True
        db_table = 'product'

    def __str__(self):
        return self.name


class Purchase(TimestampedModel):
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'purchase'
