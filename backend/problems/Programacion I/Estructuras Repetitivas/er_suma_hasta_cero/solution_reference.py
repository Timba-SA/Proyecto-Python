def main():
    """Suma números hasta que el usuario ingrese 0"""
    suma = 0
    
    while True:
        numero = int(input())
        if numero == 0:
            break
        suma += numero
    
    print(suma)

if __name__ == "__main__":
    main()
