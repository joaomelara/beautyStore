from django.shortcuts import render
from .models import Produto

# Create your views here.

def home(request):
    return render(request,'produtos/home.html')

def produtos(request):
    novo_produto = Produto()
    novo_produto.descricao = request.POST.get('descricao')
    novo_produto.marca = request.POST.get('marca')
    novo_produto.valor = request.POST.get('valor')
    novo_produto.estoque = request.POST.get('estoque')

    novo_produto.save()

    produtos ={
        'produtos':Produto.objects.all()
    }

    return render(request,'produtos/produtos.html',produtos)