from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from . import models
from forms import NameForm
from django.utils import timezone
from models import Person

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            p = models.Person()
            p.your_name = request.POST['your_name']
            p.pub_date = timezone.now()
            p.save()
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

        return render(request, 'forms/name.html', {'form': form})

def thanks(request):
    return render(request, 'forms/thanks.html')

def print_users(request):
        p = Person.objects.all().order_by('pub_date')
        return render(request, 'forms/users.html', {'users':p})

"""
if form.is_valid():
    subject = form.cleaned_data['subject']
    message = form.cleaned_data['message']
    sender = form.cleaned_data['sender']
    cc_myself = form.cleaned_data['cc_myself']

    recipients = ['info@example.com']
    if cc_myself:
        recipients.append(sender)

    send_mail(subject, message, sender, recipients)
    return HttpResponseRedirect('/thanks/')
"""
"""
class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)
"""