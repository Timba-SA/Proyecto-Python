def main():
    """Invierte el orden de los elementos de una lista"""
    numeros = list(map(int, input().split()))
    numeros.reverse()
    print(' '.join(map(str, numeros)))

if __name__ == "__main__":
    main()
