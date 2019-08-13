from django import forms
from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.urls import reverse

from studentsdb.settings import ADMIN_EMAIL


class ContactForm(forms.Form):
    from_email = forms.EmailField(label="Ваша електронна адреса")

    subject = forms.CharField(label="Заголовок листа", max_length=128)

    message = forms.CharField(label="Повідомлення", max_length=2560,
                              widget=forms.Textarea)

def contact_admin(request):

    # if from was posted
    if request.method == 'POST':
        # create a form instance and populate it with data request
        form = ContactForm(request.POST)

        # check whether data is valid
        if form.is_valid():
            # send email
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            from_email = form.cleaned_data['from_email']

            try:
                send_mail(subject, message, from_email, [ADMIN_EMAIL])
            except Exception:
                message = "Під час відправки листа виникла непередбачувана \
                помилкаю Спробуйте пізнішею"

            else:
                message = "Повідомлення надіслане"

            return HttpResponseRedirect('%s?status_message=%s' %
                                        (reverse('contact_admin'), message))

    else:
        form = ContactForm()

    return render(request, 'students/contact_admin/form.html', {'form': form})
