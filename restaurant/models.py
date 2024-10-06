from django.db import models

# Create your models here.
class Table(models.Model):
    table_number = models.IntegerField(unique=True)
    capacity = models.IntegerField()

class Category(models.Model):
    name = models.CharField(max_length=100)

class Menu(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Waiter(models.Model):
    name = models.CharField(max_length=100)
    phone = models.BigIntegerField()

class Reception(models.Model):
    name = models.CharField(max_length=100)
    phone = models.BigIntegerField()

class Order(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    menu_items = models.ManyToManyField(Menu)
    waiter = models.ForeignKey(Waiter, on_delete=models.SET_NULL, null=True)
