from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

class indexr(TemplateView):
	template_name='simulacion/pruebabase.html'