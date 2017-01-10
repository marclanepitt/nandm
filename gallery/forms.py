from django.forms import ModelForm
from models import Photo
from django.utils.translation import ugettext_lazy as _


class GalleryForm(ModelForm):
    class Meta:
        model = Photo
        fields = ('url',)
