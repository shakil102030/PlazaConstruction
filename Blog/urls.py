from django.urls import path
from Blog.views import BlogView

urlpatterns = [
  path('', BlogView, name = 'BlogView'),
]