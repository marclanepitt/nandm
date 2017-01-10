from django.shortcuts import render,render_to_response
from django.http import HttpResponseRedirect
from forms import TimeLineForm
from models import timeevent
from django.template import RequestContext

# Create your views here.
def timelineview (request):
    if request.method == 'POST':
        form = TimeLineForm(request.POST)

        if form.is_valid():
            return HttpResponseRedirect('/done/')

    else:
        form = TimeLineForm()

    context = RequestContext(request)
    timeeventlist = timeevent.objects.order_by('-event_date')
    context_dict = {'events':timeeventlist, 'form':form}
    return render_to_response('timeline.html',context_dict,context)
