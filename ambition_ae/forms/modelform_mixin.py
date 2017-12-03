from django import forms
from django.core.exceptions import ObjectDoesNotExist
from edc_registration.models import RegisteredSubject


class ModelformMixin:

    def clean(self):
        cleaned_data = super().clean()
        subject_identifier = cleaned_data.get('subject_identfier')
        try:
            RegisteredSubject.objects.get(
                subject_identifier=subject_identifier)
        except ObjectDoesNotExist:
            raise forms.ValidationError(
                {'subject_identifier': 'Invalid.'})
        return cleaned_data
