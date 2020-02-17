from django.urls import path

from absence.api.views import get_all_promotions, liste_etudiant_dans_promotion, absence_etudiant_connecte, \
    absence_etudiant_justifier

app_name = 'absence'

urlpatterns = [
    path('promotions', get_all_promotions, name="allPromotionsApi"),
    path('promotions/etudiants/<int:id>', liste_etudiant_dans_promotion, name="listeEtudiantDansPromotionApi"),
    path('etudiant', absence_etudiant_connecte, name="absenceEtuConnecteApi"),
    path('etudiant/justification/<int:id>', absence_etudiant_justifier, name="absenceEtuJustifApi"),
]