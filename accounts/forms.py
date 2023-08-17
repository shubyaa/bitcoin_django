from dataclasses import field
from django.contrib.auth.forms import UserCreationForm
from .models import UserModel, UserNotificationSettings
from django import forms


# To create our own customization inside the exisiting form provided by Django
class CreateUserCreationForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ['username', 'email', 'password1', 'password2']   
    
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder': 'Your Username'})
        self.fields['email'].widget.attrs.update({'placeholder':'E-mail'})
        self.fields['password1'].widget.attrs.update({'placeholder': 'Password'})        
        self.fields['password2'].widget.attrs.update({'placeholder': 'Repeat Password'})


class UserNotificationSettings(forms.ModelForm):
    class Meta:
        model = UserNotificationSettings
        fields="__all__"
        
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)