from pyexpat.errors import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect


def register_view(request):
    if request.method == "POST":
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, "Cadastro realizado com sucesso! Faça login.")
            return redirect('login')
        else:
            messages.error(request, "Corrija os erros abaixo.")
    else:
        user_form = UserCreationForm()
    return render(
        request,
        'register.html',
        {'user_form': user_form}
    )

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redireciona para a lista de carros após login bem-sucedido
            return redirect('cars_list')
        else:
            login_form = AuthenticationForm(request, data=request.POST)
            return render(
                request, 
                'login.html', 
                {'login_form': login_form, 'error': 'Credenciais inválidas.'}
            )
    else:
        login_form = AuthenticationForm()
    return render(
        request, 
        'login.html', 
        {'login_form': login_form})

def logout_view(request):
    logout(request)
    messages.success(request, "Você foi desconectado com sucesso.")
    return redirect('login')