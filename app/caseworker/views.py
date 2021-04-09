from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from caseworker.models import CaseWorker
from caseworker.forms import CaseWorkerModelForm
from caseworker.filters import CwFilter
# Create your views here.
from supporter.models import Supporter


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
    paginator = Paginator(cws, 15)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'form': form,
        'page_obj': page_obj
    }
    return render(request, 'caseworker/edit_or_create.html', context)


def index(request):
    cws = CaseWorker.objects.all()
    f = CwFilter(request.GET, cws)
    paginator = Paginator(f.qs, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'filter': f,
        'caseworkers': f.qs,
        'page_obj': page_obj
    }
    return render(request, 'caseworker/index.html', context)


def details(request, cw_pk):
    caseworker = get_object_or_404(CaseWorker, pk=cw_pk)
    supporters = caseworker.supporter_set.all()
    context = {
        'caseworker': caseworker,
        'supporters': supporters
    }
    return render(request, 'caseworker/details.html', context)