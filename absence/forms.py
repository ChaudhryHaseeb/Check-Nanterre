from django import forms
from django.shortcuts import get_object_or_404

from absence.models import Matiere, Promotion


class CreationMatiere(forms.Form):
    titre = forms.CharField(label="Titre", max_length=150,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Saisir le nom de la matière'}))

    def save(self, id_matiere):
        matiere = get_object_or_404(Matiere, pk=id_matiere)
        matiere.titre = self.cleaned_data['titre']
        matiere.save()


class CreationPromotion(forms.Form):
    nom = forms.ChoiceField(choices=Promotion.NOM_PROMOTION, label=('Nom'), required=True,
                               widget=forms.Select(attrs={'class': 'form-control'}))
    status = forms.ChoiceField(choices=Promotion.STATUS_PROMOTION, label=('Status'), required=True,
                                       widget=forms.Select(attrs={'class': 'form-control'}))
    annee = forms.CharField(label=('Année de Promotion'), max_length=9, required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control', 'pattern': '[0-9]{4}-[0-9]{4}',
                                                           'placeholder': '2020-2021'}))


class ImportFile(forms.Form):
    file = forms.FileField(label='Choisissez un fichier')
