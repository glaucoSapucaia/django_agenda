from django.shortcuts import render, redirect
from django.contrib import messages
from contact import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth

def register(request):
    form = forms.RegisterForm()
    if request.method == 'POST':
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuário registrado!')
            return redirect('contact:login')
        messages.error('Verifique os dados do usuário!')
    
    context = {
        'site_title': 'Registrar -',
        'form': form,
    }

    return render(
        request,
        'contact/register.html',
        context,
    )

def login_view(request):
    form = AuthenticationForm(request)
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth.login(request, user=user)
            messages.success(request, 'Você entrou =)')
            return redirect('contact:index')
        messages.error(request, 'Login inválido!')

    context = {
        'site_title': 'Autenticação -',
        'form': form,
    }

    return render(
        request,
        'contact/login.html',
        context,
    )

def logout_view(request):
    auth.logout(request)
    messages.success(request, 'Você saiu =)')
    return redirect('contact:login')