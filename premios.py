premios = {
    1000: {
        3: 10000,
        4: 25000,
        5: 50000,
        6: 100000
    },
    2000: {
        3: 25000,
        4: 50000,
        5: 100000,
        6: 200000
    },
    5000: {
        3: 62000,
        4: 125000,
        5: 250000,
        6: 500000
    },
    10000: {
        3: 125000,
        4: 250000,
        5: 500000,
        6: 1000000
    },
    20000: {
        3: 250000,
        4: 500000,
        5: 1000000,
        6: 2000000
    }
}
categorias_premio = {
    3: "Premio pequeño",
    4: "Premio mediano",
    5: "Premio grande",
    6: "Premio mayor"
}

def obtenerCategoria(aciertos: int) -> str:
    return categorias_premio.get(aciertos, "Sin premio")

def calcularPremio(valorBoleto: int, aciertos: int) -> int:
    tablaValores = premios[valorBoleto]

    if aciertos in tablaValores:
        return tablaValores[aciertos]
    else:
        return 0 


    