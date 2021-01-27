from borracho import BorrachoTradicional
from campo import Campo
from coordenada import Coordenada

from bokeh.plotting import figure, show

def caminata(campo, borracho, pasos):
    inicio = campo.obtener_coordenada(borracho)
    x = []
    y = []
    x.append(campo.obtener_coordenada(borracho).x)
    y.append(campo.obtener_coordenada(borracho).y)
    for _ in range(pasos):
        campo.mover_borracho(borracho)
        a = campo.obtener_coordenada(borracho).x
        b = campo.obtener_coordenada(borracho).x
        x.append(a)
        y.append(b)
    return inicio.distancia(campo.obtener_coordenada(borracho))

def simular_caminata(pasos, numero_intentos, tipo_borracho):
    borracho = tipo_borracho('Davd')
    origen = Coordenada(0,0)
    distancias = []
    for _ in range(numero_intentos):
        campo = Campo()
        campo.anadir_borracho(borracho, origen)
        simulacion_caminata = caminata(campo, borracho, pasos)
        distancias.append(round(simulacion_caminata, 1))
    return distancias

def main(distancias_caminata, numero_intentos, tipo_borracho):
    distancias_media_caminata = []
    for pasos in distancias_caminata:
        distancias = simular_caminata(pasos, numero_intentos, tipo_borracho)
        distancia_media = round(sum(distancias) / len(distancias), 3)
        distancia_maxima = max(distancias)
        distancia_minima = min(distancias)
        distancias_media_caminata.append(distancia_media)
        print(f'{tipo_borracho.__name__} caminata aleatoria de {pasos}')
        print(f'Media: {distancia_media}')
        print(f'Maxima: {distancia_maxima}')
        print(f'Minima: {distancia_minima}')

if __name__ == '__main__':
    distancias = [10, 100, 1000, 10000]
    numero_intentos = 100
    main(distancias, numero_intentos, BorrachoTradicional)
