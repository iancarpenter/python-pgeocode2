from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

MEASUREMENT_UNITS = [
    ('KM', 'km'),
    ('M', 'miles'),
] 

class PostcodeForm(forms.Form):
    start_postcode = forms.CharField(
        max_length= 4,
        required = True,
        label = "Enter the starting postcode"
    )
    end_postcode = forms.CharField(
        max_length = 4,
        required = True,
        label = "Enter the ending postcode"
    )
    distance_unit = forms.ChoiceField(
        choices=MEASUREMENT_UNITS, 
        label='Distance in', 
        widget=forms.RadioSelect(choices=MEASUREMENT_UNITS), initial='KM'  
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'form'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = ''

        self.helper.add_input(Submit('submit', 'Submit'))