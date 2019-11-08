from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import LecteurForm
from . import services
import os
import json
from Alma_Apis_Interface import Alma_Apis_Users


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
    request.session[identifiant] = user.user_data
    return render(request, "gestion_lecteurs/lecteur.html", locals())

def suppr_lecteur(request,identifiant,list_etab):
    results = {}
    for etab in list_etab.split(','):
        results[etab] = {}
        api_key = os.getenv("TEST_{}_API".format(etab))
        api = Alma_Apis_Users.AlmaUsers(apikey=api_key, region='EU', service='test')
        results[etab]['status'],results[etab]['response'] = api.delete_user(identifiant)
    return render(request, "gestion_lecteurs/suppr-lecteur.html", locals())

def modif_lecteur(request,identifiant,list_etab):
    user_data = request.session.get(identifiant)
    for institution  in user_data:
        user_data[institution]['primary_id'] = "valeur de test"
        json.dumps(user_data[institution]) 
    return render(request, "gestion_lecteurs/modif-lecteur.html", locals())