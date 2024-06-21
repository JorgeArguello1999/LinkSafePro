def calcular_velocidad_final(velocidad_inicial:float=0.0, aceleracion:float=0.0, tiempo:float=0.0):
    respuesta = velocidad_inicial + (aceleracion * tiempo)
    return f'La velocidad final: {respuesta}'

def calcular_velocidad_inicial(velocidad_final:float=0.0, aceleracion:float=0.0, tiempo:float=0.0):
    respuesta = velocidad_final - (aceleracion * tiempo)
    return f'La velocidad inicial es: {respuesta}'

def calcular_aceleracion(velocidad_final:float=0.0, velocidad_inicial:float=0.0, tiempo:float=1.0):
    respuesta = (velocidad_final - velocidad_inicial) / tiempo
    return f'La aceleración: {respuesta}' 

def calcular_tiempo(velocidad_final:float=0.0, velocidad_inicial:float=0.0, aceleracion:float=1.0):
    respuesta = (velocidad_final - velocidad_inicial) / aceleracion
    return f'El tiempo final es: {respuesta}'