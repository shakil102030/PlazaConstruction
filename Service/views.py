from django.shortcuts import render, get_object_or_404
from Service.models import Services, Teams
from PlazaApp.models import Setting

def ServicesView(request):
    services = Services.objects.all()
    setting = get_object_or_404(Setting, id=1)
    context = {
        'services':services,
        'setting': setting,
        }
    return render(request, 'servicesview.html', context)

def TeamView(request):
    team = Teams.objects.all()
    setting = get_object_or_404(Setting, id=1)
    context = {
        'team': team,
        'setting': setting,
        }
    return render(request, 'teamview.html', context)

