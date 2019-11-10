from django import forms
from .models import Photo

# class UploadFileForm(forms.ModelForm):
#     class Meta:
#         model = Photo
#         fields = ['origin', 'private', 'category', 'tags']

UploadMultipleFormSet = forms.modelformset_factory(
    Photo, 
    # form=UploadFileForm,
    fields = ['origin', 'private', 'category', 'tags'],
    extra=10,
    # max_num=5
)