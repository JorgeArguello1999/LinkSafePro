from django.shortcuts import render
from textencrypt import forms

from tools import read_code
from tools import textencrypt

def get(request):
    code = read_code.read_code('textencrypt.py')
    form = forms.TextEncrypt()
    result = None

    if request.method == 'POST':
        form = forms.TextEncrypt(request.POST)
        if form.is_valid():
            password = form.cleaned_data.get('password')
            text = form.cleaned_data.get('text')
            choice = form.cleaned_data.get('method_select')

        try:
            if choice == 'encrypt': result = textencrypt.encrypt(text, password)
            if choice == 'decrypt': result = textencrypt.decrypt(text, password)
        except Exception as e:
            print(e)
            result = f"Error: Your chose is correct?"

    return render(request, 'textencrypt.html', {
        'form': form, 'result': result, 'code': code
    })