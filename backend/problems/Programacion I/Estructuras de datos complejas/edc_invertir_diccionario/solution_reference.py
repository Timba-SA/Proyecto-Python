def main():
    """Invierte un diccionario de países y capitales"""
    # Diccionario original: país -> capital
    original = {
        "Argentina": "Buenos Aires",
        "Chile": "Santiago",
        "Brasil": "Brasilia",
        "Uruguay": "Montevideo"
    }
    
    # Crear diccionario invertido: capital -> país
    invertido = {}
    for pais, capital in original.items():
        invertido[capital] = pais
    
    print(invertido)

if __name__ == "__main__":
    main()
