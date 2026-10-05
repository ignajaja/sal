from django.urls import path
from . import views

urlpatterns = [
    path('', views.hub, name='hub'),
    path('mensaje/', views.vista_mensaje, name='mensaje_del_dia'),
    path('notificacion/', views.vista_notificacion, name='notificacion_directa'),
    path('galeria/', views.vista_galeria, name='galeria'),
]