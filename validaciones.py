  # Funciones auxiliares 
def enterParaContinuar(mensaje: str = "Enter para continuar..."):
    input(mensaje)

def validarInputDinero(mensaje: str, valMin: int = 1000, paso: int = 1000):
    while True:
        try:
            entrada = input(mensaje)
            entradaLimpia = entrada.replace('.', '') 
            rta = float(entradaLimpia)  
            if rta.is_integer():
                rta = int(rta)
                if rta >= valMin and rta % paso == 0:
                    return rta
                else:
                    print(f"❌😾 Ingresa un valor múltiplo de {paso} (ej: 1000, 2000...)")
            else:
                print("❌😾 No se permiten valores con centavos. Usa solo números enteros.")
        except ValueError:
            print("⚠️ Entrada inválida. Asegúrate de ingresar solo números.")
        enterParaContinuar()

def validarInput(titulo: str, valMin: int = 0, valMax: int = 5):
    while True:
        try:
            rta = int(input(titulo))
            if valMin <= rta <= valMax:
                return rta
            else:
                print(f"Por favor ingrese solo valores permitidos... \nRango de {valMin} a {valMax}")
                enterParaContinuar()
        except:
            enterParaContinuar("OIGA ESTA MAL, INTÉNTALO DE NUEVO")

def solicitarDatos(campos: list):
    respuesta = []
    for c in campos:
        if c["type"] == "dinero":
            respuesta.append(validarInputDinero(c["mensaje"]))
        elif c["type"] == "texto":
            while True:
                nombre = input(c["mensaje"]).strip()
                if nombre != "":
                    respuesta.append(nombre)
                    break
                else:
                    print("❌😾 El nombre no puede estar vacío.")
                    enterParaContinuar()
    return respuesta
