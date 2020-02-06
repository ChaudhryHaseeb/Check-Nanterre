from django import forms

class CreerEtudiant(forms.Form):
    prenom = forms.CharField(label=('Prénom'), max_length=50,
                             widget=forms.TextInput(attrs={'class': 'form-control', 'pattern': '[A-Za-z-]+$',
                                                           'placeholder': 'Prénom'}))
    nom = forms.CharField(label=('Nom'), max_length=50,
                          widget=forms.TextInput(attrs={'class': 'form-control', 'pattern': '[A-Za-z-]+$',
                                                        'placeholder': 'Nom'}))

    email = forms.EmailField(label=('Email'), widget=forms.EmailInput(attrs={'class': 'form-control',
                                                                              'placeholder': 'Email'}))

    numero = forms.CharField(label=('Numéro étudiant'), max_length=8, required=False,
                             widget=forms.TextInput(attrs={'class': 'form-control', 'pattern': '[0-9]+$',
                                                           'placeholder': 'Numéro étudiant'}))


class CreerProfesseur(forms.Form):
    prenom = forms.CharField(label=('Prénom'), max_length=50,
                             widget=forms.TextInput(attrs={'class': 'form-control', 'pattern': '[A-Za-z-]+$',
                                                           'placeholder': 'Prénom'}))
    nom = forms.CharField(label=('Nom'), max_length=50,
                          widget=forms.TextInput(attrs={'class': 'form-control', 'pattern': '[A-Za-z-]+$',
                                                        'placeholder': 'Nom'}))

    email = forms.EmailField(label=('Email'), widget=forms.EmailInput(attrs={'class': 'form-control',
                                                                              'placeholder': 'Email'}))
