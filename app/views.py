from django.shortcuts import render

from app.forms import * 
# from django.http import HttpResponse
from app.models import *

# Create your views here.

def data_registation(request):
    ERFO = RegistationForm()
    d = {'ERFO':ERFO}
    if request.method == 'POST':
        DRFO = RegistationForm(request.POST)
        if DRFO.is_valid():
            name = DRFO.cleaned_data['name']
            age = DRFO.cleaned_data['age']
            password = DRFO.cleaned_data['password']
            gender = DRFO.cleaned_data['gender']
            course = DRFO.cleaned_data['course']
            ro = Registation.objects.get_or_create(name = name,age = age,password = password,gender = gender,course = course)[0]
            ro.save()
            QSRO = Registation.objects.all()
            d1 = {'QSRO':QSRO}
            return render(request,'display_data.html',d1)
    return render(request,'data_registation.html',d)