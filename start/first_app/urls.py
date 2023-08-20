from django.contrib import admin
from django.urls import path,include
from . import views
app_name="first_app"
urlpatterns=[
path('home',views.index,name="front_page"),
path('contact',views.contact,name="contact_us"),
path('about',views.about,name="about_us"),
path('table',views.table,name="record_table"),
path('search',views.search,name="search"),
path('productview',views.productview,name="productview"),
path('checkout',views.checkout,name="checkout"),

]