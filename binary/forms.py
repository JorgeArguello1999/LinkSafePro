# forms.py
from django import forms

class ConversionForm(forms.Form):
    CONVERSION_CHOICES = [
        ('binary_decimal', 'Binario a Decimal'),
        ('decimal_binary', 'Decimal a Binario'),
    ]
    conversion_type = forms.ChoiceField(
        choices=CONVERSION_CHOICES,
        widget=forms.RadioSelect,
    )
    data = forms.CharField(max_length=100, required=False, label='Data')
