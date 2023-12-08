from django.shortcuts import render, redirect
from django.contrib import messages
from contact import forms

def register(request):
    form = forms.RegisterForm()
    if request.method == 'POST':
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuário registrado!')
            return redirect('contact:index')
    
    context = {
        'site_title': 'Registrar -',
        'form': form,
    }

    messages.error(request, 'Verifique seus dados!')
    return render(
        request,
        'contact/register.html',
        context,
    )