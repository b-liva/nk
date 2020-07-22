from django.shortcuts import render, redirect
from supporter.forms import SupporterForm
from supporter.models import Supporter
# Create your views here.


def create(request):
    print('hi')
    if request.method == 'POST':
        form = SupporterForm(request.POST or None)
        if form.is_valid():
            supporter = form.save(commit=False)
            supporter.save()
            return redirect('supporter:create')
    else:
        form = SupporterForm()

    supporters = Supporter.objects.all()
    context = {
        'form': form,
        'supporters': supporters
    }
    return render(request, 'supporter/create.html', context)


def index(request):
    supporters = Supporter.objects.all()
    context = {
        'supporters': supporters,
    }
    return render(request, 'supporter/index.html', context)