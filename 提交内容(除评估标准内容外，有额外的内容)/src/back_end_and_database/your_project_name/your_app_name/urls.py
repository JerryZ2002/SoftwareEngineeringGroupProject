# urls.py
from rest_framework.routers import DefaultRouter

from django.urls import path
from .views import get_products
from .views import add_product
from .views import delete_product
from .views import update_product

from .views import PurchaseOrderViewSet, SalesOrderViewSet, InventoryViewSet, ProductInfoViewSet

from .views import ProductInfoAPI

from django.urls import path, include

router = DefaultRouter()
router.register(r'purchase-orders', PurchaseOrderViewSet, basename='purchase-order')
router.register(r'sales-orders', SalesOrderViewSet, basename='sales-order')
router.register(r'inventories', InventoryViewSet, basename='inventory')
router.register(r'product-info', ProductInfoViewSet, basename='product-info')

urlpatterns = [
    path('api/products/', get_products, name='get_products'),
    path('api/products/add', add_product, name='add_product'),
    path('api/products/<int:product_id>/', delete_product, name='delete_product'),
    path('api/products/<int:product_id>/update/', update_product, name='update_product'),
    path('api/', include(router.urls)),
    path('api/ProductInfo/',ProductInfoAPI.as_view(),name='ProductInfoAPI')
]
