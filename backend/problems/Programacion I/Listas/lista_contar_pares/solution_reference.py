def main():
    """Cuenta cuántos números pares hay en una lista"""
    numeros = list(map(int, input().split()))
    contador = sum(1 for n in numeros if n % 2 == 0)
    print(contador)

if __name__ == "__main__":
    main()
