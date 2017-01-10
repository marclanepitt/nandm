from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from models import Photo
from forms import GalleryForm
from django.template import RequestContext


def GalleryView(request):

    if request.method == 'POST':
        form = GalleryForm(request.POST)

        if form.is_valid():
            return HttpResponseRedirect('/done/')

    else:
        form = GalleryForm()

        context = RequestContext(request)
        piclist = Photo.objects.order_by('-date_published')
        context_dict = {'pictures': piclist, 'form' :form}
        return render_to_response('gallery.html', context_dict, context)
