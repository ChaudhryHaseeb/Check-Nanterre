from django.urls import path

from absence.api.views import get_all_promotions, liste_etudiant_dans_promotion, absence_etudiant_connecte, \
    absence_etudiant_justifier, seance_creation, absence_creation, list_seance_prof, \
    list_etudiant_seance, list_etudiant_absent_seance, absence_modifier, list_matiere

app_name = 'absence'

urlpatterns = [
    path('promotions', get_all_promotions, name="allPromotionsApi"),
    path('promotions/etudiants/<int:id>', liste_etudiant_dans_promotion, name="listeEtudiantDansPromotionApi"),
    path('etudiant', absence_etudiant_connecte, name="absenceEtuConnecteApi"),
    path('etudiant/justification/<int:id>', absence_etudiant_justifier, name="absenceEtuJustifApi"),
    path('seance/creation', seance_creation, name="seanceCreationApi"),
    path('creation', absence_creation, name="absenceCreationApi"),
    path('<int:id>', absence_modifier, name="absenceModifierApi"),
    path('professeur/seances', list_seance_prof, name="seanceListProfApi"),
    path('matieres/', list_matiere, name="matiereListApi"),
    path('seances/etudiant/<int:id>', list_etudiant_seance, name="seanceListPresenceApi"),
    path('seances/absence/<int:id>', list_etudiant_absent_seance, name="seanceListPresenceApi"),
]