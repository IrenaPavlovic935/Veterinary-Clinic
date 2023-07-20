from django import forms
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django.contrib.auth.models import User
from blog.models import Profile

class RegisterUserForm(UserCreationForm):
    email= forms.EmailField()
    first_name=forms.CharField(max_length=50)
    last_name=forms.CharField(max_length=50)
    
    class Meta:
        model=User
        fields=('username', 'first_name', 'last_name', 'email','password1', 'password2')
        

class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password'}))
    
    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')
        
from datetime import datetime
from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone

from blog.models import Profile

class ProfilePageForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('biography', 'profile_pic', 'instagram_url', 'phone', 'email', 'birthday')
        
        widgets = {
            'biography': forms.TextInput(attrs={'class': 'form-control'}),
            'profile_pic': forms.FileInput(attrs={'class': 'form-control'}),
            'instagram_url': forms.Textarea(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'birthday': forms.TextInput(attrs={'class': 'form-control'}),
        }
        
    def clean_birthday(self):
        birthday = self.cleaned_data['birthday']
        
       
        try:
            parsed_birthday = datetime.strptime(birthday, "%Y-%m-%d").date()
        except ValueError:
            raise forms.ValidationError("Please enter a valid date in the format YYYY-MM-DD.")
        
        if parsed_birthday > timezone.now().date():
            raise forms.ValidationError("The date of birth cannot be in the future")
        
        return parsed_birthday

    
