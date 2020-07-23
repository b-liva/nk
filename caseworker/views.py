from django.shortcuts import render, get_object_or_404, redirect
from caseworker.models import CaseWorker
from caseworker.forms import CaseWorkerModelForm
# Create your views here.


def edit_or_create(request, cw_pk=None):
    if cw_pk:
        cw = get_object_or_404(CaseWorker, pk=cw_pk)
    else:
        cw = CaseWorker()

    if request.method == 'POST':
        form = CaseWorkerModelForm(request.POST or None, instance=cw)
        if form.is_valid():
            form.save()
            return redirect('caseworker:create')
    else:
        form = CaseWorkerModelForm(instance=cw)

    cws = CaseWorker.objects.all()
    context = {
        'form': form,
        'caseworkers': cws
    }
    return render(request, 'caseworker/edit_or_create.html', context)


def index(request):
    cws = CaseWorker.objects.all()
    context = {
        'caseworkers': cws
    }
    return render(request, 'caseworker/index.html', context)


def details(request, cw_pk):
    caseworker = get_object_or_404(CaseWorker, pk=cw_pk)
    context = {
        'caseworker': caseworker
    }
    return render(request, 'caseworker/details.html', context)