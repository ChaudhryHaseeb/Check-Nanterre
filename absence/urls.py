from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path('creation/matiere', views.creer_matiere, name='creer_matiere'),
    path('afficher/listeMatiere', views.liste_matiere, name='liste_matiere'),
    path('modifier/matiere/<int:id_matiere>/', views.modifier_matiere, name='modifier_matiere'),
    path('supprimer/matiere/<int:id_matiere>/', views.supprimer_matiere, name='supprimer_matiere'),
    path('afficher/listePromotion/', views.liste_promotion, name='liste_promotion'),
    path('afficher/promotion/<int:id_promotion>/', views.promotion_contenu, name='promotion_contenu'),
    path('creation/promotion/', views.creer_promotion, name='creer_promotion'),
]
