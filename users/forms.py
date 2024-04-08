from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserModel

class InscriptionForm(forms.ModelForm):
    
    class Meta:
        model = UserModel
        fields = "__all__"
        widgets = {
            'date_naissance': forms.DateInput(attrs={'type': 'date'}),
            'mot_de_pass': forms.PasswordInput(),
            'confirmer_mot_de_pass': forms.PasswordInput(),
            "email":forms.EmailInput(),
        }


    
