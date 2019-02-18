from django import forms
from django.core import validators

class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    varify_email = forms.EmailField(label="Confirm email!")
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        all_clean_data = super().clean()
        print(all_clean_data)
        email = all_clean_data['email']
        vemail = all_clean_data['varify_email']

        if email != vemail:
            raise forms.ValidationError("Make sure email match!")
