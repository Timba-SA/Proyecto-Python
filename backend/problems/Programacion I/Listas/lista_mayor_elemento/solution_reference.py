def main():
    """Encuentra el mayor elemento de una lista"""
    numeros = list(map(int, input().split()))
    mayor = max(numeros)
    print(mayor)

if __name__ == "__main__":
    main()
