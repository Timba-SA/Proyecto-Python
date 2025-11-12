def main():
    """Analiza 100 números: cuenta pares, impares, positivos y negativos"""
    pares = 0
    impares = 0
    positivos = 0
    negativos = 0
    
    for i in range(100):
        numero = int(input())
        
        # Contar pares e impares
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1
        
        # Contar positivos y negativos
        if numero > 0:
            positivos += 1
        elif numero < 0:
            negativos += 1
    
    print(pares)
    print(impares)
    print(negativos)
    print(positivos)

if __name__ == "__main__":
    main()
