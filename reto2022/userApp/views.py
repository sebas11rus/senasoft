from django.shortcuts import render
from registroApp.models import Ciudadano
from django.contrib.auth.models import User

# Create your views here.
def user(request):
    if request.method=="POST":    
        if User.is_authenticated:
            usuario = User.cleaned_data.get("username")            
            datos = Ciudadano.objects.filter('usuario' == usuario)
    else:
        return render(request, 'user.html')