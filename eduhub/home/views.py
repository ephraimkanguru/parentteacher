from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Homepage view
def homepage(request):
    return render(request, 'home/index.html')  # Render index.html for login

# Login view
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('chatbox')  # Redirect to chatbox after successful login
        else:
            messages.error(request, 'Invalid username or password')
    else:
        form = AuthenticationForm()

    return render(request, 'home/index.html', {'form': form})  # Render index.html for login

# Logout view
def user_logout(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logging out

# Signup view
def user_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('chatbox')  # Redirect to chatbox after successful signup
    else:
        form = UserCreationForm()

    return render(request, 'home/signup.html', {'form': form})  # Render signup.html for signup

# Chatbox view
@login_required  # Ensure only logged-in users can access the chatbox
def chatbox(request):
    return render(request, 'home/chatbox.html')  # Render the chatbox template
