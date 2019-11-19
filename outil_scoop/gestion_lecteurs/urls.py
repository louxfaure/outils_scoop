"""outil_scoop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path('recherche-lecteur',views.recherche_lecteur, name='recherche-lecteur'),
    path('lecteur/<str:type_identifiant>/<str:identifiant>', views.lecteur, name='lecteur'),
    path('modification-lecteur/<str:identifiant>', views.modif_lecteur ,name='modif-lecteur'),
    path('suppression-lecteur/<str:identifiant>/<str:list_etab>', views.suppr_lecteur ,name='suppr-lecteur'),
    path('result-modification-lecteur/<str:identifiant>', views.result_modif_lecteur ,name='result-modif-lecteur'),
]
