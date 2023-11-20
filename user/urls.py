from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('<slug:pk>/', views.UserProfileView.as_view(), name='profile'),
    path('<slug:pk>/edit/', views.EditProfileView.as_view(), name='edit-profile'),
]