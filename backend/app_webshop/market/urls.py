from django.urls import path, include
from .views.auth import AuthView, hello
from .views.product import ProductListView

urlpatterns = [
    path('product_list', ProductListView.as_view()),
    path('userlogin', AuthView.as_view()),
    path('hello', hello),
]