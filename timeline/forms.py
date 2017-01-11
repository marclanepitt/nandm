from django.forms import ModelForm
from django import forms
from models import timeevent
from django.utils.translation import ugettext_lazy as _

class DateInput(forms.DateInput):
    input_type = 'date'

class TimeLineForm(ModelForm):
    class Meta:
        model = timeevent
        fields = ('title', 'description','pic','event_date','side')
        labels = {
            'pic': _("Link to Picture")
        }
        help_texts = {
            'side': _("Select for right side")
        }
        widgets = {
            'event_date' : DateInput()
        }


