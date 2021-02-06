from django.shortcuts import render, redirect, get_object_or_404
from PlazaApp.models import Setting, ContactForm, ContactMessage 
from Service.models import Services
from Construct.models import ConstructionProjects
from Blog.models import BlogGrid
def Home(request):
    setting = get_object_or_404(Setting, id = 1)
    constructionPro = ConstructionProjects.objects.all().order_by('id')[:4]
    services = Services.objects.all().order_by('-id')[:4]
    recentNews = BlogGrid.objects.all().order_by('-id')[:3]
    context = {'setting': setting, 'constructionPro': constructionPro, 'services':services, 'recentNews':recentNews}
    return render(request, 'base.html', context)

def ContactView(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = ContactMessage()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()

            return redirect('ContactView')
    
    form = ContactForm
    setting = Setting.objects.get(id=1)

    context = {
        'form': form,
        'setting': setting,
    }
    return render(request, 'contact.html', context)


def AllProjects(request):
    setting = get_object_or_404(Setting, id=1)
    allPro = ConstructionProjects.objects.all()
    context = {'setting': setting, 'allPro': allPro}
    return render(request, 'allprojects.html', context)


def Project(request, id):
    setting = get_object_or_404(Setting, id=1)
    constructionPro = get_object_or_404(ConstructionProjects, id=id)
    context = {'setting': setting, 'constructionPro': constructionPro}
    return render(request, 'project.html', context)

def Aboutus(request):
    setting = get_object_or_404(Setting, id=1)
    service = Services.objects.all().order_by('-id')[:4]
    context = {'setting': setting, 'service': service}
    return render(request, 'aboutview.html', context)




