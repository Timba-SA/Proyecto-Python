def main():
    """Analiza palabras únicas y cuenta repeticiones"""
    frase = input()
    palabras = frase.split()
    
    # Palabras únicas usando set
    palabras_unicas = set(palabras)
    print(f"Palabras únicas: {palabras_unicas}")
    
    # Contar apariciones
    recuento = {}
    for palabra in palabras:
        if palabra in recuento:
            recuento[palabra] += 1
        else:
            recuento[palabra] = 1
    
    print(f"Recuento: {recuento}")

if __name__ == "__main__":
    main()
