from urllib import response
from django.shortcuts import render, HttpResponse, redirect
from .forms import RegistroForm
from .models import Ciudadano

#  

# from django.template.loader import render_to_string

# from weasyprint import *

# Create your views here.


def registro(request):
    form = RegistroForm()
    if request.method == "POST":
        ciudadano = Ciudadano(
            tipo_doc=request.POST["tipo_doc"], n_doc=request.POST["n_doc"], nom=request.POST["nom"],
            ape=request.POST["ape"], sexo=request.POST["sexo"], cel=request.POST["cel"], tel=request.POST["tel"],
            mun=request.POST["mun"], dire=request.POST["dire"], barrio=request.POST["barrio"], fecha_nac=request.POST["fecha_nac"],
            etnia=request.POST["etnia"], disc=request.POST["disc"], estrato=request.POST["estrato"], accs_tec=request.POST["accs_tec"],
            cuales=request.POST["cuales"], con_int=request.POST["con_int"], reg=request.POST["reg"])
        ciudadano.save()
        return redirect('index')
    else:
        return render(request, 'registro.html', {'form': form})


# def get( request):

#     response = HttpResponse(content_type='application/pdf')

#     buffer = BytesIO()

#     pdf = canvas.Canvas(buffer)
#     pdf.showPage()
#     pdf.save()
#     pdf = buffer.getvalue()
#     buffer.close()
#     response.write(pdf)

#     return  response
