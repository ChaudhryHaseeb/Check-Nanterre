from django.conf.urls import url
from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('connexion', views.connexion, name="connexion"),
    url(r'^deconnexion/$', auth_views.LogoutView.as_view(), {'next_page': 'index.html'}, name="deconnexion"),
    path('motdepasse/oublie', views.mdpOublie, name='mdpOublie'),
    path('etudiant/creation', views.creerEtudiant, name='creerEtudiant'),
    path('professeur/creation', views.creerProfesseur, name='creerProfesseur'),
]