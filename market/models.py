from django.db import models


# Create your models here.
class Customers(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    address = models.CharField(max_length=120)
    phone = models.CharField(max_length=15)
    sign_up_date = models.DateField()

    def __str__(self):
        return self.name


class Goods(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField(max_length=250)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    total_quantity = models.DecimalField(decimal_places=2, max_digits=15)
    add_date = models.DateField()


class Orders(models.Model):
    user = models.ForeignKey(Customers, on_delete=models.CASCADE)
    goods = models.ManyToManyField(Goods)
    total_price = models.DecimalField(decimal_places=2, max_digits=12)
    add_date = models.DateField()
