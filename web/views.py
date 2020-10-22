from pathlib import Path

from PIL import Image
from django.conf import settings
from django.core.mail import (send_mail, EmailMessage)
from django.http import HttpResponse
from django.shortcuts import (render, redirect)

from .forms import (ContactForm, PresetForm)
from .models import (Contact, Preset, Notice)

RECIPIENT_LIST = settings.RECIPIENT_LIST
EMAIL_FROM = settings.EMAIL_HOST_USER
THUMBNAIL_IMAGE_WIDTH = (1200, 1150)


def index(request):
    slider_images = [Path('slider').joinpath(path.name) for path in
                     settings.SLIDER_IMAGES_FOLDER.iterdir()]
    return render(request, 'index.html', {'category': 'home', 'slider_images': slider_images})


def about_me(request):
    return render(request, 'about.html', {'category': 'about'})


def contact(request):
    form = ContactForm(request.POST)
    success_send = request.session.pop('mail_sending_success', False)

    if request.method == 'POST' and form.is_valid():
        name = form.cleaned_data["name"]
        email = form.cleaned_data['email']
        message = form.cleaned_data['message']

        subject = 'Contact from %s' % name
        body = 'You have a new message from: %s \n %s' % (email, message)
        send_mail(subject, body, EMAIL_FROM, RECIPIENT_LIST)

        request.session['mail_sending_success'] = True
        contact_log = Contact(name=name, message=message, email=email)
        contact_log.save()

        return redirect('web:contact')

    return render(request, 'contact.html', {'category': 'contact', 'form': form, 'success': success_send})


def portfolio(request, subclass):
    portfolio_images = [Path('media', 'thumb', path.parent.parent.name, path.parent.name, path.name) for path in
                        settings.PORTFOLIO_IMAGES_ROOT.joinpath(subclass).iterdir()]

    return render(request, 'gallery.html',
                  {'category': 'portfolio', 'images_paths': portfolio_images, 'subclass': subclass})


def get_thumb_image(request, class_folder, parent_folder, image_name):
    image_path = settings.IMAGES_FOLDER_ROOT.joinpath(class_folder).joinpath(parent_folder).joinpath(image_name)
    response = HttpResponse(content_type="image/jpeg")
    try:
        image = Image.open(image_path)
        image.thumbnail(THUMBNAIL_IMAGE_WIDTH, Image.ANTIALIAS)

        image.save(response, "JPEG")
    except IOError:
        red = Image.new('RGBA', (1, 1), (255, 0, 0, 0))
        red.save(response, "JPEG")

    return response


def get_large_image(request, class_folder, image_name, parent_folder=None):
    if parent_folder:
        image_path = settings.IMAGES_FOLDER_ROOT.joinpath(class_folder).joinpath(parent_folder).joinpath(image_name)
    else:
        image_path = settings.IMAGES_FOLDER_ROOT.joinpath(class_folder).joinpath(image_name)
    try:
        with open(str(image_path), "rb") as input_stream:
            image = input_stream.read()
    except IOError:
        red = Image.new('RGBA', (1, 1), (255, 0, 0, 0))
        response = HttpResponse(content_type="image/jpeg")
        red.save(response, "JPEG")

        return response

    return HttpResponse(image, content_type="image/jpeg")


def get_slider_image(request, image_name):
    image_path = settings.SLIDER_IMAGES_FOLDER.joinpath(image_name)
    response = HttpResponse(content_type="image/jpeg")
    try:
        image = Image.open(image_path)
        image.thumbnail((1708, 1140), Image.ANTIALIAS)

        image.save(response, "JPEG")
    except IOError:
        red = Image.new('RGBA', (1, 1), (255, 0, 0, 0))
        red.save(response, "JPEG")

    return response


def presets(request):
    form = PresetForm(request.POST)
    if request.method == 'POST' and form.is_valid():
        preset = Preset.objects.get(pk=form.cleaned_data['preset_id'])
        print(form.cleaned_data, preset.file_path)
        email = EmailMessage()
        email.subject = '%s from skkuweb3' % preset.title
        email.to = [form.cleaned_data['email'], ]
        email.from_email = settings.EMAIL_HOST_USER
        preset_file_path = settings.PRESETS_ROOT.joinpath(preset.file_path)
        email.attach_file(preset_file_path)
        email.body = preset.description or ''
        email.send()

        return redirect('web:presets')
    return render(request, 'presets.html', {'category': 'presets', 'presets': Preset.objects.all()})


def notices(request):
    notices_ = Notice.objects.order_by('date').all()
    return render(request, 'notices.html', {'category': 'notices', 'notices': notices_})
