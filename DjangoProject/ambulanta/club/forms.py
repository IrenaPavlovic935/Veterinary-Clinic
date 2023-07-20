from django import forms
from .models import Venue, Event

class VenueForm(forms.ModelForm):
    class Meta:
        model = Venue
        fields = ('name', 'address', 'phone', 'venue_image')
        
        labels = {
            'name': '',
            'address' : '',
            'phone' : '',
            'venue_image' : '',
        }
        widgets={
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Venue Name'}),
            'address' : forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Address'}),
            'phone' : forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Phone Number'}),
        }
        
        
class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ( 'name','venue', 'event_date','description','menager', 'event_image')
        
        labels = {
            'name': '',
            'event_date' : '',
            'venue' : '', 
            'description' : '',
            'menager' : '',
            'event_image' : '',
        }
        widgets={
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Event Name'}),
            'event_date' : forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Event Date'}),
            'venue' : forms.Select(attrs={'class':'form-select', 'placeholder': 'Venue', 'style': 'width: 400px; height:50px;border-radius:5px; border: 2px solid #ccc;'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description', 'style': 'width: 390px;padding-left:7px;height: 100px;border-radius:5px; font-size: 20px; border: 2px solid #ccc;'}),
            'menager': forms.TextInput(attrs={'class':'form-select', 'placeholder': 'Menager', 'style': 'width: 400px; height:50px;border-radius:5px; border: 2px solid #ccc;'}),
        }