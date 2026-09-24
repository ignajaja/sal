from django.urls import path
from . import views

urlpatterns = [
    path('', views.vista_mensaje, name='mensaje_del_dia'),
]