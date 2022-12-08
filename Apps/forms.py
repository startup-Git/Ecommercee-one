from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordChangeForm,SetPasswordForm, PasswordResetForm
# from django.core.exceptions import ValidationError
# from django.forms.fields import EmailField
# from django.forms.forms import Form
from .models import Customer

class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'class': "form-control"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'class':'form-control'}))

class CustomeRegistrationForm(UserCreationForm):
    username = forms.CharField(label="User name", required=True, widget=forms.TextInput(attrs={'class': "form-control"}))
    email = forms.EmailField(label="Enter Mail", required=True, widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label='Password', required=True, widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password', required=True, widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
    # def username_clean(self):
    #     username = self.cleaned_data['username'].lower()
    #     new = User.objects.filter(username = username)
    #     if new.count():
    #         raise ValidationError("User Already Exist.")
    #     return username
    
    # def email_clean(self):
    #     email = self.cleaned_data['email'].lower()
    #     new = User.objects.filter(email = email)
    #     if new.count():
    #         raise ValidationError("Email Already Exist.")
    #     return email
    
    # def clean_password2(self) -> str:
    #     password1 = self.cleaned_data['password1']
    #     password2 = self.cleaned_data['password2']

    #     if password1 and password2 and password1 != password2:
    #         raise ValidationError("Password don't match.")
    #     return password2
    
    # def save(self, commit = True):
    #     user = User.objects.create_user(
    #         self.cleaned_data['username'],
    #         self.cleaned_data['email'],
    #         self.cleaned_data['password1']
    #     )
    #     return user
class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label='old password', widget=forms.PasswordInput(attrs={'autofocus':'True', 'class':'form-control', 'autocomplete':'current-password'}))
    new_password1 = forms.CharField(label='new password', widget=forms.PasswordInput(attrs={'autofocus':'True', 'class':'form-control', 'autocomplete':'current-password'}))
    new_password2 = forms.CharField(label='confirm password', widget=forms.PasswordInput(attrs={'autofocus':'True', 'class':'form-control', 'autocomplete':'current-password'}))

class MyPasswordResetForm(PasswordResetForm):
    email  = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
class MySetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label='new password', widget=forms.PasswordInput(attrs={'autofocus':'True', 'class':'form-control', 'autocomplete':'current-password'}))
    new_password2 = forms.CharField(label='confirm password', widget=forms.PasswordInput(attrs={'autofocus':'True', 'class':'form-control', 'autocomplete':'current-password'}))

class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'locality', 'city', 'mobile', 'state', 'zipcode']
        widgets={
            'name':forms.TextInput(attrs={'class': "form-control"}),
            'locality':forms.TextInput(attrs={'class': "form-control"}),
            'city':forms.TextInput(attrs={'class': "form-control"}),
            'mobile':forms.NumberInput(attrs={'class': "form-control"}),
            'state':forms.Select(attrs={'class': "form-control"}),
            'zipcode':forms.NumberInput(attrs={'class': "form-control"}),
        }