from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(redirect_field_name='login')
def painelPedidos(request):
    return render(request, 'pedidos/PainelPedidos.html')


@login_required(redirect_field_name='login')
def painelCozinha(request):
    return render(request, 'pedidos/painelCozinha.html')


