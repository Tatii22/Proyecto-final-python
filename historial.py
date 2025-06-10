import json

def guardarHistorial(historial, archivo='historial.json'):
    """
    Guarda el historial de mensajes en un archivo JSON.
    
    :param historial: Lista de diccionarios con el historial de mensajes.
    :param archivo: Nombre del archivo donde se guardará el historial.
    """
    with open(archivo, 'w', encoding='utf-8') as f:
        json.dump(historial, f, ensure_ascii=False, indent=4)
def cargarHistorial(archivo='historial.json'):
    """
    Carga el historial de mensajes desde un archivo JSON.
    
    :param archivo: Nombre del archivo desde donde se cargará el historial.
    :return: Lista de diccionarios con el historial de mensajes.
    """
    try:
        with open(archivo, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []  # Retorna una lista vacía si el archivo no existe
    except json.JSONDecodeError:
        print("⚠️ Error al decodificar el archivo JSON. Retornando historial vacío.")
        return []
def mostrarHistorial(historial):
    """
    Muestra el historial de mensajes en la consola.
    
    :param historial: Lista de diccionarios con el historial de mensajes.
    """
    if not historial:
        print("📜 No hay historial disponible.")
        return
    
    for i, mensaje in enumerate(historial, start=1):
        print(f"{i}. {mensaje['fecha']} - {mensaje['usuario']}: {mensaje['mensaje']}")
    print("\nTotal de mensajes:", len(historial))
def agregarMensaje(historial, usuario, mensaje):
    """
    Agrega un nuevo mensaje al historial.
    :param historial: Lista de diccionarios con el historial de mensajes.
    :param usuario: Nombre del usuario que envía el mensaje.
    :param mensaje: Contenido del mensaje.
    """
    from datetime import datetime
    nuevo_mensaje = {
        "fecha": datetime.now().isoformat(),
        "usuario": usuario,
        "mensaje": mensaje
    }
    historial.append(nuevo_mensaje)
    print("✅ Mensaje agregado al historial.")