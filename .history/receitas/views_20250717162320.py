from django.shortcuts import render
from django.http import HttpResponse
from .models import Receita

# Create your views here.
def index(request):
    receitas = 

    dados = {
        'nome_das_receitas': receitas
    }
    return render(request,'index.html',dados)

def receita(request):
    return render(request,'receita.html')