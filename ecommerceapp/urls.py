from django.urls import path
from ecommerceapp import views

urlpatterns = [
    path('',views.index, name="index"),
    path('contact/',views.contact, name="contact"),
    path('about',views.about, name="about"),
    path('checkout/', views.checkout, name='checkout'),
    path('order_confirmation/', views.order_confirmation, name="order_confirmation"),
    path('profile/', views.profile, name="profile"),
    
    

    
]