from django.urls import path

from . import views

app_name = 'web'

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about_me, name='about_me'),
    path('contact', views.contact, name='contact'),
    path('portfolio/<subclass>', views.portfolio, name='portfolio'),
    path('portfolio/media/thumb/<class_folder>/<parent_folder>/<image_name>', views.get_thumb_image,
         name='get_thumb_image'),
    path('portfolio/media/large/<class_folder>/<parent_folder>/<image_name>', views.get_large_image,
         name='get_large_image'),
    path('portfolio/media/large/<class_folder>/<image_name>', views.get_large_image,
         name='get_large_image'),
    path('presets/<preset_id>', views.presets, name='get_preset'),
    path('presets/', views.presets, name='presets'),
]
