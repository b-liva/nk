from django.shortcuts import render, redirect
from recipient.forms import (RecipientModelForm,)
from recipient.models import Recipient
from case.models import Illness
from case.forms import IllnessModelForm


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

