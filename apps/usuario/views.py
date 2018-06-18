from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import RegistroForms
from django.views.generic import TemplateView

class Contra(TemplateView):
    template_name = 'usuario/login2.html'


class RegistroUsuario1(CreateView):
	model=User
	template_name="usuario/login3.html"
	form_class=UserCreationForm
	success_url =reverse_lazy('simu:index')


class RegistroUsuario(CreateView):
	model=User
	template_name="usuario/login3.html"
	form_class=RegistroForms
	success_url =reverse_lazy('simu:index')