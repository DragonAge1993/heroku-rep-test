from django.urls import path
from .import views

urlpatterns = [
    path('about/',views.About.as_view(), name = 'about'),
    path('',views.Home.as_view(), name = 'home'),
]