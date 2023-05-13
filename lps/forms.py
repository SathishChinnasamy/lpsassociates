from django import forms
from lps.models import FreeConsultationModel

class FreeConsultForm(forms.ModelForm):

    class Meta:
        model= FreeConsultationModel
        fields = ["name","cmobilenumber","cemail","subject","message","iscontacted"]
        #labels = {'name': "Name", "cmobilenumber": "Mobile Number","cemail":"email","subject":"Subject","message":"Message",}