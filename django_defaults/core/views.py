from django.http import HttpResponse
from django.shortcuts import render

from .models import Contact


def contacts(request):
    contacts = Contact.objects.all()
    return render(request, 'contacts.html', {"contacts": contacts})



