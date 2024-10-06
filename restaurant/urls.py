from django.urls import path
from .views import *

urlpatterns = [
    path('table/',TableView.as_view()),
    path('table/<int:pk>/',Table_UD_view.as_view()),
    path('category/',CategoryView.as_view()),
    path('category/<int:pk>/',Category_UD_view.as_view()),
    path('menu/',MenuView.as_view()),
    path('menu/<int:pk>/',Menu_UD_view.as_view()),
    path('waiter/',WaiterView.as_view()),
    path('waiter/<int:pk>/',Waiter_UD_view.as_view()),
    path('reception/',ReceptionView.as_view()),
    path('reception/<int:pk>/',Reception_UD_view.as_view()),
    path('order/',OrderView.as_view()),
    path('order/<int:pk>/',Order_UD_View.as_view()),
]