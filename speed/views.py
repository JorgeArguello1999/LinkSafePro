from django.shortcuts import render
from speed import forms

from tools import read_code
from tools import speed

def get(request):
    code = read_code.read_code('speed.py')
    result = None
    form = forms.CalculoForm()

    if request.method == 'POST':
        form = forms.CalculoForm(request.POST)
        if form.is_valid():
            opcion = form.cleaned_data['opcion']
            velocidad_inicial = float(form.cleaned_data.get('velocidad_inicial'))
            velocidad_final = float(form.cleaned_data.get('velocidad_final'))
            aceleracion = float(form.cleaned_data.get('aceleracion'))
            tiempo = float(form.cleaned_data.get('tiempo'))

            try:
                if opcion == '1': result = speed.calcular_velocidad_final(velocidad_inicial, aceleracion, tiempo)
                elif opcion == '2': result = speed.calcular_velocidad_inicial(velocidad_final, aceleracion, tiempo)
                elif opcion == '3': result = speed.calcular_aceleracion(velocidad_final, velocidad_inicial, tiempo)
                elif opcion == '4': result = speed.calcular_tiempo(velocidad_final, velocidad_inicial, aceleracion)
            except Exception as e:
                print(e)
                result = f"Error: {e}"
            


    return render(request, 'speed.html', {'code': code, 'result': result, 'form': form})