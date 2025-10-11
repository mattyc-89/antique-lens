from django import forms
from django.forms import ModelForm 

from .models import Antique

class UploadAntique(ModelForm):
    image = forms.ImageField(required=True, label='Upload Image')

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            if image.size > 10 * 1024 * 1024:  # 10MB limit
                raise forms.ValidationError("Image size exceeds the 10MB limit.")
            return image
        raise forms.ValidationError("No image provided.")
