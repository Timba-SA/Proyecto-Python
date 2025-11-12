def main():
    """Busca si un elemento existe en una lista"""
    numeros = list(map(int, input().split()))
    buscar = int(input())
    if buscar in numeros:
        print("Si")
    else:
        print("No")

if __name__ == "__main__":
    main()
