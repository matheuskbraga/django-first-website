from django.urls import path
from . import views # 5° coisa importar a view


urlpatterns = [
    # 4° coisa criar a url
    path('', views.home, name='home'),
    path('lista_projetos/', views.projetos_view, name='lista_projetos'),
    path('projeto/<str:id_projeto>/', views.detalhes_projeto, name='detalhes_projeto'),  # Detalhes do projeto
]