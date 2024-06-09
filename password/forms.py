from django import forms 

class PasswordForm(forms.Form):
    length = forms.IntegerField()