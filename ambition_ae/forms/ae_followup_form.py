from django import forms
from edc_base.sites.forms import SiteModelFormMixin
from edc_constants.constants import YES, DEAD
from edc_form_validators import FormValidatorMixin, FormValidator

from ..constants import SEVERITY_INCREASED_FROM_G3, GRADE5
from ..models import AeFollowup
from .modelform_mixin import ModelFormMixin


class AeFollowupFormValidator(FormValidator):

    def clean(self):

        self.applicable_if(
            SEVERITY_INCREASED_FROM_G3,
            field='outcome', field_applicable='ae_grade')

        self.applicable_if(
            SEVERITY_INCREASED_FROM_G3,
            field='outcome', field_applicable='ae_grade')


class AeFollowupForm(FormValidatorMixin, ModelFormMixin,
                     forms.ModelForm):

    form_validator_cls = AeFollowupFormValidator

    action_identifier = forms.CharField(
        label='Action Identifier',
        required=False,
        widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    subject_identifier = forms.CharField(
        label='Subject Identifier',
        required=False,
        widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get('followup') == YES:
            if (cleaned_data.get('ae_grade') == GRADE5
                    or cleaned_data.get('outcome') == DEAD):
                raise forms.ValidationError({
                    'followup': (
                        'Expected No. Submit a death report when the '
                        'severity increases to grade 5.')})

        return cleaned_data

    class Meta:
        model = AeFollowup
        fields = '__all__'
