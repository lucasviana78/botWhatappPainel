from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def login(request):

    if request.method != 'POST':
        return render(request, 'accounts/login.html')

    user = auth.authenticate(request,
                             username=request.POST.get('usuario'),
                             password=request.POST.get('senha')
                             )
    
    if not user:
        messages.error(request, "Usuário ou senha inválido!")
        return render(request, 'accounts/login.html')
    else:
        auth.login(request, user)
        return redirect('indexSystem')


def logout(request):
    auth.logout(request)
    return redirect('login')


@login_required(redirect_field_name='login')
def indexSystem(request):
    return render(request, 'accounts/index.html')