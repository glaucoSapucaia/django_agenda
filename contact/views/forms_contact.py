from contact import forms
from django.shortcuts import render

def create(request):
    if request.method == 'POST':
        context = {
            'form': forms.ContactForm(request.POST),
            'site_title': 'Criar contato -',
        }

        return render(
            request,
            'contact/create.html',
            context,
        )

    context = {}

    return render(
        request,
        'contact/create.html',
        context,
    )