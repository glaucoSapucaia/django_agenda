from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.db.models import Q
from contact import models
from django.contrib import messages

def index(request):
    contacts = models.Contact.objects.filter(show=True).order_by('-id')
    paginator = Paginator(contacts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
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
    search_value = request.GET.get('q', '').strip()
    search_context = f'Busca por "{search_value}" -'
    if search_value == '':
        messages.info(request, 'Você não buscou por nada!')
        return redirect('contact:index')
    
    contacts = models.Contact.objects.filter(
        Q(first_name__icontains=search_value) |
        Q(last_name__icontains=search_value) |
        Q(phone__icontains=search_value) |
        Q(email__icontains=search_value),
        show=True,
    ).order_by('-id')

    paginator = Paginator(contacts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'site_title': search_context,
        'search_value': search_value,
    }

    return render(
        request,
        'contact/index.html',
        context,
    )