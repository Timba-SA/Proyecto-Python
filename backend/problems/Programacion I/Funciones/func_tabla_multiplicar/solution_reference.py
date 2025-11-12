def tabla_multiplicar(numero):
    """Imprime la tabla de multiplicar de un número"""
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

if __name__ == "__main__":
    tabla_multiplicar(5)
