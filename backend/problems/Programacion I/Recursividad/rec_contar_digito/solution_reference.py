def contar_digito(numero, digito):
    """Cuenta cuántas veces aparece un dígito en un número usando recursión"""
    if numero == 0:
        return 0
    else:
        # Si el último dígito coincide, suma 1; si no, suma 0
        if numero % 10 == digito:
            return 1 + contar_digito(numero // 10, digito)
        else:
            return contar_digito(numero // 10, digito)

def main():
    """Cuenta y muestra cuántas veces aparece un dígito en un número"""
    numero = int(input())
    digito = int(input())
    
    contador = contar_digito(numero, digito)
    print(f"El digito {digito} aparece {contador} veces en el numero {numero}")

if __name__ == "__main__":
    main()
