from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from .models import Table, Category, Menu, Waiter, Reception, Order
from .serializers import TableSerializer, CategorySerializer, MenuSerializer, WaiterSerializer, ReceptionSerializer, OrderSerializer
from rest_framework.response import Response

# Create your views here.
class TableView(GenericAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer

    def get(self,request):
        table_objs = self.get_queryset()
        serializer = self.serializer_class(table_objs, many=True)
        return Response (serializer.data)


    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('Data created!')
        else:
            return Response(serializer.errors)
        
class Table_UD_view(GenericAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer

    def get(self,request,pk):
        try:
            table_obj = Table.objects.get(id=pk)
        except:
            return Response('Data not found!')
        serializer = self.serializer_class(table_obj)
        return Response(serializer.data)
    
    def put(self,request,pk):
        try:
            table_obj = Table.objects.get(id=pk)
        except:
            return Response('Data not found!')
        serializer = self.serializer_class(table_obj,data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response('Data updated!')
        else:
            return Response(serializer.errors)
    
    def delete(self,request,pk):
        try:
            table_obj = Table.objects.get(id=pk)
        except:
            return Response('Data not found!')
        table_obj.delete()
        return Response('Data deleted!')

class CategoryView(GenericAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get(self,request):
        category_objs = self.get_queryset()
        serializer = self.serializer_class(category_objs, many=True)
        return Response (serializer.data)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('Data created!')
        else:
            return Response(serializer.errors)
        
class Category_UD_view(GenericAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get(self,request,pk):
        try:
            category_obj = Category.objects.get(id=pk)
        except:
            return Response('Data not found!')
        serializer = self.serializer_class(category_obj)
        return Response(serializer.data)
    
    def put(self,request,pk):
        try:
            category_obj = Category.objects.get(id=pk)
        except:
            return Response('Data not found!')
        serializer = self.serializer_class(category_obj,data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response('Data updated!')
        else:
            return Response(serializer.errors)
    
    def delete(self,request,pk):
        try:
            category_obj = Category.objects.get(id=pk)
        except:
            return Response('Data not found!')
        category_obj.delete()
        return Response('Data deleted!')
    

class MenuView(GenericAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    def get(self,request):
        menu_objs = self.get_queryset()
        serializer = self.serializer_class(menu_objs, many=True)
        return Response (serializer.data)


    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('Data created!')
        else:
            return Response(serializer.errors)
        
class Menu_UD_view(GenericAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    def get(self,request,pk):
        try:
            menu_obj = Menu.objects.get(id=pk)
        except:
            return Response('Data not found!')
        serializer = self.serializer_class(menu_obj)
        return Response(serializer.data)
    
    def put(self,request,pk):
        try:
            menu_obj = Menu.objects.get(id=pk)
        except:
            return Response('Data not found!')
        serializer = self.serializer_class(menu_obj,data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response('Data updated!')
        else:
            return Response(serializer.errors)
    
    def delete(self,request,pk):
        try:
            menu_obj = Menu.objects.get(id=pk)
        except:
            return Response('Data not found!')
        menu_obj.delete()
        return Response('Data deleted!')

        

class WaiterView(GenericAPIView):
    queryset = Waiter.objects.all()
    serializer_class = WaiterSerializer

    def get(self,request):
        waiter_objs = self.get_queryset()
        serializer = self.serializer_class(waiter_objs, many=True)
        return Response (serializer.data)


    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('Data created!')
        else:
            return Response(serializer.errors)
        
class Waiter_UD_view(GenericAPIView):
    queryset = Waiter.objects.all()
    serializer_class = WaiterSerializer

    def get(self,request,pk):
        try:
            waiter_obj = Waiter.objects.get(id=pk)
        except:
            return Response('Data not found!')
        serializer = self.serializer_class(waiter_obj)
        return Response(serializer.data)
    
    def put(self,request,pk):
        try:
            waiter_obj = Waiter.objects.get(id=pk)
        except:
            return Response('Data not found!')
        serializer = self.serializer_class(waiter_obj,data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response('Data updated!')
        else:
            return Response(serializer.errors)
    
    def delete(self,request,pk):
        try:
            waiter_obj = Waiter.objects.get(id=pk)
        except:
            return Response('Data not found!')
        waiter_obj.delete()
        return Response('Data deleted!')

        

class ReceptionView(GenericAPIView):
    queryset = Reception.objects.all()
    serializer_class = ReceptionSerializer

    def get(self,request):
        reception_objs = self.get_queryset()
        serializer = self.serializer_class(reception_objs, many=True)
        return Response (serializer.data)


    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('Data created!')
        else:
            return Response(serializer.errors)
        
class Reception_UD_view(GenericAPIView):
    queryset = Reception.objects.all()
    serializer_class = ReceptionSerializer

    def get(self,request,pk):
        try:
            reception_obj = Reception.objects.get(id=pk)
        except:
            return Response('Data not found!')
        serializer = self.serializer_class(reception_obj)
        return Response(serializer.data)
    
    def put(self,request,pk):
        try:
            reception_obj = Reception.objects.get(id=pk)
        except:
            return Response('Data not found!')
        serializer = self.serializer_class(reception_obj,data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response('Data updated!')
        else:
            return Response(serializer.errors)
    
    def delete(self,request,pk):
        try:
            reception_obj = Reception.objects.get(id=pk)
        except:
            return Response('Data not found!')
        reception_obj.delete()
        return Response('Data deleted!')

        

class OrderView(GenericAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get(self,request):
        order_objs = self.get_queryset()
        serializer = self.serializer_class(order_objs, many=True)
        return Response (serializer.data)


    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('Data created!')
        else:
            return Response(serializer.errors)
        
class Order_UD_View(GenericAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get(self,request,pk):
        try:
            order_obj = Order.objects.get(id=pk)
        except:
            return Response('Data not found!')
        serializer = self.serializer_class(order_obj)
        return Response(serializer.data)
    
    def put(self,request,pk):
        try:
            order_obj = Order.objects.get(id=pk)
        except:
            return Response('Data not found!')
        serializer = self.serializer_class(order_obj,data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response('Data updated!')
        else:
            return Response(serializer.errors)
    
    def delete(self,request,pk):
        try:
            order_obj = Order.objects.get(id=pk)
        except:
            return Response('Data not found!')
        order_obj.delete()
        return Response('Data deleted!')
