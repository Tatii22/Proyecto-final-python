import random
from validaciones import (
    validarInput,
    validarInputDinero,
    enterParaContinuar,
    solicitarDatos
)



def boleto(codigo: int, nombre: str, dinero: int):
    return {"codigo": codigo, "nombre": nombre, "dinero": dinero}

precios = [1000, 2000, 5000, 10000, 20000]
def calcularBoletos(valor, precios):
    resultado = {}
    for precio in precios:
        cantidad = valor // precio
        resultado[precio] = cantidad
    return resultado

def seleccionBoletos(dineroDisponible):
    boletosComprados = []
    dineroRestante = dineroDisponible

    while dineroRestante >= 1000:
        opcionesMenu = []
        opcionesDisponibles = calcularBoletos(dineroRestante, precios)

        for precio, cantidad in opcionesDisponibles.items():
            if cantidad > 0:
                opcionesMenu.append(precio)

        

        print("🎟️🐱 Puedes comprar:")
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
        print(f"Te queda: ${dineroRestante}")
        print("")

    total = len(boletosComprados)
    print(f"🎫🙀 Total de boletos comprados: {total}")
    print("\n🧾😼 Resumen de boletos comprados:")
    print("┌──────────────┬───────────────────────────────┐")
    print("│   Valor $    │       Números 🐾              │")
    print("├──────────────┼───────────────────────────────┤")

    for boleto in boletosComprados:
        numeros = ", ".join(f"{n:02}" for n in boleto["numeros"])
        print(f"│   ${boleto['valor']:<8}  │  {numeros:<29}│")

    print("└──────────────┴───────────────────────────────┘")

    return boletosComprados




def comprarBoletos(lista):
    nuevoId = max([b["codigo"] for b in lista], default=0) + 1
    datosBoletos = [
        {"mensaje": "🐈 Ingresa tu nombre:\n", "type": "texto"},
        {"mensaje": "💵 ¿Cuánto deseas apostar? (mínimo $1.000):\n", "type": "dinero"}
    ]
    datos = solicitarDatos(datosBoletos)
    dineroDisponible = datos[1]

    boletosComprados = seleccionBoletos(dineroDisponible)

    nuevoUsuario = boleto(nuevoId, datos[0], datos[1])
    nuevoUsuario["boletos"] = boletosComprados

    loteria["boletos"].append(nuevoUsuario)
    print("✅ Datos registrados correctamente.")
    print("-------------------------------------")


# Diccionario principal
loteria = {
    "boletos": [],
    "ganadores" : [],
    "historial" : []
}

if __name__ == "__main__":
    comprarBoletos(loteria["boletos"])

