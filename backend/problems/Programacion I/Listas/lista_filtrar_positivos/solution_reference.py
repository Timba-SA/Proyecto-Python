def main():
    """Filtra solo los números positivos de una lista"""
    numeros = list(map(int, input().split()))
    positivos = [n for n in numeros if n > 0]
    if positivos:
        print(' '.join(map(str, positivos)))
    else:
        print()

if __name__ == "__main__":
    main()
