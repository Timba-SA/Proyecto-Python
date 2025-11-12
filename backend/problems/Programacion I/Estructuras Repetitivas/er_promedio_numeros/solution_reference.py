def main():
    """Calcula el promedio de 100 números"""
    suma = 0
    
    for i in range(100):
        numero = int(input())
        suma += numero
    
    promedio = suma / 100
    print(promedio)

if __name__ == "__main__":
    main()
