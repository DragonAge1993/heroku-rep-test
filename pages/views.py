from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
#def home(request):
  #  return HttpResponse("Hello World")
class Home(TemplateView):
    template_name = 'home.html'
class About(TemplateView):
    template_name = 'about.html'
# Create your views here.
