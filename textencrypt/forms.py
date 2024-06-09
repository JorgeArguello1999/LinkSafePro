from django import forms 

class TextEncrypt(forms.Form):
    CONVERSION_CHOICES = [
        ('', '--- Select ---'),
        ('decrypt', 'Decrypt your text'),
        ('encrypt', 'Encrypt your text')
    ]

    method_select = forms.ChoiceField(choices=CONVERSION_CHOICES)

    text = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows': 4,  
            'cols': 40, 
            'placeholder': 'Put your text...' 
        })
    )
    password = forms.CharField(widget=forms.PasswordInput())
