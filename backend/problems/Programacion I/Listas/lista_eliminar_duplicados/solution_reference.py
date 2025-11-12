def main():
    """Elimina elementos duplicados y ordena la lista"""
    numeros = list(map(int, input().split()))
    unicos = sorted(set(numeros))
    print(' '.join(map(str, unicos)))

if __name__ == "__main__":
    main()
