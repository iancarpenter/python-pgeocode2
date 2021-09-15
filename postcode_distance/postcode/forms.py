from django import forms

MEASUREMENT_UNITS = [
    ('KM', 'km'),
    ('M', 'miles'),
] 

class PostcodeForm(forms.Form):
    start_postcode = forms.CharField(max_length=4)
    end_postcode = forms.CharField(max_length=4)
    distance_unit = forms.ChoiceField(choices=MEASUREMENT_UNITS, label='Distance in', widget=forms.RadioSelect(choices=MEASUREMENT_UNITS)  )