from django.shortcuts import render, redirect, get_object_or_404
from case.forms import IllnessModelForm, CaseModelForm
from case.models import Illness, Case
# Create your views here.


def edit_or_create_case(request, case_pk=None):
    if case_pk:
        case = get_object_or_404(Case, pk=case_pk)
    else:
        case = Case()
    if request.method == 'POST':
        form = CaseModelForm(request.POST or None, instance=case)
        form.save()
        return redirect('case:create_case')
    else:
        form = CaseModelForm(instance=case)
    cases = Case.objects.all()
    context = {
        'form': form,
        'cases': cases
    }
    return render(request, 'case/case/edit_or_create.html', context)


def index_case(request):
    cases = Case.objects.all()
    context = {
        'cases': cases
    }
    return render(request, 'case/case/index.html', context)


def case_details(requests, case_pk):
    case = Case.objects.get(pk=case_pk)
    context = {
        'case': case,
    }
    return render(requests, 'case/case/details.html', context)


def edit_or_create_illness(request, illness_pk=None):
    if illness_pk:
        illness = get_object_or_404(Illness, pk=illness_pk)
    else:
        illness = Illness()
    if request.method == 'POST':
        form = IllnessModelForm(request.POST or None, instance=illness)
        form.save()
        return redirect('case:create_illness')
    else:
        form = IllnessModelForm(instance=illness)
    illnesses = Illness.objects.all()
    context = {
        'form': form,
        'illnesses': illnesses
    }
    return render(request, 'case/illness/edit_or_create.html', context)


def index_illnesses(request):
    illnesses = Illness.objects.all()
    context = {
        'illnesses': illnesses
    }
    return render(request, 'case/illness/index.html', context)


def illness_details(request, illness_pk):
    illness = get_object_or_404(Illness, pk=illness_pk)
    context = {
        'illness': illness
    }
    return render(request, 'case/illness/details.html', context)
