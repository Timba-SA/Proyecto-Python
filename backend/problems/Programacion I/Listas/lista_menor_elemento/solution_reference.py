def main():
    """Encuentra el menor elemento de una lista"""
    numeros = list(map(int, input().split()))
    menor = min(numeros)
    print(menor)

if __name__ == "__main__":
    main()
