from django import forms
from dal import autocomplete
from .models import User, Weapon

class WeaponForm(forms.ModelForm):
    user_ssn_number = forms.ModelChoiceField(
    queryset=User.objects.all(),
    widget=autocomplete.ModelSelect2(url='user-autocomplete'))

class Meta:
    model = Weapon
    fields = ('name', 'user_ssn_number',)

