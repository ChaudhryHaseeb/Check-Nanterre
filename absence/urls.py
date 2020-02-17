from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path('creation/matiere', views.creer_matiere, name='creer_matiere'),
    path('afficher/listeMatiere', views.liste_matiere, name='liste_matiere'),
    path('modifier/matiere/<int:id_matiere>/', views.modifier_matiere, name='modifier_matiere'),
    path('supprimer/matiere/<int:id_matiere>/', views.supprimer_matiere, name='supprimer_matiere'),
]
