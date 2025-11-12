def main():
    """Calcula la suma de todos los elementos de una lista"""
    numeros = list(map(int, input().split()))
    suma = sum(numeros)
    print(suma)

if __name__ == "__main__":
    main()
