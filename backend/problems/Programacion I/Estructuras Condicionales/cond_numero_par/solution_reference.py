def main():
    """Determina si un número es par o impar"""
    numero = int(input())
    
    if numero % 2 == 0:
        print("Ha ingresado un número par")
    else:
        print("Por favor, ingrese un número par")

if __name__ == "__main__":
    main()
