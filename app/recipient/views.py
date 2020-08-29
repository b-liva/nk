from django.shortcuts import render, redirect, get_object_or_404
from recipient.forms import (RecipientModelForm,)
from recipient.models import Recipient
from case.models import Illness
from case.forms import IllnessModelForm


# Create your views here.
def edit_or_create(request, recipient_pk=None):
    if recipient_pk:
        recipient = get_object_or_404(Recipient, pk=recipient_pk)
    else:
        recipient = Recipient()

    if request.method == 'POST':
        form = RecipientModelForm(request.POST or None, instance=recipient)
        if form.is_valid():
            form.save()
            return redirect('recipient:create_recipient')
    else:
        form = RecipientModelForm(instance=recipient)

    recipients = Recipient.objects.all()
    context = {
        'recipients': recipients,
        'form': form
    }
    return render(request, 'recipient/recipient/edit_or_create.html', context)


def index_recipients(request):
    recipients = Recipient.objects.all()
    context = {
        'recipients': recipients,
    }
    return render(request, 'recipient/recipient/index.html', context)


def details(request, recipient_pk):
    recipient = get_object_or_404(Recipient, pk=recipient_pk)
    context = {
        'recipient': recipient
    }
    return render(request, 'recipient/recipient/details.html', context)
