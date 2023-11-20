from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView, UpdateView
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from .forms import LoginForm, SignUpForm, EditDetailsForm, ChangePasswordForm
from .utility_functions import get_year, is_strong_password

User = get_user_model()

context = {
    'year': get_year()
}

class LoginView(View):
    '''View to login users'''
    
    def get(self, request):
        form = LoginForm()
        context['form'] = form
        context['page_title']= 'Login'
        
        return render(request, 'user/login.html', context)
    
    def post(self, request):
        form = LoginForm(request.POST)
        
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            user = authenticate(email=email, password=password)
            
            if user is not None:
                login(request, user=user)
                messages.success(request, f'Welcome {user.first_name}')
                return redirect(reverse_lazy('screentrackapp:home'))
            else:
                messages.error(request, 'Invalid login credentials.')
                
            context['form'] = form
            context['page_title']= 'Login'
            return render(request, 'user/login.html', context)
        

class SignUpView(View):
    '''View to sign up users'''
    
    def get(self, request):
        form = SignUpForm()
        context['form'] = form
        context['page_title']= 'Sign Up'
        
        return render(request, 'user/signUp.html', context)
    
    def post(self, request):
        form = SignUpForm(request.POST)
        
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            password2 = form.cleaned_data['password2']
            
            # Validation Checks
            # ---------------------------------------- #
            
            # Check password match
            if password != password2:
                messages.error(request, 'Your passwords do not match.')
            else:
                # Check password strength
                if not is_strong_password(password) or not is_strong_password(password2):
                    messages.error(request, 'Password is not strong enough. Your password must have at least 8 characters consisting of uppercase, lowercase and special characters')
                else:
                    # Check database if a user with the email entered already exists
                    user_check = User.objects.filter(email=email)
                    if user_check.exists():
                        messages.error(request, 'This email is already in use. Pick another email.')
                    else:
                        # Save user in database
                        user = User.objects.create(
                            first_name = first_name,
                            last_name = last_name,
                            email = email,
                            password = password,
                        )
                        
                        user.save()
                        
                        # Login the user direcyly
                        login(request, user=user)
                        messages.success(request, 'Account created successfully.')
                        return redirect(reverse_lazy('screentrackapp:home'))
                        
            context['form'] = form
            context['page_title']= 'Sign Up'
            return render(request, 'user/signup.html', context)

    
class UserProfileView(LoginRequiredMixin, DetailView):
    '''View to get user details'''
    
    login_url = 'user:login'
    
    model = User
    template_name = 'user/profile.html'
    context_object_name = 'user'
    
    def get(self, request, pk):
        context['page_title'] = 'Profile'
        return render(request, self.template_name, context)
    

class EditProfileView(LoginRequiredMixin, View):
    '''View to edit user details'''
    
    login_url = 'user:login'
    
    def get(self, request, pk):
        # Get current logged in user
        user = request.user
        initial_data = {
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
        }
        
        # Populate form fields with data
        form = EditDetailsForm(initial=initial_data)
        
        context['form'] = form
        context['page_title'] = 'Edit Profile'
        
        return render(context, 'user/edit-profile.html', context)
    

def logout_view(request):
    '''View to logout users'''
    
    logout(request)
    messages.success(request, 'Logout successful.')
    return redirect(reverse_lazy('user:login'))