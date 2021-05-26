from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from .forms import UserCreationForm, ProfileForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Profile

class Login(LoginView):
    template_name = 'accounts/auth.html'

    def form_valid(self, form):
        return super().form_valid(form)

    def form_invalid(self,form):
        return super().form_invalid(form)

class Logout(LogoutView):
    template_name = 'accounts/auth.html'

def signup(request):
    if request.method == 'POST':
        form_user = UserCreationForm(request.POST)
        if form_user.is_valid():
            user = form_user.save(commit=False)
            user.save()
            login(request, user)
            return redirect('/characters/index')
    return render(request, 'accounts/auth.html')

@login_required
def mypage(request):
    form = ProfileForm()


    if request.method == 'POST':
        form_profile = ProfileForm(request.POST)
        if form_profile.is_valid():
            profile = form_profile.save(commit=False)
            profile.user = request.user
            profile.save()
    return render(request, 'accounts/mypage.html', context={'form': form})