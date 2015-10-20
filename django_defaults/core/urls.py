from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'delete-contact/(?P<contact_id>[0-9]+)$', views.delete_contact,
        name="delete-contact"),
    url(r'call/(?P<contact_id>[0-9]+)$', views.call, name="call-contact"),
    url(r'conference-twiml$', views.conference_twiml, name="conference-twiml"),
    url(r'$', views.contacts, name="contacts"),
]
