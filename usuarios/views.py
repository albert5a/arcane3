from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.contrib import messages, auth
from django.contrib.auth import authenticate
from usuarios.models import Cliente

def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        if senha != confirmar_senha:
            messages.add_message(request, constants.ERROR, 'Senha e confirmar senha não são iguais.')
            return redirect('cadastro')
        
        if len(senha) < 8:
            messages.add_message(request, constants.ERROR, 'Senha deve ter pelo menos 8 caracteres.')
            return redirect('cadastro')

        users = User.objects.filter(username=username)
        if users.exists():
            messages.add_message(request, constants.ERROR, 'Usuário já cadastrado.')
            return redirect('cadastro')

        User.objects.create_user(username=username, password=senha)
        messages.add_message(request, constants.SUCCESS, 'Usuário cadastrado com sucesso!')
        return redirect('login')

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = authenticate(username=username, password=senha)
        if user is not None:
            auth.login(request, user)
            return redirect('clientes')
        else:
            messages.add_message(request, constants.ERROR, 'Usuário ou senha inválidos.')
            return redirect('login')

def clientes(request):
    if request.method == 'GET':
        clientes = Cliente.objects.filter(user=request.user)
        return render(request, 'clientes.html', {'clientes': clientes})
    elif request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        tipo = request.POST.get('tipo')
        status = request.POST.get('status') == 'on'
        
        Cliente.objects.create(
            nome=nome,
            email=email,
            tipo=tipo,
            status=status,
            user=request.user
        )
        
        messages.add_message(request, constants.SUCCESS, 'Cliente cadastrado com sucesso!')
        return redirect('clientes')