from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('',views.walls_detail(), name='walls_detail'),
]