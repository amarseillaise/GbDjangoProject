from django import forms
from .models import Customers, Goods


class CustomerChoiceForm(forms.Form):
    customer = forms.ModelChoiceField(queryset=Customers.objects.all())


class PhotoChoiceForm(forms.ModelForm):
    class Meta:
        model = Goods
        fields = ['photo',]

    def __init__(self, *args, pkid=None, **kwargs):
        super(PhotoChoiceForm, self).__init__(*args, **kwargs)
        self.fields['photo'].widget.attrs.update({'id': pkid or self.instance.id, 'onchange': "upload(this.id)"})
