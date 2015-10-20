from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'delete-contact/(?P<contact_id>[0-9]+)$', views.delete_contact,
        name="delete-contact"),
    url(r'$', views.contacts, name="contacts"),
]
