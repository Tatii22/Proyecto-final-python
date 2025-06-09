import random
import compraBoletos 

def generarAleatoriosganador():
    numganadores = []
    for i in range(6):
        num = random.randint(1, 99)
        numganadores.append(num)
    compraBoletos.loteria["ganadores"]. append(numganadores)
    print(f"Numeros ganadores {numganadores}")

def generarAleatorios():
    
    pass

generarAleatoriosganador()

