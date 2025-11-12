def main():
    """Calcula el promedio de todos los elementos de una lista"""
    numeros = list(map(float, input().split()))
    promedio = sum(numeros) / len(numeros)
    print(round(promedio, 2))

if __name__ == "__main__":
    main()
