from django import forms
from .models import Photo, Category


class PhotoForm(forms.ModelForm):
    new_category = forms.CharField(max_length=100, required=False)
    class Meta:
        model = Photo
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

    def save(self, *args, **kwargs):
        new_category = self.cleaned_data['new_category']
        if new_category:
            category = Category.objects.create(name=new_category)
            self.instance.category = category
        super().save(*args, **kwargs)
