from ukmetoffice.models import Region, Month, Weather
from django.http import JsonResponse
from django.http import Http404

# Create your views here.
def process_queryset(qs):
    output = []
    for record in qs:
        output.append({
            "region": record.region.name,
            "month": record.month.name,
            "year": record.year,
            "tmax": record.tmax,
            "tmin": record.tmin,
            "tmean": record.tmean,
            "sunshine": record.sunshine,
            "rainfall": record.rainfall,
            "raindays1mm": record.raindays1mm,
            "airfrost": record.airfrost
        })
    return output

def region_all(request, region):
    qs = Weather.objects.select_related("region").select_related("month").filter(region__name=region).all().order_by("year", "month")
    if len(qs)==0:
        raise Http404
    output = process_queryset(qs)
    return JsonResponse(output, json_dumps_params={'indent': 2}, safe=False)

def region_timespan(request, region, start, end):
    qs = Weather.objects.select_related("region").select_related("month").filter(region__name=region, year__gte=start, year__lte=end).all().order_by(
        "year", "month")
    if len(qs) == 0:
        raise Http404
    output = process_queryset(qs)
    return JsonResponse(output, json_dumps_params={'indent': 2}, safe=False)
