from django import forms
from django.core.exceptions import ValidationError

from .models import Advertisements


class AdvertisementForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['description'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['price'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['auction'].widget.attrs['class'] = 'form-check-input'
        self.fields['image'].widget.attrs['class'] = 'form-control form-control-lg'
    class Meta:
        model = Advertisements
        fields = ("title", "description", "image", "price", "auction")

    def clean_title(self):
        title = self.cleaned_data['title'] #чистые данные
        if title.startswith('?'):
            raise ValidationError('Заголовок не может начинаться с ?')
        return title