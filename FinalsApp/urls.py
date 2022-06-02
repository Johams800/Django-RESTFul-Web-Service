"""FinalsProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include


from rest_framework.routers import DefaultRouter
from .views import AddCustomerViewSet, GetCustomerViewSet, UpdateCustomerViewSet, \
    AddAddressViewSet, GetAddressViewSet, UpdateAddressViewSet, AddOrderViewSet, \
    UpdateOrderViewSet, GetOrderViewSet, AddProductViewSet, GetProductsViewSet

router = DefaultRouter()
# Routers
router.register(r'add_customer', AddCustomerViewSet, "add_customer")
router.register(r'get_customers', GetCustomerViewSet, "get_customers")
router.register(r'update_customer', UpdateCustomerViewSet, "update_customer")
router.register(r'add_address', AddAddressViewSet, "add_address")
router.register(r'get_address', GetAddressViewSet, "get_address")
router.register(r'update_address', UpdateAddressViewSet, "update_address")
router.register(r'add_order', AddOrderViewSet, "add_order")
router.register(r'get_order', GetOrderViewSet, "get_order")
router.register(r'update_order', UpdateOrderViewSet, "update_order")
router.register(r'add_product', AddProductViewSet, "add_product")
router.register(r'get_products', GetProductsViewSet, "get_products")

urlpatterns = [

]
urlpatterns += router.urls

