from django.urls import path
from . import views

urlpatterns= [
    path('', views.home, name='url_home'),
    path('populate/', views.populate, name='url_populate'),
    path('details/', views.details, name='url_details'),
]