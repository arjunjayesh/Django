from . import views
from django.urls import path, include

urlpatterns = [
    path('',views.demo),
    path('home',views.home,name='home'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('details',views.details,name='details'),
    path('thanks',views.thanks,name='thanks'),
    path('cal',views.calc,name='cal'),
    path('res',views.result,name='calcresult'),
]