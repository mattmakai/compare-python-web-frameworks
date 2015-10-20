from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from .forms import ContactForm
from .models import Contact


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
