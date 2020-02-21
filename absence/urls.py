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
    path('afficher/listeSeance/', views.liste_seance, name='liste_seance'),
    path('afficher/listeAbsence/', views.liste_absence, name='liste_absence'),
    path('afficher/listeSeanceAbsence/<int:id_seance>/', views.liste_seance_absence, name='liste_seance_absence'),
    path('afficher/Absence/<int:id_absence>/', views.absence, name='absence'),
    path('afficher/listeEtudiantAbsence/<int:id_etudiant>/', views.liste_etudiant_absence, name='liste_etudiant_absence'),
    path('import/<int:id_promotion>', views.import_file, name='import_file'),
]
