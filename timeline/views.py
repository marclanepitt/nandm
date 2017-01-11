from django.shortcuts import render,redirect
from forms import TimeLineForm
from models import timeevent

# Create your views here.
def timelineview (request):
    if request.method == "POST":
        form = TimeLineForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.save()
            return redirect('timeline.html', pk=event.pk)

    else:
        form = TimeLineForm()
        timeeventlist = timeevent.objects.order_by('-event_date')
        return render(request,'timeline.html', {'events': timeeventlist, 'form': form})
