from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import LecteurForm
from .forms import ChangeLecteurForm
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

def modif_lecteur(request,identifiant):
    form =  ChangeLecteurForm(request.POST or None)
    if form.is_valid():
        user_data = request.session.get(identifiant)
        new_id_lecteur = form.cleaned_data['nouvel_identifiant']
        expiry_date = form.cleaned_data['date_expiration']
        for institution  in user_data:
            if new_id_lecteur:
                user_data[institution]['primary_id'] = new_id_lecteur
            if expiry_date:
                date =  "{}Z".format(expiry_date.strftime("%Y-%m-%d"))
                user_data[institution]['expiry_date'] = date
                user_data[institution]['purge_date'] = date
        request.session[identifiant]=user_data
        return HttpResponseRedirect(reverse('result-modif-lecteur',kwargs={'identifiant': identifiant}))
    return render(request, "gestion_lecteurs/modif-lecteur.html", locals())

def result_modif_lecteur(request,identifiant):
    results = {}
    user_data = request.session.get(identifiant)
    for institution  in user_data:
        api_key = os.getenv("TEST_{}_API".format(institution))
        api = Alma_Apis_Users.AlmaUsers(apikey=api_key, region='EU', service='test')
        results[institution] = {}
        results[institution]["status"], results[institution]["response"] = api.update_user(identifiant,
                                                                                        "user_group,job_category,pin_number,preferred_language,campus_code,rs_libraries,user_title,library_notices",
                                                                                            json.dumps(user_data[institution]),
                                                                                            accept='json',
                                                                                            content_type='json') 
    return render(request, "gestion_lecteurs/result-modif-lecteur.html", locals())