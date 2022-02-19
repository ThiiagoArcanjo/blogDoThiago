from unicodedata import name
from django.urls import path
from . import views 

urlpatterns = [
    path('', views.lista_post, name='lista_post'),
    path('post/<int:pk>/', views.post_detalhes, name='post_detalhes'),
    path('post/novo/', views.novo_post, name='novo_post'),
    path('post/<int:pk>/edite/', views.post_edite, name='post_edite'),
    path('post/<int:pk>/excluir/', views.excluir_post, name='excluir_post'),
    path('post/<int:pk>/confirmar_exclusao/', views.confirmar_exclusao, name='confirmar_exclusao'),
    path('hi/', views.hi, name="hi"),
]