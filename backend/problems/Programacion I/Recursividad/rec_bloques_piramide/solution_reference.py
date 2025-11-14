def contar_bloques(n):
    """Calcula el total de bloques de una pirámide usando recursión"""
    if n == 0:
        return 0
    else:
        return n + contar_bloques(n - 1)

def main():
    """Calcula y muestra el total de bloques de una pirámide"""
    n = int(input())
    
    total = contar_bloques(n)
    print(f"Para una piramide de {n} niveles se necesitan {total} bloques")

if __name__ == "__main__":
    main()
