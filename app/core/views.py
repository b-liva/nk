from django.shortcuts import render
from supporter.models import FollowUp


# Create your views here.
def homepage(request):
    followup = FollowUp.objects.all().order_by('date').reverse()
    context = {
        'followup': followup
    }
    return render(request, 'core/pages/homepage.html', context)
