from django import forms


class ImageForm(forms.Form):
    file = forms.FileField(widget=forms.FileInput(attrs={'id': 'file'}))
