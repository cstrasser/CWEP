from django import forms
from models import STO
import datetime

class STOForm (forms.ModelForm):
    #nothingfield = forms.CharField(max_length=50, help_text ="needed something")
    contact_name = forms.CharField(max_length=50, help_text ="contact name")
    stid = forms.IntegerField(widget=forms.HiddenInput())
    
    class Meta:
        model = STO
        fields = ('stid','project','status','person_responsible','customer_location','contact','notes',
                  'entrydate', 'status', 'reference', 'contact',
                  'billing','phone','add1','add2','add3','city','state','stzip','tag','email')