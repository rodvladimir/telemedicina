from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.contrib.messages import get_messages

# Create your views here.
def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get("email")
        senha = request.POST.get("senha")
        confirmar_senha = request.POST.get('confirmar_senha')

        users = User.objects.filter(username=username)

        if users.exists():
            get_messages.add_message(request, constants.ERROR, "Usuario já existe.")
            return redirect('/usuarios/cadastro')

        if senha != confirmar_senha:
            get_messages.add_message(request, constants.ERROR, "A senha e o confirmar senha devem ser iguais.")
            return redirect('/usuarios/cadastro')

        if len(senha) < 6:
            get_messages.add_message(request, constants.ERROR, "A senha deve ter mais de 6 digitos.")
            return redirect('/usuarios/cadastro')
 
        try:
            User.objects.create_user(
                username=username,
                email=email,
                password=senha
            )
            return redirect('/usuarios/login')
        except:
            print('Erro 4')
        return redirect('/usuarios/cadastro')