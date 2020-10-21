from django.urls import path

from . import views

app_name = 'web'

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about_me, name='about_me'),
    path('contact', views.contact, name='contact'),
    path('portfolio', views.portfolio, name='portfolio'),
    path('media/thumb/<parent_folder>/<image_name>', views.get_thumb_image, name='get_thumb_image'),
    path('media/large/<parent_folder>/<image_name>', views.get_large_image, name='get_large_image'),
]
