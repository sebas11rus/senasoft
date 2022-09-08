from django.shortcuts import render, HttpResponse, redirect
from registroApp.models import Sondeo, Pregunta, Respuesta
from .proccess import html_pdf
from django.views.generic import View


# Create your views here.


def index(request):
    sondeos = Sondeo.objects.all()
    return render(request, 'index.html', {'sondeos': sondeos})


def contestar(request):
    
    sondeos = Sondeo.objects.filter(visible=True, )
    return render(request, 'contestar.html', {'sondeos': sondeos})


def error(request):
    return render(request, 'error.html')


# vista basada en clase
class Generar_pdf(View):

    def get(self, request):
        # traer el template
        pdf = html_pdf('reporte.html')

        # redige el html
        return HttpResponse(pdf, content_type='application/pdf')



