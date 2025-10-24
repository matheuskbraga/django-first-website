from django.shortcuts import render
from .dados import projetos

# Create your views here.
def home(request): # 1° coisa criar a view
    return render(request, 'home.html') # 2° coisa renderizar o template

def projetos_view(request):
    return render(request, 'projetos.html', {'projetos': projetos})

def detalhes_projeto(request, id_projeto):
    projeto = projetos.get(id_projeto)
    return render(request, 'detalhes_projeto.html', {'projeto': projeto})