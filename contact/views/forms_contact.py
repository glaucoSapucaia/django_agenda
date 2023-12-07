from contact import forms
from django.shortcuts import render, redirect

def create(request):
    form = forms.ContactForm()

    if request.method == 'POST':
        form = forms.ContactForm(request.POST)
        context = {
            'form': form,
            'site_title': 'Criar contato -',
        }
        if form.is_valid():
            form.save()
            return redirect('contact:create')

        return render(
            request,
            'contact/create.html',
            context,
        )

    context = {
        'form': form,
        'site_title': 'Criar contato -',
    }

    return render(
        request,
        'contact/create.html',
        context,
    )