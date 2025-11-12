def operaciones_basicas(a, b):
    """Realiza las 4 operaciones básicas"""
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b
    return (suma, resta, multiplicacion, division)

if __name__ == "__main__":
    resultado = operaciones_basicas(10, 2)
    print(resultado)  # (12, 8, 20, 5.0)
