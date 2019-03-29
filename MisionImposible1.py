# encoding: UTF-8
# Autor: Jose Isidro Sánchez Vázquez
# Crear espirografos
import math

import pygame   # Librería de pygame
import random


def generarColor():
    color = random.randint(0, 255)
    return color

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
VERDE_BANDERA = (27, 94, 32)    # un poco de rojo, más de verde, un poco de azul
ROJO = (255, 0, 0)      # solo rojo, nada de verde, nada de azul
AZUL = (0, 0, 255)      # nada de rojo, ni verde, solo azul


# Estructura básica de un programa que usa pygame para dibujar
def dibujar(r,R,l):
    # Inicializa el motor de pygame
    pygame.init()
    # Crea una ventana de ANCHO x ALTO
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no

    while not termina:  # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True      # Queremos terminar el ciclo

        # Borrar pantalla
        ventana.fill(BLANCO)

        # Dibujar, aquí haces todos los trazos que requieras
        # Normalmente llamas a otra función y le pasas -ventana- como parámetro, por ejemplo, dibujarLineas(ventana)
        # Consulta https://www.pygame.org/docs/ref/draw.html para ver lo que puede hacer draw
        radio = 100
        for angulo in range(0,360+1,20):
            a = math.radians(angulo)  # Convierte a radianes
            x = int(radio*math.cos(a))
            y = int(radio*math.sin(a))
            pygame.draw.circle(ventana,generarColor(), ((x + ALTO // 2), (ANCHO // 2 + y)),radio,2)
        k = r / R
        for segundo in range(0, 360 * r // math.gcd(r, R)):
            teta = math.radians(segundo)  # Se convierten los grados a radianes.

            x = int(R * (((1 - k) * math.cos(teta)) + ((l * k) * math.cos((((1 - k) / (k)) * teta)))))

            y = int(R * (((1 - k) * math.sin(teta)) - (l * k) * math.sin((((1 - k) / (k)) * teta))))

            pygame.draw.circle(ventana, generarColor(), ((x + ALTO // 2), (ANCHO // 2 + y)), 1)




        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


# Función principal, aquí resuelves el problema
def main():
    r = eval(input("Teclea el valor de r: "))
    R = eval(input("Teclea el valor de R: "))
    l = eval(input("Teclea el valor de l: "))
    dibujar(r,R,l)   # Por ahora, solo dibuja


# Llamas a la función principal
main()