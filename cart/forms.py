from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]

class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce = int)

    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)


    # def __init__(self, *args, **kwargs):
    #     super(PostForm, self).__init__(*args, **kwargs)
    #     for field in (self.fields['title'], self.fields['body'], self.fields['status']):
    #         fields.widget.attrs.update({'class':'form-control'})

    #     self.fields['image'].widget.attrs.update({'class':'form-control-file'})



