from django import forms
from django.shortcuts import get_object_or_404

from absence.models import Matiere


class CreationMatiere(forms.Form):
    titre = forms.CharField(label="Titre", max_length=150,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Saisir le nom de la matière'}))


class ModifierMatiere(forms.Form):
    titre = forms.CharField(label="Titre", max_length=150,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Saisir le nom de la matière'}))

    def save(self, id_matiere):
        matiere = get_object_or_404(Matiere, pk=id_matiere)
        matiere.titre = self.cleaned_data['titre']
        matiere.save()


