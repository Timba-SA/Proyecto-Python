def fibonacci(n):
    """Calcula el valor de Fibonacci en la posición n de forma recursiva"""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def main():
    """Muestra la serie de Fibonacci desde 0 hasta n"""
    n = int(input())
    
    serie = []
    for i in range(n + 1):
        serie.append(fibonacci(i))
    
    print(", ".join(map(str, serie)))

if __name__ == "__main__":
    main()
