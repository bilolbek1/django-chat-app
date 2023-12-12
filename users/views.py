from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from .forms import SignUpForm, ProfileForm


class SignUpView(View):
    def get(self, request):
        signup_form = SignUpForm()
        context = {
            'signup_form': signup_form,
        }
        return render(request, 'register/signup.html', context)

    def post(self, request):
        signup_form = SignUpForm(data=request.POST)

        if signup_form.is_valid():
            signup_form.save()

            return redirect('login')
        else:
            context = {
                'signup_form': signup_form
            }
            return render(request, 'register/signup.html', context)



class LoginView(View):
    def get(self, request):
        login_form = AuthenticationForm()
        context = {
            'login_form': login_form,
        }
        return render(request, 'register/login.html', context)

    def post(self, request):
        login_form = AuthenticationForm(data=request.POST)

        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)

            messages.success(request, 'You have successfully logged in')
            return redirect('home')

        else:
            context = {
                'login_form': login_form
            }
            return render(request, 'register/login.html', context)





class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user
        context = {
            'user': user
        }
        return render(request, 'register/profile.html', context)



class UpdateProfileView(LoginRequiredMixin, View):
    def get(self, request):
        update_profile_form = ProfileForm(instance=request.user)
        context = {
            'profile': update_profile_form
        }
        return render(request, 'register/update_profile.html', context)

    def post(self, request):
        update_profile_form = ProfileForm(instance=request.user,
                                          data=request.POST,
                                          files=request.FILES)
        if update_profile_form.is_valid():
            update_profile_form.save()

            messages.success(request, 'Successfully updated your profile')

            return redirect('profile')

        else:
            context = {
                'profile': update_profile_form
            }
            return render(request, 'register/update_profile.html', context)


class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return redirect('login')






















































