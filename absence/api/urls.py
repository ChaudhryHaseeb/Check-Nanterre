from django.urls import path

from absence.api.views import get_all_promotions, liste_etudiant_dans_promotion

app_name = 'absence'

urlpatterns = [
    path('promotions', get_all_promotions, name="allPromotionsApi"),
    path('promotions/etudiants/<int:id>', liste_etudiant_dans_promotion, name="listeEtudiantDansPromotion"),
]