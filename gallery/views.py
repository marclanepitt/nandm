from django.shortcuts import render, redirect
from django.utils import timezone
from models import Photo
from forms import GalleryForm




def GalleryView(request):
    if request.method == "POST":
        form = GalleryForm(request.POST)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.date_published = timezone.now()
            photo.save()
            return redirect('gallery.html', pk=photo.pk)
    else:
        form = GalleryForm()
        piclist = Photo.objects.order_by('-date_published')
        return render(request, 'gallery.html', {'form': form,'pictures':piclist})


