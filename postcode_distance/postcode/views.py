from django.shortcuts import render
from .forms import PostcodeForm
from .models import Postcode
from django.views import View
from django.template.response import TemplateResponse
import pgeocode

class PostCode(View):
    
    form = PostcodeForm

    def get(self, request, *args, **kwargs):
        form = self.form()
        return TemplateResponse(request, "postcode/postcode.html", {"form": form} )
    
    def post(self, request):

        form = PostcodeForm(request.POST)

        if form.is_valid():

            cd = form.cleaned_data

            pc = Postcode(
                start_postcode=cd['start_postcode'],
                end_postcode=cd['end_postcode'],
                result_measurement_unit=cd['distance_unit'],
            )
      
            pc.save()

            start_postcode = form['start_postcode'].value()
            
            end_postcode = form['end_postcode'].value()

            dist = pgeocode.GeoDistance('GB')

            distance_result = dist.query_postal_code(start_postcode, end_postcode)
            
            measurement_unit = 'km'

            if form['distance_unit'].value() == 'M':
                # convert to miles 
                distance_result /= 1.609
                
                measurement_unit = 'miles'

            distance_result = round(distance_result, 2)

            return TemplateResponse(request, "postcode/postcode.html", {"form": form, "distance_result": distance_result, 'measurement_unit': measurement_unit} )