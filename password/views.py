from django.shortcuts import render
from password import forms

from tools import read_code
from tools import password

def get(request):
    code = read_code.read_code('password.py')
    form = forms.PasswordForm()
    result = None

    if request.method == 'POST': 
        form = forms.PasswordForm(request.POST)
        if form.is_valid(): 
            try:
                input_data = int(form.cleaned_data.get('length'))
                result = password.generate_password(input_data)

            except Exception as e:
                result: f'Error: {e}'

    return render(request, 'password.html', {'form': form, 'code': code , 'result': result})