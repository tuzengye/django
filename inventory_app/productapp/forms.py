# from django import forms
#
# class NameForm(forms.Form):
#     your_name = forms.CharField(label='Your name', max_length=100)

from django import forms
from . models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('title', 'description','price','summary',)