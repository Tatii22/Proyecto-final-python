import random
import compraBoletos 


def generarAleatoriosganador():
    numganadores = []
    for i in range(6):
        num = random.randint(0, 9)
        numganadores.append(num)
    compraBoletos.loteria["ganadores"]. append(numganadores)
    print(compraBoletos.loteria["ganadores"])

def generarAleatorios():
    
    pass

generarAleatoriosganador()

