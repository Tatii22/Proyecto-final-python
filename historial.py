import json
from datetime import datetime

def guardarHistorialLoteria(historial, archivo='historial.json'):
    try:
        with open(archivo, 'w', encoding='utf-8') as f:
            json.dump(historial, f, ensure_ascii=False, indent=4, separators=(',', ': '))
        print("✅ Historial guardado en archivo JSON.")
    except Exception as e:
        print(f"Error al guardar el historial: {e}")


def cargarHistorialLoteria(archivo='historial.json'):
    try:
        with open(archivo, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print("Archivo no encontrado. Se creará uno nuevo.")
        return []
    except json.JSONDecodeError:
        return []

def mostrarHistorialLoteria(historial):
    if not historial:
        print("📜😿 No hay historial de sorteos.")
        return

    for i, sorteo in enumerate(historial, 1):
        print(f"\n📅 Sorteo #{i} - Fecha: {sorteo['fecha']}")
        print(f"# Números ganadores: {sorteo['ganadores']}")
        for participante in sorteo['resultados']:
            print(f"🐈 {participante['nombre']}")
            for boleto in participante['boletos']:
                print(f"  🎟️🐱  {boleto['numeros']} - Aciertos: {boleto['cantidad_aciertos']} - Premio: ${boleto['premio']} ({boleto['categoria']})")
