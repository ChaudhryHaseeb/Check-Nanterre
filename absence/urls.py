from django.urls import path

from . import views

urlpatterns = [
    path('creation/matiere', views.creer_matiere, name='creer_matiere'),
    path('afficher/listeMatiere', views.liste_matiere, name='liste_matiere'),
]
