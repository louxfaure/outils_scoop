from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect

# Create your views here.
def home(request):
    return render(request, 'home_page/index.html')