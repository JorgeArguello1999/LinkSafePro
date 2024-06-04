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
                if opcion == 'v_f': result = speed.calcular_velocidad_final(velocidad_inicial, aceleracion, tiempo)
                elif opcion == 'v_i': result = speed.calcular_velocidad_inicial(velocidad_final, aceleracion, tiempo)
                elif opcion == 'a': result = speed.calcular_aceleracion(velocidad_final, velocidad_inicial, tiempo)
                elif opcion == 't': result = speed.calcular_tiempo(velocidad_final, velocidad_inicial, aceleracion)
            except Exception as e:
                print(e)
                result = f"Error: {e}"
            


    return render(request, 'speed.html', {'code': code, 'result': result, 'form': form})