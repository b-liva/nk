from django.shortcuts import render, redirect, get_object_or_404
from supporter.forms import SupporterForm
from supporter.models import Supporter
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
    context = {
        'supporter': supp,
    }
    return render(request, 'supporter/details.html', context)
