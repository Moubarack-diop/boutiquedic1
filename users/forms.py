from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserModel

class InscriptionForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = "__all__"

class ConnexionForm(forms.ModelForm):
    class Meta:
        model=UserModel
        fields=['email', 'mot_de_pass']