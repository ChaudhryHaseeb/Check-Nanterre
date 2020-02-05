from django.contrib import admin
from .models import Etudiant

class EtudiantAdmin(admin.ModelAdmin):
    fields = ['user', 'numero_etudiant']
    list_display = ('user', 'numero_etudiant')

admin.site.register(Etudiant, EtudiantAdmin)