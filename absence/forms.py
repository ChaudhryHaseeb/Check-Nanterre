from django import forms


class CreationMatiere(forms.Form):
    titre = forms.CharField(label="Titre", max_length=150,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Saisir le nom de la matière'}))