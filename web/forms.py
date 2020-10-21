from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(min_length=4)
    email = forms.EmailField()
    message = forms.CharField(min_length=1, max_length=10000)
