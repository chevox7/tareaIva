

from django.conf.urls import url, include
from .views import Index, Contra, Res, Entradas, SimulacionDelete, Lista, Guardar
from django.contrib.auth.decorators import login_required
#from django.urls import re_path

app_name="simu"
urlpatterns = [
 url(r'index',login_required(Index.as_view()), name='index'),
 url(r'entradas',login_required(Entradas),name="entradas"),
 url(r'listado',login_required(Lista.as_view()), name='lista'),
 url(r'contra',Contra.as_view(), name='contra'),
 url(r'^delete/(?P<pk>\d+)/$',login_required(SimulacionDelete.as_view()) ,name='delete',),
 url(r'res',login_required(Res.as_view()), name='res'),
 url(r'guardar',login_required(Guardar),name="guardar"),
]