from django import forms

class ConversionForm(forms.Form):
    CONVERSION_CHOICES = [
        ('binary_decimal', 'Binary to Decimal'),
        ('decimal_binary', 'Decimal to Binary'),
    ]
    conversion_type = forms.ChoiceField(
        choices=CONVERSION_CHOICES,
        widget=forms.RadioSelect,
    )
    data = forms.CharField(max_length=100, required=False, label='Data')
