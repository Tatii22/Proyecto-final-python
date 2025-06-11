import random
import compraBoletos 
from premios import calcularPremio, obtenerCategoria
from datetime import datetime
from historial import guardarHistorialLoteria, cargarHistorialLoteria, mostrarHistorialLoteria

def generarAleatoriosganador():
    numganadores = random.sample(range(1, 49), 6) 
    compraBoletos.loteria["ganadores"].append(numganadores) 

def evaluarBoletos(loteria: dict):
    if not loteria["ganadores"]:
        print("⚠️😿 No hay sorteo realizado aún.")
        return

    listaGanadora = loteria["ganadores"][0]
    print(f"✨😸 Números ganadores de la Loteria Miau: {listaGanadora}")
    
    fecha = datetime.now().strftime("%Y-%m-%d")
    resultadoHistorial = []

    for participante in loteria["boletos"]:
        print(f"🐈 Participante: {participante['nombre']}")
        boletosResultado = []

        for boleto in participante["boletos"]:
            numeros = boleto["numeros"]
            valor = boleto["valor"]
            aciertos = set(numeros) & set(listaGanadora)
            cantidad_aciertos = len(aciertos)
            premio = calcularPremio(valor, cantidad_aciertos)
            categoria = obtenerCategoria(cantidad_aciertos)

            print(f"🎟️🐱  Boleto de ${valor} con números {numeros}")
            print(f"➤ Aciertos: {cantidad_aciertos} → {sorted(aciertos)}")

            if premio > 0:
                print(f"📲 Categoría: {categoria}")
                print(f"🤑😸 ¡Premio ganado!: ${premio}\n")
            else:
                print("😿 No ganó premio.\n")

            boletosResultado.append({
                "numeros": numeros,
                "valor": valor,
                "aciertos": sorted(aciertos),
                "cantidad_aciertos": cantidad_aciertos,
                "premio": premio,
                "categoria": categoria
            })

        clienteResultado = {
            "nombre": participante["nombre"],
            "boletos": boletosResultado
        }
        resultadoHistorial.append(clienteResultado)

    sorteo = {
        "fecha": fecha,
        "ganadores": listaGanadora,
        "resultados": resultadoHistorial
    }

  
    historial_existente = cargarHistorialLoteria()
    historial_existente.append(sorteo)

 
    guardarHistorialLoteria(historial_existente)
    
    print("📜🐈‍ Historial actualizado y guardado.")
if __name__ == "__main__":
    historial = cargarHistorialLoteria()
    mostrarHistorialLoteria(historial)
    generarAleatoriosganador()
    evaluarBoletos(compraBoletos.loteria)

