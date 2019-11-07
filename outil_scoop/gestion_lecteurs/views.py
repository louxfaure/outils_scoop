from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import LecteurForm
from . import services


def recherche_lecteur(request):
    form = LecteurForm(request.POST or None)
    if form.is_valid():
        id_lecteur = form.cleaned_data['identifiant']
        return HttpResponseRedirect(reverse('lecteur', kwargs={'identifiant': id_lecteur}))
    return render(request, "gestion_lecteurs/recherche_lecteur.html", locals())

def lecteur(request,identifiant):
    user = services.User(identifiant)
    datas = ("full_name","job_category","user_group","record_type","account_type","expiry_date","loans","requests")
    user_data_in_table = user.get_user_data_in_table(datas)
    return render(request, "gestion_lecteurs/lecteur.html", locals())

def modif_lecteur(request,identifiant,list_etab):
    return render(request, "gestion_lecteurs/modif-lecteur.html", locals())