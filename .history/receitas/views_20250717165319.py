from django.shortcuts import render
from django.http import HttpResponse
from .models import Receita

# Create your views here.
def index(request):
    receitas = Receita.objects.all()

    dados = {
        'receitas': receitas
    }
    return render(request,'index.html',dados)

def receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)
    return render(request,'receita.html')