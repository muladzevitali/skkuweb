from django.urls import path

from . import views

app_name = 'web'

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about_me, name='about_me'),
    path('contact', views.contact, name='contact'),
]
