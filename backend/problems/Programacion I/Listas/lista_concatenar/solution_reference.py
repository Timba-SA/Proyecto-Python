def main():
    """Concatena dos listas en una sola"""
    lista1 = list(map(int, input().split()))
    lista2 = list(map(int, input().split()))
    concatenada = lista1 + lista2
    print(' '.join(map(str, concatenada)))

if __name__ == "__main__":
    main()
