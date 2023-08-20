from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()


# from django.contrib.auth.forms import AuthenticationForm

class CustomAuthenticationForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Email'}),
        label='Email',
        required=True
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'}),
        label='Password',
        required=True
    )

class ForgotPasswordForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Email'}),
        label='Email',
        required=True
    )
    def clean_email(self):
        email = self.cleaned_data.get('email')
        print(email)
        if not User.objects.filter(email=email).exists():
            print("not wdkjjsd")
            raise ValidationError("User with this email doesn't exist.")
        return email







class ResetPasswordForm(forms.Form):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'}),
        label='Password',
        required=True
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}),
        label='Password',
        required=True
    )
    
