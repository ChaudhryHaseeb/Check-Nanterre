from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('connexion', views.connexion, name="connexion"),
    path('deconnexion/', auth_views.LogoutView.as_view(), {'next_page': 'index.html'}, name="deconnexion"),
    path('creation/etudiant', views.creer_etudiant, name='creer_etudiant'),
    path('creation/professeur', views.creer_professeur, name='creer_professeur'),
    path('afficher/listeProfs', views.liste_professeur, name='liste_professeur'),
    path('afficher/listeEtudiants', views.liste_etudiant, name='liste_etudiant'),
    path('modifier/etudiant/<int:id_utilisateur>/', views.modifier_etudiant, name='modifier_etudiant'),
    path('modifier/professeur/<int:id_professeur>/', views.modifier_prof, name='modifier_professeur')
]
