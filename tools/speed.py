def calcular_velocidad_final(velocidad_inicial:float=0.0, aceleracion:float=0.0, tiempo:float=0.0):
    return velocidad_inicial + (aceleracion * tiempo)

def calcular_velocidad_inicial(velocidad_final:float=0.0, aceleracion:float=0.0, tiempo:float=0.0):
    return velocidad_final - (aceleracion * tiempo)

def calcular_aceleracion(velocidad_final:float=0.0, velocidad_inicial:float=0.0, tiempo:float=1.0):
    return (velocidad_final - velocidad_inicial) / tiempo

def calcular_tiempo(velocidad_final:float=0.0, velocidad_inicial:float=0.0, aceleracion:float=1.0):
    return (velocidad_final - velocidad_inicial) / aceleracion