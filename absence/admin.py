from django.contrib import admin
from .models import Promotion, Matiere, Seance, Absence, PromotionEtudiants, MatiereProfesseur,\
    MatierePromotion, SeanceMatiere, SeanceProfesseur, SeancePromotion, AbsenceSeance, AbsenceEtudiants


class PromotionAdmin(admin.ModelAdmin):
    fields = ['nom_promotion', 'annee_filiere','status_promotion']
    list_display = ('nom_promotion', 'annee_filiere', 'status_promotion')


admin.site.register(Promotion, PromotionAdmin)


class PromotionEtudiantsAdmin(admin.ModelAdmin):
    fields = ['etudiant', 'promotion']
    list_display = ('etudiant', 'promotion')


admin.site.register(PromotionEtudiants, PromotionEtudiantsAdmin)


class MatiereAdmin(admin.ModelAdmin):
    fields = ['titre']
    list_display = ('titre',)


admin.site.register(Matiere, MatiereAdmin)


class MatiereProfesseurAdmin(admin.ModelAdmin):
    fields = ['professeur_matiere', 'matiere']
    list_display = ('professeur_matiere', 'matiere')


admin.site.register(MatiereProfesseur, MatiereProfesseurAdmin)


class MatierePromotionAdmin(admin.ModelAdmin):
    fields = ['promotion_matiere', 'matiere']
    list_display = ('promotion_matiere', 'matiere')


admin.site.register(MatierePromotion, MatierePromotionAdmin)


class SeanceAdmin(admin.ModelAdmin):
    fields = ['date_seance', 'heure_deb','heure_fin']
    list_display = ('date_seance', 'heure_deb','heure_fin')


admin.site.register(Seance, SeanceAdmin)


class SeanceMatiereAdmin(admin.ModelAdmin):
    fields = ['seance_matiere', 'matiere']
    list_display = ('seance_matiere', 'matiere')


admin.site.register(SeanceMatiere, SeanceMatiereAdmin)


class SeanceProfesseurAdmin(admin.ModelAdmin):
    fields = ['seance_professeur', 'professeur']
    list_display = ('seance_professeur', 'professeur')


admin.site.register(SeanceProfesseur, SeanceProfesseurAdmin)


class SeancePromotionAdmin(admin.ModelAdmin):
    fields = ['seance_promotion', 'promotion']
    list_display = ('seance_promotion', 'promotion')


admin.site.register(SeancePromotion, SeancePromotionAdmin)


class AbsenceAdmin(admin.ModelAdmin):
    fields = ['absent', 'retard', 'justification']
    list_display = ('absent', 'retard', 'justification')


admin.site.register(Absence, AbsenceAdmin)


class AbsenceEtudiantAdmin(admin.ModelAdmin):
    fields = ['absence_etudiant', 'etudiant']
    list_display = ('absence_etudiant', 'etudiant')


admin.site.register(AbsenceEtudiants, AbsenceEtudiantAdmin)


class AbsenceSeanceAdmin(admin.ModelAdmin):
    fields = ['absence_seance', 'seance']
    list_display = ('absence_seance', 'seance')


admin.site.register(AbsenceSeance, AbsenceSeanceAdmin)