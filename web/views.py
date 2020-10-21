from pathlib import Path
from PIL import Image
from django.shortcuts import (render, redirect)
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse

from .forms import ContactForm
from .models import Contact

RECIPIENT_LIST = ['muladzevitali@gmail.com', ]
EMAIL_FROM = settings.EMAIL_HOST_USER
THUMBNAIL_IMAGE_WIDTH = (1200, 1150)


def index(request):
    return render(request, 'index.html', {'category': 'home'})


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


def portfolio(request):
    portfolio_images = [Path('media', 'thumb', path.parent.name, path.name) for path in
                        settings.PORTFOLIO_IMAGES_ROOT.iterdir()]

    return render(request, 'gallery.html', {'category': 'portfolio', 'images_paths': portfolio_images})


def get_thumb_image(request, parent_folder, image_name):
    image_path = settings.IMAGES_FOLDER_ROOT.joinpath(parent_folder).joinpath(image_name)
    response = HttpResponse(content_type="image/jpeg")
    try:
        image = Image.open(image_path)
        image.thumbnail(THUMBNAIL_IMAGE_WIDTH, Image.ANTIALIAS)

        image.save(response, "JPEG")
    except IOError:
        red = Image.new('RGBA', (1, 1), (255, 0, 0, 0))
        red.save(response, "JPEG")

    return response


def get_large_image(request, parent_folder, image_name):
    image_path = settings.IMAGES_FOLDER_ROOT.joinpath(parent_folder).joinpath(image_name)
    try:
        with open(str(image_path), "rb") as input_stream:
            image = input_stream.read()
    except IOError:
        red = Image.new('RGBA', (1, 1), (255, 0, 0, 0))
        response = HttpResponse(content_type="image/jpeg")
        red.save(response, "JPEG")

        return response

    return HttpResponse(image, content_type="image/jpeg")
