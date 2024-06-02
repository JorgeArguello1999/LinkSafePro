from django.shortcuts import render
from binary import forms

def get(request):
    form = forms.ConversionForm()
    result = None

    if request.method == 'POST':
        form = forms.ConversionForm(request.POST)
        if form.is_valid():
            conversion_type = form.cleaned_data['conversion_type']
            input_data = form.cleaned_data['data']
            result = f"The result is: {conversion_type} and {input_data}" 

    return render(request, 'binary.html', {'form': form, 'result': result})
