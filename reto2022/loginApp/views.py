from email import message
from pyexpat.errors import messages
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.views import View


# Create your views here.


class RegistroUser(View):

    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:

            return render(request, 'login.html', {'form': form})


def cerrar_sesion(request):
    logout(request)
    return redirect('/')


def iniciar_sesion(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'campo invalido')
    else:
        form = UserCreationForm()

    return render(request, 'singup.html', {'form': form})
    