from contact import forms
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from contact import models

def create(request):
    form = forms.ContactForm()
    form_action = reverse('contact:create')

    if request.method == 'POST':
        form = forms.ContactForm(request.POST)
        context = {
            'form': form,
            'site_title': 'Criar contato -',
            'form_action': form_action,
        }
        if form.is_valid():
            contact = form.save()
            return redirect('contact:update', contact_id=contact.id)

        return render(
            request,
            'contact/create.html',
            context,
        )

    context = {
        'form': form,
        'site_title': 'Criar contato -',
        'form_action': form_action,
    }

    return render(
        request,
        'contact/create.html',
        context,
    )

def update(request, contact_id):
    contact = get_object_or_404(models.Contact.objects, pk=contact_id, show=True)
    form_action = reverse('contact:update', args=(contact_id, ))
    form = forms.ContactForm(instance=contact)

    if request.method == 'POST':
        form = forms.ContactForm(request.POST, instance=contact)
        context = {
            'form': form,
            'site_title': 'Atualizar contato -',
            'form_action': form_action,
        }
        if form.is_valid():
            contact = form.save()
            return redirect('contact:update', contact_id=contact.id)

        return render(
            request,
            'contact/create.html',
            context,
        )

    context = {
        'form': form,
        'site_title': 'Atualizar contato -',
        'form_action': form_action,
    }

    return render(
        request,
        'contact/create.html',
        context,
    )

def delete(request, contact_id):
    contact = get_object_or_404(models.Contact.objects, pk=contact_id, show=True)
    confirmation = request.POST.get('confirmation', 'no')
    context = {
        'contact': contact,
        'confirmation': confirmation,
        'site_title': 'Deletar contato -'
    }
    if confirmation == 'yes':
        contact.delete()
        return redirect('contact:index')
    
    return render(
        request,
        'contact/contact.html',
        context,
    )