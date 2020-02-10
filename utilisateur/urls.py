from django.conf.urls import url
from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
from .forms import ConnexionForm

urlpatterns = [
    path('connexion', views.connexion, name="connexion"),
    url(r'^deconnexion/$', auth_views.LogoutView.as_view(), {'next_page': 'index.html'}, name="deconnexion"),
    path('etudiant/creation', views.creerEtudiant, name='creerEtudiant'),
    path('professeur/creation', views.creerProfesseur, name='creerProfesseur'),
]