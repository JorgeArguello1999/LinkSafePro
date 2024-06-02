from django.shortcuts import render
from binary import forms

from tools import binary
from tools import read_code

def get(request):
    form = forms.ConversionForm()
    result = None

    code = read_code.read_code('binary.py')

    if request.method == 'POST':
        form = forms.ConversionForm(request.POST)
        if form.is_valid():
            conversion_type = form.cleaned_data['conversion_type']
            input_data = form.cleaned_data['data']

        try:
            input_data = float(input_data)
            if conversion_type == 'decimal_binary': result = binary.decimal_binary(input_data)
            if conversion_type == 'binary_decimal': result = binary.binary_decimal(input_data)
            
        except Exception as e:
            result = "Error to operate with data, only numbers"


    return render(request, 'binary.html', {'form': form, 'result': result, 'code': code})
