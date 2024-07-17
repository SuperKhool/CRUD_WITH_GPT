from django import forms
from .models import Employ


class Empolyeform(forms.ModelForm):
    class Meta:
        model = Employ
        fields = ['name','email','phone','profile_image']