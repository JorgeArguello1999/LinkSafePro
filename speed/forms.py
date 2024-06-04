from django import forms

class CalculoForm(forms.Form):
    OPCIONES = [
        ('1', 'Velocidad final (v_f)'),
        ('2', 'Velocidad inicial (v_i)'),
        ('3', 'Aceleración (a)'),
        ('4', 'Tiempo (t)'),
    ]
    
    opcion = forms.ChoiceField(choices=OPCIONES, label='Seleccione la variable que desea calcular')
    velocidad_inicial = forms.FloatField(required=False, label='Velocidad inicial (m/s)')
    velocidad_final = forms.FloatField(required=False, label='Velocidad final (m/s)')
    aceleracion = forms.FloatField(required=False, label='Aceleración (m/s^2)')
    tiempo = forms.FloatField(required=False, label='Tiempo (s)')