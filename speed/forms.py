from django import forms

class CalculoForm(forms.Form):
    OPCIONES = [
        ('-- Selecciona --', '--Selecciona--'),
        ('v_f', 'Velocidad final (v_f)'),
        ('v_i', 'Velocidad inicial (v_i)'),
        ('a', 'Aceleración (a)'),
        ('t', 'Tiempo (t)'),
    ]
    
    opcion = forms.ChoiceField(choices=OPCIONES, label='Seleccione la variable que desea calcular')
    velocidad_inicial = forms.FloatField(required=False, label='Velocidad inicial (m/s)')
    velocidad_final = forms.FloatField(required=False, label='Velocidad final (m/s)')
    aceleracion = forms.FloatField(required=False, label='Aceleración (m/s^2)')
    tiempo = forms.FloatField(required=False, label='Tiempo (s)')