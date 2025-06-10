import random
import compraBoletos 
from premios import calcularPremio, obtenerCategoria
from datetime import datetime
import historial

def generarAleatoriosganador():
    numganadores = random.sample(range(1, 49), 6) 
    compraBoletos.loteria["ganadores"].append(numganadores) 

def evaluarBoletos(loteria: dict):
    if not loteria["ganadores"]:
        print("​⚠️ No hay sorteo realizado aún.")
        return

    listaGanadora = loteria["ganadores"][0]
    print(f"✨​ Números ganadores generados: {listaGanadora}")
    
    fecha = datetime.now().strftime("%Y-%m-%d")

    resultadoHistorial = []

    for participante in loteria["boletos"]:
        print(f"👤 Participante: {participante['nombre']}")
        boletos_resultado = []

        for boleto in participante["boletos"]:
            numeros = boleto["numeros"]
            valor = boleto["valor"]
            aciertos = set(numeros) & set(listaGanadora)
            cantidad_aciertos = len(aciertos)
            premio = calcularPremio(valor, cantidad_aciertos)
            categoria = obtenerCategoria(cantidad_aciertos)

            print(f"🎟️  Boleto de ${valor} con números {numeros}")
            print(f"➤ Aciertos: {cantidad_aciertos} → {sorted(aciertos)}")

            if premio > 0:
                print(f"🏅 Categoría: {categoria}")
                print(f"🏆 ¡Premio ganado!: ${premio}\n")
            else:
                print("🎲 No ganó premio.\n")

            boletos_resultado.append({
                "numeros": numeros,
                "valor": valor,
                "aciertos": sorted(aciertos),
                "cantidad_aciertos": cantidad_aciertos,
                "premio": premio,
                "categoria": categoria
            })

        cliente_resultado = {
            "nombre": participante["nombre"],
            "boletos": boletos_resultado
        }
        resultadoHistorial.append(cliente_resultado)


    sorteo = {
        "fecha": fecha,
        "ganadores": listaGanadora,
        "resultados": resultadoHistorial
    }
    loteria["historial"].append(sorteo)
    historial.guardarHistorial(loteria["historial"], 'historial_loteria.json')
    print("📜 Historial actualizado y guardado en 'historial_loteria.json'.")
generarAleatoriosganador()
evaluarBoletos(compraBoletos.loteria)