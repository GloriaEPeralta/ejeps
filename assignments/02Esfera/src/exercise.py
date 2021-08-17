import math
import os

def main():
    #escribe tu código abajo de esta línea

    os.system('clear')
    
    radio = float(input("Dame el valor del radio de la esfera:"))
    area = 4 * math.pi * radio ** 2
    volumen = 4 / 3 * math.pi * math.pow(radio,3)

    print(f"El area de la esfera con radio {radio} es {area} unidades cuadradas")
    print(f"El volumen de la esfera con radio {radio} es {volumen} unidades cubicas")

if __name__=='__main__':
    main()
