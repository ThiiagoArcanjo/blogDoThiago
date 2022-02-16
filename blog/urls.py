from django.urls import path
from . import views 

urlpatterns = [
    path('', views.lista_post, name='lista_post'),
    path('post/<int:pk>/', views.post_detalhes, name='post_detalhes'),
    path('post/novo/', views.novo_post, name='novo_post'),
]