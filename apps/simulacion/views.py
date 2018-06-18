from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse
from django.views.generic import ListView,TemplateView,DeleteView
from .forms import EntradaForm
from .models import Simulacion,DatoEntrada
from django.views.generic import ListView,CreateView,DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.template import RequestContext 
# Create your views here.


class Index(TemplateView):
    template_name = 'simulacion/index.html'


class Lista(ListView):
		model=Simulacion
		template_name = 'simulacion/listado.html'

class Contra(TemplateView):
    template_name = 'usuario/login2.html'

class Res(TemplateView):
      template_name = 'resultado/res.html'    




def Entradas(request):
	if request.method == 'POST':
		
				form1 = EntradaForm(request.POST)
				if form1.is_valid():
					salario=request.POST.get('salario')
					renta=request.POST.get('renta')
					ganancias=request.POST.get('ganancias')
					interes=request.POST.get('interes')
					impuestos_indirectos=request.POST.get('impuestos_indirectos')
					depreciacion=request.POST.get('depreciacion')
					subsidios=request.POST.get('subsidios')
					poblacion=request.POST.get('poblacion')
					can_Ampliada=request.POST.get('can_Ampliada')
					salario_Minimo=request.POST.get('salario_Minimo')
					anios_simulados=request.POST.get('anios_simulados')
					iva_simulado=request.POST.get('iva_simulado')
					pib1=0
					percapita1=0
					canasta1=0
					crecimiento1=0
					inflacion1=0
					pib2=0
					percapita2=0
					canasta2=0
					crecimiento2=0
					inflacion2=0
					#form1.save()

					
					
				return render_to_response('resultado/resultado.html', {'salario':salario, 'renta':renta, 'ganancias':ganancias, 'poblacion':poblacion, 'salminimo':salario_Minimo, 'iva_simulado':iva_simulado,
					'pib1':pib1,'percapita1':percapita1, 'canasta1':canasta1, 'crecimiento1':crecimiento1,'inflacion1':inflacion1, 'pib2':pib2,'percapita2':percapita2,
					'canasta2':canasta2,'crecimiento2':crecimiento2,'inflacion2':inflacion2,'form1':form1})

	else:
			form1=EntradaForm()

	#contexto ={
	#'entradas':form1,'salidas':suma
	#}
	return render(request,'simulacion/entradas.html', {'form1':form1})

class SimulacionDelete(DeleteView):
	model=Simulacion
	template_name='simulacion/delete.html'
	success_url= reverse_lazy('simu:lista')



def Guardar(request):

	return redirect('simu:index')



