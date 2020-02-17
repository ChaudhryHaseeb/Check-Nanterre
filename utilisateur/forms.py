from django import forms
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from absence.models import Promotion, PromotionEtudiants
from utilisateur.models import Utilisateur


class ConnexionForm(forms.Form):
    username = forms.CharField(label="Email", max_length=150,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username',
                                                             'placeholder': 'Email'}))
    password = forms.CharField(label="Mot de passe", max_length=30,
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password',
                                                                 'placeholder': 'Mot de passe'}))


class CreerEtudiant(forms.Form):
    prenom = forms.CharField(label=('Prénom'), max_length=50,
                             widget=forms.TextInput(attrs={'class': 'form-control', 'pattern': '[A-Za-z-]+$',
                                                           'placeholder': 'Prénom'}))
    nom = forms.CharField(label=('Nom'), max_length=50,
                          widget=forms.TextInput(attrs={'class': 'form-control', 'pattern': '[A-Za-z-]+$',
                                                        'placeholder': 'Nom'}))

    numero = forms.CharField(label=('Numéro étudiant'), max_length=8, required=False,
                             widget=forms.TextInput(attrs={'class': 'form-control', 'pattern': '[0-9]{8}',
                                                           'placeholder': 'Numéro étudiant'}))
    promotion = forms.ModelChoiceField(queryset=Promotion.objects.all(), label=('Promotion'), required=True,
                                     widget=forms.Select(attrs={'class': 'form-control'}))

    def save(self, id_utilisateur):
        etudiant = get_object_or_404(Utilisateur, pk=id_utilisateur)
        user = User.objects.get(username=etudiant.user.username, first_name=etudiant.user.first_name, last_name=etudiant.user.last_name)
        etudiant_promotion = PromotionEtudiants.objects.get(etudiant=id_utilisateur)
        user.first_name = self.cleaned_data['prenom']
        user.last_name = self.cleaned_data['nom']
        user.username = self.cleaned_data['numero']
        etudiant_promotion.promotion = self.cleaned_data['promotion']
        user.save()
        etudiant_promotion.save()


class CreerProfesseur(forms.Form):
    prenom = forms.CharField(label=('Prénom'), max_length=50,
                             widget=forms.TextInput(attrs={'class': 'form-control', 'pattern': '[A-Za-z-]+$',
                                                           'placeholder': 'Prénom'}))
    nom = forms.CharField(label=('Nom'), max_length=50,
                          widget=forms.TextInput(attrs={'class': 'form-control', 'pattern': '[A-Za-z-]+$',
                                                        'placeholder': 'Nom'}))

    email = forms.EmailField(label=('Email'), widget=forms.EmailInput(attrs={'class': 'form-control',
                                                                              'placeholder': 'Email'}))

    def save(self, id_professeur):
        prof = get_object_or_404(User, pk=id_professeur)
        user = User.objects.get(username=prof.username, first_name=prof.first_name, last_name=prof.last_name)
        user.first_name = self.cleaned_data['prenom']
        user.last_name = self.cleaned_data['nom']
        user.username = self.cleaned_data['email']
        user.save()


class MdpOublie(forms.Form):
    email = forms.EmailField(label=('Email'), widget=forms.EmailInput(attrs={'class': 'form-control',
                                                                             'placeholder': 'Email'}))
