from django.conf.urls import url
from .views import RegistroUsuario,Contra,RegistroUsuario1
app_name="usuario"
urlpatterns=[
    url(r'contra',Contra.as_view(), name='contra'),
    url(r'^reg',RegistroUsuario1.as_view(),name="registra"),
	url(r'^registrar',RegistroUsuario.as_view(),name="registrarme"),
	

]