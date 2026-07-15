from django.shortcuts import render
from django.http import HttpResponse

def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        # Aqui você pode adicionar a lógica para salvar os dados do usuário no banco de dados
        return HttpResponse(f'Usuário {username} cadastrado com sucesso!')