def factorial(n):
    """Calcula el factorial de n de forma recursiva"""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def main():
    """Muestra el factorial de todos los números desde 1 hasta n"""
    n = int(input())
    
    for i in range(1, n + 1):
        resultado = factorial(i)
        print(f"El factorial de {i} es {resultado}")

if __name__ == "__main__":
    main()
