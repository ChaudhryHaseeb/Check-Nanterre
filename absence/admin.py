from django.contrib import admin
from .models import Etudiant

class PromotionAdmin(admin.ModelAdmin):
    fields = ['nom_promotion', 'annee_filiere','status_promotion','etudiant']
    list_display = ('user', 'numero_etudiant')

admin.site.register(Etudiant, EtudiantAdmin)