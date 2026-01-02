from django.urls import path
from . import views 

# importando a unção url e todas as nossas views do aplicativo blog

urlpatterns = [
    path('', views.post_list, name = 'post_list'),
]

# atreibuição de view (chamada 'post_list'), tendo uma sequência de caracteres vazia, ignorando o nome do arquivo
# que antecede o caminho compelto da url, post_list é o nome usado para identificar a view