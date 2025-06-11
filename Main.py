import compraBoletos
import resultadosLoteria
from historial import mostrarHistorialLoteria, cargarHistorialLoteria

opcionesMenu = """
                        |\__/,|   (`\\
                        |_ _  |.--.) )
                        ( T   )     /
                        (((^_(((/(((_/
·································································
 _                            _          ______  _             
| |           _              (_)        |  ___ \(_)            
| |      ___ | |_  ____  ____ _  ____   | | _ | |_  ____ _   _ 
| |     / _ \|  _)/ _  )/ ___) |/ _  |  | || || | |/ _  | | | |
| |____| |_| | |_( (/ /| |   | ( ( | |  | || || | ( ( | | |_| |
|_______)___/ \___)____)_|   |_|\_||_|  |_||_||_|_|\_||_|\____|

Seleccione una opción:
1. Comprar boletos 🤑😸
2. Realizar sorteo y mostrar resultados 🎰😼
3. Ver historial de sorteos 📄🙀
4. Salir 📤😿
"""

def menu():
    while True:
        print(opcionesMenu)
        opcion = input("Ingrese el número de su elección: ")

        if opcion == '1':
            compraBoletos.comprarBoletos(compraBoletos.loteria["boletos"])

        elif opcion == '2':
            resultadosLoteria.generarAleatoriosganador()
            resultadosLoteria.evaluarBoletos(compraBoletos.loteria)

        elif opcion == '3':
            historial = cargarHistorialLoteria()
            mostrarHistorialLoteria(historial)

        elif opcion == '4':
            print("👋😽 ¡Gracias por usar la Lotería Virtual Miau! Hasta luego.")
            break

        else:
            print("😾 Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()
