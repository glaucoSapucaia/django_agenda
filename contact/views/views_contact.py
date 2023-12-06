from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from contact import models

def index(request):
    contacts = models.Contact.objects.filter(show=True).order_by('-id')
    context = {
        'contacts': contacts,
        'site_title': 'Contatos -'
    }
    return render(
        request,
        'contact/index.html',
        context,
    )

def contact(request, contact_id):
    single_contact = get_object_or_404(models.Contact.objects, pk=contact_id, show=True)
    site_title = f'{single_contact.first_name} {single_contact.last_name} -'
    context = {
        'contact': single_contact,
        'site_title': site_title,
    }
    return render(
        request,
        'contact/contact.html',
        context
    )

def search(request):
    search_value = request.GET.get('q', '')
    search_context = f'Busca por "{search_value}" -'
    if search_value == '':
        return redirect('contact:index')
    
    contacts = models.Contact.objects.filter(
        Q(first_name__icontains=search_value) |
        Q(last_name__icontains=search_value) |
        Q(phone__icontains=search_value) |
        Q(email__icontains=search_value),
        show=True,
    ).order_by('-id')

    context = {
        'contacts': contacts,
        'site_title': search_context,
    }

    return render(
        request,
        'contact/index.html',
        context,
    )