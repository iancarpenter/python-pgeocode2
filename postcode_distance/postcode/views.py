from django.shortcuts import render
from .forms import PostcodeForm
from .models import Postcode
import pgeocode


def postcode(request):

    if request.method == "POST":

        form = PostcodeForm(request.POST)

        if form.is_valid():
            # with model forms you can call form.save which works because it has a model associated with it
            # and knows what to save and where
            # This isn't available here so get a handle to the form valid data 
            cd = form.cleaned_data
            
            # Postcode is a model that can be found in the models.py file. 
            # Create an object, populating the attributes with the values from the form
            pc = Postcode(
                start_postcode = cd['start_postcode'],
                end_postcode = cd['end_postcode'],
                result_measurement_unit = cd['distance_unit']
            )
            # can finally save
            pc.save()

            start_postcode = form['start_postcode'].value()
            end_postcode = form['end_postcode'].value()

            dist = pgeocode.GeoDistance('GB')
            distance_result = dist.query_postal_code(start_postcode, end_postcode)
            measurement_unit = 'km'

            # convert to miles if 
            if form['distance_unit'].value() == 'M':
                distance_result = distance_result / 1.609 
                measurement_unit = 'miles'

            distance_result = round(distance_result,2)
            
            return render(request, "postcode/postcode.html", {"form": form, "distance_result":distance_result, 'measurement_unit': measurement_unit})

    else:
        form = PostcodeForm
        return render(request, "postcode/postcode.html", {"form": form})