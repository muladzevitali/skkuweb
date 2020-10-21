from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm


def index(request):
    return render(request, 'index.html', {'category': 'home'})


def about_me(request):
    return render(request, 'about.html', {'category': 'about'})


def contact(request):
    form = ContactForm(request.POST)
    success_send = request.session.pop('mail_sending_success', False)

    if request.method == 'POST' and form.is_valid():
        subject = f'Contact from {form.cleaned_data["name"]}'
        message = 'You have a new message from: %s \n %s' % (form.cleaned_data['email'], form.cleaned_data['message'])
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['muladzevitali@gmail.com', ]
        send_mail(subject, message, email_from, recipient_list)
        request.session['mail_sending_success'] = True

        return redirect('web:contact')

    return render(request, 'contact.html', {'category': 'contact', 'form': form, 'success': success_send})
