from rest_framework.serializers import ModelSerializer
from .models import Table, Category, Menu, Waiter, Reception, Order

class TableSerializer(ModelSerializer):
    class Meta:
        model = Table
        fields = '__all__'

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class MenuSerializer(ModelSerializer):
    class Meta:
        model = Menu
        fields ='__all__'

class WaiterSerializer(ModelSerializer):
    class Meta:
        model = Waiter
        fields = '__all__'

class ReceptionSerializer(ModelSerializer):
    class Meta:
        model = Reception
        fields = '__all__'

class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'