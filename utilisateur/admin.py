from django.contrib import admin

from utilisateur.models import Utilisateur


class UtilisateurAdmin(admin.ModelAdmin):
    fields = ['user', 'role']
    list_display = ('user', 'role')

admin.site.register(Utilisateur, UtilisateurAdmin)