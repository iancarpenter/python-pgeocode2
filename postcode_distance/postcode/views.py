from django.shortcuts import render
from .forms import PostcodeForm
import pgeocode


def postcode(request):
    if request.method == "POST":
        form = PostcodeForm(request.POST)
        if form.is_valid():
            #form.save()
            
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