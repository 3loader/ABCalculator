import json
import math

from django.http import HttpResponse

# Create your views here.


def calculate(request):
    data = dict(p_value='NaN', significance='No')
    if request.GET:
        try:
            control_visitors = int(request.GET['control_visitors'])
            variation_visitors = int(request.GET['variation_visitors'])
            control_conversions = int(request.GET['control_conversions'])
            variation_conversions = int(request.GET['variation_conversions'])

            control_p = control_conversions / control_visitors
            variation_p = variation_conversions / variation_visitors

            control_se = math.sqrt((control_p * (1 - control_p) / control_visitors))
            se_variation = math.sqrt((variation_p * (1 - variation_p) / variation_visitors))

            z_score = (control_p - variation_p) / math.sqrt(control_se ** 2 + se_variation ** 2)

            p_value = round(1 - ((1 + math.erf(z_score / math.sqrt(2))) / 2), 3)
            data['p_value'] = p_value

            if p_value > 0.95 or p_value < 0.05:
                data['significance'] = 'Yes!'
        except ValueError:
            pass
    return HttpResponse(json.dumps(data))
