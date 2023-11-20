from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django import forms

class UserChangeForm(UserChangeForm):
    class Meta:
        fields = ["email",]

class UserCreationForm(UserCreationForm):
    class Meta:
        fields = ["email",]
        

# FORMS
class LoginForm(forms.Form):
    '''Form to login users'''
    
    email = forms.EmailField(max_length=50, required=True, label='Email', widget=forms.EmailInput(attrs={
        'placeholder': 'Enter your email', 
        'class': 'input-field',
    }))
    
    password = forms.CharField(max_length=30, min_length=8, required=True, label='Password', widget=forms.PasswordInput(attrs={
        'placeholder': 'Ex. Johndoe@123',
        'class': 'input-field',
    }))
    
    
class SignUpForm(forms.Form):
    '''Form to login users'''
    
    first_name = forms.CharField(max_length=100, required=True, label='First Name', widget=forms.TextInput(attrs={
        'placeholder': 'Enter your first name', 
        'class': 'input-field',
    }))
    
    last_name = forms.CharField(max_length=100, required=True, label='Last Name', widget=forms.TextInput(attrs={
        'placeholder': 'Enter your last name', 
        'class': 'input-field',
    }))
    
    email = forms.EmailField(max_length=50, required=True, label='Email', widget=forms.EmailInput(attrs={
        'placeholder': 'Enter your email', 
        'class': 'input-field',
    }))
    
    password = forms.CharField(max_length=30, min_length=8, required=True, label='Password', widget=forms.PasswordInput(attrs={
        'placeholder': 'Ex. Johndoe@123',
        'class': 'input-field',
    }))
    
    password2 = forms.CharField(max_length=30, min_length=8, required=True, label='Confirm zPassword', widget=forms.PasswordInput(attrs={
        'placeholder': 'Ex. Johndoe@123',
        'class': 'input-field',
    }))
    

class EditDetailsForm(forms.Form):
    '''Form to update user details'''
    
    first_name = forms.CharField(max_length=100, required=True, label='First Name', widget=forms.TextInput(attrs={
        'placeholder': 'Enter your first name', 
        'class': 'input-field',
    }))
    
    last_name = forms.CharField(max_length=100, required=True, label='Last Name', widget=forms.TextInput(attrs={
        'placeholder': 'Enter your last name', 
        'class': 'input-field',
    }))
    
    email = forms.EmailField(max_length=50, required=True, label='Email', widget=forms.EmailInput(attrs={
        'placeholder': 'Enter your email', 
        'class': 'input-field',
    }))
    
    
class ChangePasswordForm(forms.Form):
    '''Form to change user password'''
    
    email = forms.EmailField(max_length=50, required=True, label='Email', widget=forms.EmailInput(attrs={
        'placeholder': 'Enter your email', 
        'class': 'input-field',
        'readonly': True,
    }))
    
    password = forms.CharField(max_length=30, min_length=8, required=True, label='Password', widget=forms.PasswordInput(attrs={
        'placeholder': 'Ex. Johndoe@123',
        'class': 'input-field',
    }))
    
    password2 = forms.CharField(max_length=30, min_length=8, required=True, label='Confirm zPassword', widget=forms.PasswordInput(attrs={
        'placeholder': 'Ex. Johndoe@123',
        'class': 'input-field',
    }))