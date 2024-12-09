# home/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),  # Home page
    path('login/', views.user_login, name='login'),  # Login page
    path('logout/', views.user_logout, name='logout'),  # Logout page
    path('signup/', views.user_signup, name='signup'),  # Signup page
    path('chatbox/', views.chatbox, name='chatbox'),  # Chatbox page (protected by login_required)
]
