from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from twilio import twiml
from twilio.rest import TwilioRestClient

from .forms import ContactForm
from .models import Contact


client = TwilioRestClient()


def contacts(request):
    if request.method == 'GET':
        contacts = Contact.objects.all()
        form = ContactForm()
        return render(request, 'contacts.html', {"contacts": contacts,
                                                 'form': form})
    elif request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # save valid form object
            form.save()
            return redirect('core:contacts')
        return render(request, 'contacts.html', {"form": form})


def delete_contact(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id)
    contact.delete()
    return redirect('core:contacts')


def call(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id)
    client.calls.create(to=contact.phone_number, from_=settings.TWILIO_NUMBER,
                        url="http://twimlbin.com/external/5433e2a6577fdbf5")
    return redirect('core:contacts')


def conference_twiml(request):
    twiml_response = twiml.Response()
    twiml_response.dial().conference('pycontacts')
    return HttpResponse(str(twiml_response))

