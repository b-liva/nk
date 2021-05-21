from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from commitment.models import Commitment
from commitment.forms import CommitmentModelForm
from commitment.filters import CommitmentFilter
# Create your views here.
from supporter.models import Supporter


def edit_or_create(request, commitment_pk=None):
    if commitment_pk:
        commitment = get_object_or_404(Commitment, pk=commitment_pk)
    else:
        commitment = Commitment()
    if request.method == 'POST':
        form = CommitmentModelForm(request.POST or None, instance=commitment)
        if form.is_valid():
            cm = form.save(commit=False)
            cm.supporter = get_object_or_404(Supporter, pk=request.POST.get('su_value'))
            cm.save()
            return redirect('commitment:create')
    else:
        form = CommitmentModelForm(instance=commitment)

    commitments = Commitment.objects.all()
    paginator = Paginator(commitments, 50)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'form': form,
        'page_obj': page_obj
    }

    if 'su_value' in request.POST:
        context['supporter'] = Supporter.objects.get(pk=request.POST.get('su_value'))

    return render(request, 'commitment/edit_or_create.html', context)


def index(request):
    commitments = Commitment.objects.all()
    f = CommitmentFilter(request.GET, commitments)
    paginator = Paginator(f.qs, 50)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'filter': f,
        'page_obj': page_obj
    }
    return render(request, 'commitment/index.html', context)


def details(request, commitment_pk):
    commitment = get_object_or_404(Commitment, pk=commitment_pk)
    context = {
        'commitment': commitment
    }
    return render(request, 'commitment/details.html', context)
