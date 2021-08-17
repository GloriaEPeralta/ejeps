import math
import os

def main():
    #escribe tu código abajo de esta línea

    os.system('clear')
    print("CALCULO DEL AREA Y PERIMETRO DE UN CUADRADO")
    print("===========================================")
    lado=float(input("Dame el lado del cuadrado"))
    perimetro= 4*lado
    area=lado**2
    print("El perimetro de este cuadrado es "+ str(perimetro))
    print("El area de este cuadrado es "+ str(area))
if __name__=='__main__':
    main()
