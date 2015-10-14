from django.db import models


class Contact(models.Model):
    """
        Represents a single person that can be contacted by our app.
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=32)

    def __unicode__(self):
        return '<Contact {0} {1} {2}>'.format(self.first_name,
                                              self.last_name,
                                              self.phone_number)
