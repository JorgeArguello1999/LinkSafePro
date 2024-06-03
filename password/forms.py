from django import forms 

class PasswordForm(forms.Form):
    length = forms.IntegerField(max_value=500)