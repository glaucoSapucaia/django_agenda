from django.shortcuts import render, redirect
from contact import forms

def register(request):
    form = forms.RegisterForm()
    if request.method == 'POST':
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact:index')
    
    context = {
        'site_title': 'Registrar -',
        'form': form,
    }

    return render(
        request,
        'contact/register.html',
        context,
    )