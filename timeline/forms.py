from django.forms import ModelForm
from models import timeevent
from django.utils.translation import ugettext_lazy as _

class TimeLineForm(ModelForm):
    class Meta:
        model = timeevent
        fields = ('title','side',)
