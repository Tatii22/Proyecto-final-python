import random

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
                    print(f"❌ Ingresa un valor múltiplo de {paso} (ej: 1000, 2000...)")
            else:
                print("❌ No se permiten valores con centavos. Usa solo números enteros.")
        except ValueError:
            print("⚠️ Entrada inválida. Asegúrate de ingresar solo números.")
        enterParaContinuar()

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
                    print("❌ El nombre no puede estar vacío.")
                    enterParaContinuar()
    return respuesta

def boleto(codigo: int, nombre: str, dinero: int):
    return {"codigo": codigo, "nombre": nombre, "dinero": dinero}

precios = [1000, 2000, 5000, 10000, 20000]
def calcularBoletos(valor, precios):
    resultado = {}
    for precio in precios:
        cantidad = valor // precio
        resultado[precio] = cantidad
    return resultado


def validarInput(titulo : str, valMin: int = 0, valMax: int = 5):
    while True:
        try:
            rta = int(input(titulo))
            if rta >= valMin and rta <= valMax:
                return rta
            else:
                print(f"Por favor ingrese solo valores permitidos... \nRango de {valMin} a {valMax}")
                enterParaContinuar()
        except:
            enterParaContinuar("OIGA ESTA MAL, INTENTALO DE NUEVO")


def seleccionBoletos(dineroDisponible):
    boletosComprados = []
    dineroRestante = dineroDisponible

    while dineroRestante >= 1000:
        opcionesMenu = []
        opcionesDisponibles = calcularBoletos(dineroRestante, precios)

        for precio, cantidad in opcionesDisponibles.items():
            if cantidad > 0:
                opcionesMenu.append(precio)

        #print(f"\n💰 Saldo restante: ${dineroRestante}")

        print("🎟️ Puedes comprar:")
        for precio in opcionesMenu:
            print(f"  - Hasta {opcionesDisponibles[precio]} boletos de ${precio}")

        print("\n📋 ¿Qué tipo de boleto deseas comprar?")
        for i, precio in enumerate(opcionesMenu, start=1):
            print(f"{i}. Boleto de ${precio}")

        opcion = validarInput("→ ", 1, len(opcionesMenu))
        precioSeleccionado = opcionesMenu[opcion - 1]
        maxCantidad = opcionesDisponibles[precioSeleccionado]

        cantidad = validarInput(f"¿Cuántos boletos de ${precioSeleccionado} deseas comprar?\n→ ", 1, maxCantidad)
        for _ in range(cantidad):
            boleto = {
                "valor": precioSeleccionado,
                "numeros": random.sample(range(1, 49), 6)
            }   
            boletosComprados.append(boleto)

        dineroRestante -= precioSeleccionado * cantidad

        print(f"✅ Has comprado {cantidad} boletos de ${precioSeleccionado}.")
        print(f"💸 Te queda: ${dineroRestante}")
        print("")

    total = len(boletosComprados)
    print(f"🎫 Total de boletos comprados: {total}")
    print("\n🧾 Resumen de boletos comprados:")
    print("┌──────────────┬───────────────────────────────┐")
    print("│   Valor 💵   │       Números 🎲              │")
    print("├──────────────┼───────────────────────────────┤")

    for boleto in boletosComprados:
        numeros = ", ".join(f"{n:02}" for n in boleto["numeros"])
        print(f"│   ${boleto['valor']:<8}  │  {numeros:<29}│")

    print("└──────────────┴───────────────────────────────┘")

    return boletosComprados




def comprarBoletos(lista):
    nuevoId = max([b["codigo"] for b in lista], default=0) + 1
    datosBoletos = [
        {"mensaje": "👤 Ingresa tu nombre:\n", "type": "texto"},
        {"mensaje": "💵 ¿Cuánto deseas apostar? (mínimo $1.000):\n", "type": "dinero"}
    ]
    datos = solicitarDatos(datosBoletos)
    dineroDisponible = datos[1]

    boletosComprados = seleccionBoletos(dineroDisponible)

    nuevoUsuario = boleto(nuevoId, datos[0], datos[1])
    nuevoUsuario["boletos"] = boletosComprados

    loteria["boletos"].append(nuevoUsuario)
    print("✅ Datos registrados correctamente.")
    print(loteria)


# Diccionario principal
loteria = {
    "boletos": [],
    "ganadores" : [],
    "historial" : []
}


comprarBoletos(loteria["boletos"])

