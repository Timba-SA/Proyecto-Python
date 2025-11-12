def es_palindromo(palabra):
    """Verifica si una palabra es palíndromo de forma recursiva"""
    # Caso base: cadena vacía o de 1 carácter
    if len(palabra) <= 1:
        return True
    
    # Si primer y último carácter son diferentes
    if palabra[0] != palabra[-1]:
        return False
    
    # Caso recursivo: verificar el resto
    return es_palindromo(palabra[1:-1])

def main():
    """Verifica y muestra si una palabra es palíndromo"""
    palabra = input().lower()
    
    if es_palindromo(palabra):
        print(f"La palabra {palabra} es un palindromo")
    else:
        print(f"La palabra {palabra} no es un palindromo")

if __name__ == "__main__":
    main()
