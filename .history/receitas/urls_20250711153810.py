from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('receita', views.index, name='receita'),
]
