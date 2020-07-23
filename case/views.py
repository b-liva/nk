from django.shortcuts import render, redirect
from case.forms import IllnessModelForm, CaseModelForm
from case.models import Illness, Case
# Create your views here.


def create_case(request):
    if request.method == 'POST':
        form = CaseModelForm(request.POST or None)
        form.save()
        return redirect('case:create_case')
    else:
        form = CaseModelForm()
    cases = Case.objects.all()
    context = {
        'form': form,
        'cases': cases
    }
    return render(request, 'case/case/create.html', context)


def index_case(request):
    cases = Case.objects.all()
    context = {
        'cases': cases
    }
    return render(request, 'case/case/index.html', context)


def create_illness(request):
    if request.method == 'POST':
        form = IllnessModelForm(request.POST or None)
        form.save()
        return redirect('case:create_illness')
    else:
        form = IllnessModelForm()
    illnesses = Illness.objects.all()
    context = {
        'form': form,
        'illnesses': illnesses
    }
    return render(request, 'case/illness/create.html', context)


def index_illnesses(request):
    illnesses = Illness.objects.all()
    context = {
        'illnesses': illnesses
    }
    return render(request, 'case/illness/index.html', context)
