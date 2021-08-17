import math
import os

def main():
    #escribe tu código abajo de esta línea

    os.system('clear')
    
    catetoA = float(input("Valor CatetoA:"))
    catetoB = float(input("Valor CatetoB:"))
    hipotenusa = math.pow(catetoA,2)+math.pow(catetoB,2)

    
    print(f"El cuadrado de la hipotenusa {hipotenusa} ")

    print(f"Los valores de los catetos son CatetoA {catetoA} CatetoB {catetoB} ")
    print("LA RAIZ CUADRADA")
    numero=float(input("Numero"))
    raizC=math.sqrt(numero)
    print(f"LA RAIZ CUADRADA DE {numero} es {raizC} ")
    

if __name__=='__main__':
    main()
