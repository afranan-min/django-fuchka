from django.urls import path

from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('cart/', views.product_page, name='product_page'),
    path('add-to-cart/', views.add_to_cart, name='add_to_cart'),
    path('order-message/', views.order_whatsapp, name='order_whatsapp'),
    path('remove-cart-item/<int:item_id>/', views.remove_cart_item, name='remove_cart_item'),
]
