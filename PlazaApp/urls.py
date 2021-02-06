from django.urls import path
from PlazaApp.views import Home, Project, Aboutus, AllProjects, ContactView #, Contact, SingleProject, Aboutus, AllProjects

urlpatterns = [
    path('', Home, name = 'home'),
    path('contact/', ContactView, name = 'ContactView'),
    path('projects/', AllProjects, name = 'AllProjects'),
    path('projects/<int:id>/', Project, name = 'Project'),
    path('about/', Aboutus, name = 'aboutus'),
   
]