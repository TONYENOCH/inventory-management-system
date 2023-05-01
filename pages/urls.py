from django.urls import path
from .views import (
    ItemsListView, 
    ItemsDetailView, 
    SearchListView, 
    ItemSellView,
    TransactionsView,
    ItemCreateView
)

app_name = 'pages'

urlpatterns = [
    path('',ItemsListView.as_view(), name='itemsList'),
    path('detail/<int:pk>/',ItemsDetailView.as_view(), name='itemsDetail'),
    path('search/',SearchListView.as_view(), name='itemsSearch'),
    path('sell/<int:pk>/',ItemSellView.as_view(), name='itemSell'),
    path('transactions/',TransactionsView.as_view(), name='transactions'),
    path('create/',ItemCreateView.as_view(), name='itemCreate'),
]


