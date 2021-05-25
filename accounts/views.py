from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from .forms import UserCreationForm
from django.contrib.auth import login

class Login(LoginView):
    template_name = 'accounts/login.html'

    def form_valid(self, form):
        return super().form_valid(form)

    def form_invalid(self,form):
        return super().form_invalid(form)

class Logout(LogoutView):
    template_name = 'accounts/logout.html'

def signup(request):
    if request.method == 'POST':
        form_user = UserCreationForm(request.POST)
        if form_user.is_valid():
            user = form_user.save(commit=False)
            user.save()
            login(request, user)
            return redirect('/characters/index')
    return render(request, 'accounts/auth.html')