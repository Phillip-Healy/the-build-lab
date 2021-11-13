""" form control for interactions app """
from django import forms
from django.core.exceptions import ValidationError


class FutureRequest(forms.Form):
    """ Form control to take in future content ideas """
    content_request = forms.Textarea()

    def clean_future_request(self):
        """ Form control to sanitise data """
        data = self.cleaned_data['content_request']

        # Check if string is empty
        if data.length() <= 0:
            raise ValidationError('Add some ideas before sending an empty form!')

        return data
