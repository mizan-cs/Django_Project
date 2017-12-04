from django import forms

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime


class UserInput(forms.Form):
    name = forms.CharField(max_length=50,help_text="Enter your valid name")

    def clean_renewal_data(self):
        data = self.cleaned_data['name']

        if data is None:
            raise ValidationError(_('Invalid Name '))

        return data