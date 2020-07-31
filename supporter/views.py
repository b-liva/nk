from django.shortcuts import render, redirect, get_object_or_404
from supporter.forms import SupporterForm, ContactForm
from supporter.models import Supporter, Contact


# Create your views here.


def edit_or_create(request, supporter_pk=None):
    if supporter_pk:
        supp = get_object_or_404(Supporter, pk=supporter_pk)
    else:
        supp = Supporter()
    if request.method == 'POST':
        form = SupporterForm(request.POST or None, instance=supp)
        if form.is_valid():
            supporter = form.save(commit=False)
            supporter.save()
            return redirect('supporter:create')
    else:
        form = SupporterForm(instance=supp)

    supporters = Supporter.objects.all()
    context = {
        'form': form,
        'supporters': supporters
    }
    return render(request, 'supporter/edit_or_create.html', context)


def index(request):
    supporters = Supporter.objects.all()
    context = {
        'supporters': supporters,
    }
    return render(request, 'supporter/index.html', context)


def details(request, supporter_pk):
    supp = get_object_or_404(Supporter, pk=supporter_pk)
    supp.contact_set.all()
    context = {
        'supporter': supp,
    }
    return render(request, 'supporter/details.html', context)


def upsert_contact(request, supporter_pk, contact_pk=None):
    supporter = get_object_or_404(Supporter, pk=supporter_pk)
    if contact_pk:
        contact = get_object_or_404(Contact, pk=contact_pk)
        print('edit',  contact)
    else:
        contact = Contact()
        print('add...', contact)

    if request.method == 'POST':
        print('post')
        form = ContactForm(request.POST or None, instance=contact)
        if form.is_valid():
            contact_form = form.save(commit=False)
            contact_form.supporter = supporter
            contact_form.save()
            return redirect('supporter:create_contact', supporter_pk=supporter_pk)
    else:
        form = ContactForm(instance=contact)
        print('!show db')

    contacts = Contact.objects.filter(supporter=supporter)
    context = {
        'contact': contact,
        'form': form,
        'contacts': contacts,
        'supporter': supporter
    }
    print(context)
    return render(request, 'supporter/upsert_contact.html', context)
