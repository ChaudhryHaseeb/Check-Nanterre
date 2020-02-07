from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Promotion, Etudiant


def index(request):
    Etu = Etudiant()
    pr = Promotion(nom_promotion="L1", annee_filiere="2019/2020", status_promotion="cla")
    pr.save()
    return HttpResponse("Test")
