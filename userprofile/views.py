# coding=utf-8
from django.shortcuts import render, redirect
from django.contrib import messages
import django.contrib.auth
from django.views.generic.base import View
from django.utils.translation import ugettext as _

from .forms import LoginForm

from .models import UserProfile


class LogoutView(View):
    def get(self, request):
        django.contrib.auth.logout(request)
        messages.add_message(
            request, messages.SUCCESS, _("Logout successful"))
        return redirect('index')


class LoginView(View):

    def get(self, request):
        login_form = LoginForm()
        return render(request, 'registration/login.html', locals())

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = django.contrib.auth.authenticate(**form.cleaned_data)
            if user:
                django.contrib.auth.login(request, user)
                return redirect('index')
        messages.add_message(
            request, messages.ERROR, _("E-mail or password incorrect"))
        return redirect("login")
