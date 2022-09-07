from django.shortcuts import render

# Create your views here.

def sondeo(request):
    return render(request, 'sondeo.html')
