from django.shortcuts import render
from timeline.models import timeevent

def homeview (request):
    timeeventlist = timeevent.objects.order_by('?')
    return render(request, 'index.html', {'events': timeeventlist})

