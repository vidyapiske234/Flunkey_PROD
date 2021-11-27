from django import forms
from .models import CustomUser as User

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')
    
class SignupForm(forms.ModelForm):
    pass