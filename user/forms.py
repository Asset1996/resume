"""
Forms for user app.
"""
from django import forms
from main.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    """Form for registering new user."""
    email = forms.EmailField(required=True)
    password = forms.PasswordInput()

    class Meta:
      model = User
      fields = ['name_en', 'name_ru', 'email', 'password1', 'password2']
    
    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class LoginForm(forms.Form):
    """Form for authenticating the user."""
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        fields = ['email', 'password']

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
