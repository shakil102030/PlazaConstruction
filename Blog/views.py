from django.shortcuts import render, get_object_or_404
from Blog.models import BlogGrid
from PlazaApp.models import Setting
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def BlogView(request):
    bloggrid = BlogGrid.objects.all()
    recentpost = BlogGrid.objects.all().order_by('-id')[:3]
    setting = get_object_or_404(Setting, id=1)
    paginator = Paginator(bloggrid, 3) # Show 3 images per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'setting': setting,
        'recentpost':recentpost,
        'page_obj':page_obj,
        }
    return render(request, 'blogview.html', context)

