from django import forms

class CreateStudent(forms.Form):

    numero = forms.CharField(label=_('Numéro étudiant'), max_length=8, required=False,
                             widget=forms.TextInput(attrs={'class': 'form-control', 'pattern': '[0-9]+$',
                                                           'placeholder': 'Numéro étudiant'}))
    prenom = forms.CharField(label=_('Prénom'), max_length=50,
                             widget=forms.TextInput(attrs={'class': 'form-control', 'pattern': '[A-Za-z-]+$',
                                                           'placeholder': 'Prénom'}))
    nom = forms.CharField(label=_('Nom'), max_length=50,
                          widget=forms.TextInput(attrs={'class': 'form-control', 'pattern': '[A-Za-z-]+$',
                                                        'placeholder': 'Nom'}))

    email = forms.EmailField(label=_('Email'), widget=forms.EmailInput(attrs={'class': 'form-control',
                                                                              'placeholder': 'Email'}))
    mot_de_passe = forms.CharField(label=_("Mot de passe"), max_length=30,
                                   widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                     'placeholder': 'Mot de passe'}))
    mot_de_passe_confirmation = forms.CharField(label=_("Mot de passe"), max_length=30,
                                                widget=forms.PasswordInput(
                                                    attrs={'class': 'form-control',
                                                           'placeholder': 'Confirmation du mot de passe'}))