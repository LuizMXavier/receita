from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    receitas = {
        1:'Lasanha',
        2:''
    }
    return render(request,'index.html')

def receita(request):
    return render(request,'receita.html')