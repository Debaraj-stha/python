from my_app.models import multipleImageUpload
from django import forms
class multipleImageUploadForm(forms.ModelForm):
    class Meta:
        model = multipleImageUpload
        fields = ['images']
        widgets = {
            'images': forms.ClearableFileInput(attrs={'multiple': True}),
        }
