from django.urls import path
from Service.views import ServicesView, TeamView
urlpatterns = [
   path('', ServicesView, name = 'ServicesView'),
   path('team/', TeamView, name = 'TeamView'),
]