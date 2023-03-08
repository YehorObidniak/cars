"""cars_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from . import settings
from django.conf.urls.static import static
from main.views import index, load_more_dubicars, load_more_dubizzle, load_more_yallamotor, dubicars, dubizzle, yallamotor

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('dubicars/', dubicars, name='dubicars'),
    path('dubizzle/', dubizzle, name='dubizzle'),
    path('yallamotor/', yallamotor, name='yallamotor'),
    path('load_dubicars/', load_more_dubicars, name='load_dubicars'),
    path('load_dubizzle/', load_more_dubizzle, name='load_dubizzle'),
    path('load_yallamotor/', load_more_yallamotor, name='load_yallamotor'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

