from django.shortcuts import render
from speed import forms

from tools import read_code
from tools import speed

def get(request):
    code = read_code.read_code('speed.py')
    result = None
    form = forms.CalculoForm(initial={
        'velocidad_inicial': 0,
        'velocidad_final': 0,
        'aceleracion': 0,
        'tiempo': 0,
    })

    if request.method == 'POST':
        form = forms.CalculoForm(request.POST)
        if form.is_valid():
            try:
                opcion = form.cleaned_data['opcion']
                velocidad_inicial = form.cleaned_data.get('velocidad_inicial')
                velocidad_final = form.cleaned_data.get('velocidad_final')
                aceleracion = form.cleaned_data.get('aceleracion')
                tiempo = form.cleaned_data.get('tiempo')

                if opcion == 'v_f': result = speed.calcular_velocidad_final(
                    float(velocidad_inicial), float(aceleracion), float(tiempo)
                )
                elif opcion == 'v_i': result = speed.calcular_velocidad_inicial(
                    float(velocidad_final), float(aceleracion), float(tiempo)
                )
                elif opcion == 'a': result = speed.calcular_aceleracion(
                    float(velocidad_final), float(velocidad_inicial), float(tiempo)
                )
                elif opcion == 't': result = speed.calcular_tiempo(
                    float(velocidad_final), float(velocidad_inicial), float(aceleracion)
                )
            except Exception as e:
                print(e)
                result = f"Error: {e}"
            


    return render(request, 'speed.html', {'code': code, 'result': result, 'form': form})