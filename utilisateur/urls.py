from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('etudiant/creation', views.creerEtudiant, name='creerEtudiant'),
    path('professeur/creation', views.creerProfesseur, name='creerProfesseur'),
]