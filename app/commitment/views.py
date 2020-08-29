from django.shortcuts import render, redirect, get_object_or_404
from commitment.models import Commitment
from commitment.forms import CommitmentModelForm
# Create your views here.


def edit_or_create(request, commitment_pk=None):
    if commitment_pk:
        commitment = get_object_or_404(Commitment, pk=commitment_pk)
    else:
        commitment = Commitment()
    if request.method == 'POST':
        form = CommitmentModelForm(request.POST or None, instance=commitment)
        if form.is_valid():
            form.save()
            return redirect('commitment:create')
    else:
        form = CommitmentModelForm(instance=commitment)

    commitments = Commitment.objects.all()
    context = {
        'form': form,
        'commitments': commitments
    }
    return render(request, 'commitment/edit_or_create.html', context)


def index(request):
    commitments = Commitment.objects.all()
    context = {
        'commitments': commitments
    }
    return render(request, 'commitment/index.html', context)


def details(request, commitment_pk):
    commitment = get_object_or_404(Commitment, pk=commitment_pk)
    context = {
        'commitment': commitment
    }
    return render(request, 'commitment/details.html', context)
