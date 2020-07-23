from django.shortcuts import render, redirect
from commitment.models import Commitment
from commitment.forms import CommitmentModelForm
# Create your views here.


def create(request):
    if request.method == 'POST':
        form = CommitmentModelForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('commitment:create')
    else:
        form = CommitmentModelForm()

    commitments = Commitment.objects.all()
    context = {
        'form': form,
        'commitments': commitments
    }
    return render(request, 'commitment/create.html', context)


def index(request):
    commitments = Commitment.objects.all()
    context = {
        'commitments': commitments
    }
    return render(request, 'commitment/index.html', context)
