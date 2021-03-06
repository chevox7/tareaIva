"""tarea URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

from django.conf.urls import url, include
from django.contrib.auth.views import login,logout_then_login

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^sim/',include('apps.simulacion.urls',namespace="simu")),
    url(r'^usuario/',include('apps.usuario.urls',namespace="usuario")),
     url(r'^accounts/login/$', login, {'template_name':'usuario/login1.html'}, name='login' ),
    url(r'^logout/',logout_then_login, name='logout'), 
      
]
