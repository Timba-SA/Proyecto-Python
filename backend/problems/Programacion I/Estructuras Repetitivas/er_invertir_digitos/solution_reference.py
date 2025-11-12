def main():
    """Invierte el orden de los dígitos de un número"""
    numero = int(input())
    
    invertido = 0
    
    while numero > 0:
        digito = numero % 10
        invertido = invertido * 10 + digito
        numero = numero // 10
    
    print(invertido)

if __name__ == "__main__":
    main()
