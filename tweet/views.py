from django.shortcuts import render
from django.core.serializers import serialize
from .models import Twitt
# Create your views here.

def Tview(user):
    #Realizando QuerySet y ordenando este de forma Desendente con la fecha
    data = Twitt.objects.filter(user_twit_id=user.id).order_by('-date_twit')
    return data

