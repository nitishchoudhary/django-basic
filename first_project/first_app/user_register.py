from django import forms
from first_app.models import Register

class NewUserForm(forms.ModelForm):
    class Meta():
        model = Register
        fields = '__all__'
