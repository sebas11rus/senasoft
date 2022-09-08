from django.shortcuts import render, redirect
from registroApp.models import Ciudadano, Sondeo
from django.contrib.auth.models import User

from registroApp.models import Condicion

# Create your views here.
def user(request):
    if request.method=="GET":    
        if request.user.is_authenticated:
            usuario1 = request.user.username
            datos = Ciudadano.objects.filter(usuario=usuario1)
            
            # condicion =""
            
            sondeos = Sondeo.objects.all()
            # for sondeo in sondeos:
            #     condicion = Condicion.objects.filter(id=sondeo.id_condicion)

            # sondeos = Sondeo.objects.all()
                        
            # for dato in datos:
            #     for sondeo in sondeos:    
            #         barr = sondeo.brr   
            #         grupo = sondeo.grupo                                 
            #         sondeos = Sondeo.objects.filter(barr=dato.barrio,grupo=dato.etnia)            
                
            return render(request, 'user.html',{'usuario':usuario1, 'datos':datos, 'sondeos': sondeos  } )
        else:
            return redirect( 'index')
        