from django.shortcuts import render, redirect
from recipient.forms import (RecipientModelForm, IllnessModelForm,)
from recipient.models import Recipient, Illness


# Create your views here.
def create_recipient(request):
    if request.method == 'POST':
        form = RecipientModelForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('recipient:create_recipient')
    else:
        form = RecipientModelForm()

    recipients = Recipient.objects.all()
    context = {
        'recipients': recipients,
        'form': form
    }
    return render(request, 'recipient/recipient/create.html', context)


def index_recipients(request):
    recipients = Recipient.objects.all()
    context = {
        'recipients': recipients,
    }
    return render(request, 'recipient/recipient/index.html', context)


def create_illness(request):

    if request.method == 'POST':
        form = IllnessModelForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('recipient:create_illness')
    else:
        form = IllnessModelForm()

    illnesses = Illness.objects.all()
    context = {
        'illnesses': illnesses,
        'form': form
    }
    return render(request, 'recipient/illness/create.html', context)


def index_illness(request):
    illnesses = Illness.objects.all()
    context = {
        'illnesses': illnesses,
    }
    return render(request, 'recipient/illness/index.html', context)
