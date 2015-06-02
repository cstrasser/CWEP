from django import forms
from models import STO
import datetime

class STOForm (forms.ModelForm):
    #nothingfield = forms.CharField(max_length=50, help_text ="needed something")
    contact_name = forms.CharField(widget=forms.TextInput(attrs={'size':500}),max_length=50, help_text ="contact name")
    entrydate = forms.DateField(widget=forms.DateInput(format = '%d/%m/%y'),input_formats=('%d/%m/%y',))
    stid = forms.IntegerField(widget=forms.HiddenInput())
    add1 = forms.CharField(widget=forms.TextInput(attrs={'size':50}))
    add2 = forms.CharField(widget=forms.TextInput(attrs={'size':50}))
    add3 = forms.CharField(widget=forms.TextInput(attrs={'size':50}))
    #notes = forms.CharField(widget=forms.Textarea(attrs={'size':100}))
    notes = forms.CharField(widget=forms.Textarea(attrs={'rows':7,'cols':99}))
    class Meta:
        model = STO
        fields = ('stid','project','status','person_responsible','customer_location','contact','notes',
                  'entrydate', 'status', 'reference',
                  'billing','phone','add1','add2','add3','city','state','stzip','tag','email')