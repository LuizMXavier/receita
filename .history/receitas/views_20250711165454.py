from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    receitas = {
        
    }
    return render(request,'index.html')

def receita(request):
    return render(request,'receita.html')