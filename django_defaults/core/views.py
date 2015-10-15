from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import ContactForm
from .models import Contact


def contacts(request):
    if request.method == 'GET':
        contacts = Contact.objects.all()
        form = ContactForm()
        return render(request, 'contacts.html', {"contacts": contacts,
                                                 'form': form})
    elif request.method == 'POST':
        # form handling code
        return redirect('core:contacts')


