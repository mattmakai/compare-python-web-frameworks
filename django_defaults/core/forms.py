from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from .models import Contact


class ContactForm(ModelForm):
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('Save', 'save', css_class='btn-primary'))

    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'phone_number']
