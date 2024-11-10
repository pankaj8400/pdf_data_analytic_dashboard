# violation/forms.py
from django import forms

class DateRangeForm(forms.Form):
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

class CameraRangeForm(forms.Form):
    camera_number = forms.IntegerField(required=False, label="Camera Number")
    start_camera_number = forms.IntegerField(required=False, label="Start Camera Number")
    end_camera_number = forms.IntegerField(required=False, label="End Camera Number")

from .models import Violation

class ViolationForm(forms.ModelForm):
    class Meta:
        model = Violation
        fields = ['camera_number', 'without_jacket', 'without_helmet', 'both', 'image']    



class ReportForm(forms.Form):
    # Define your form fields here
    camera_number = forms.IntegerField(required=False)
    start_date = forms.DateField(required=False)
    end_date = forms.DateField(required=False)
    # Add more fields as needed        