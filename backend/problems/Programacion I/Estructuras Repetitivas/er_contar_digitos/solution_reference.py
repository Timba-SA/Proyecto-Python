def main():
    """Cuenta la cantidad de dígitos de un número"""
    numero = int(input())
    
    # Caso especial: 0 tiene 1 dígito
    if numero == 0:
        print(1)
        return
    
    # Trabajar con valor absoluto para números negativos
    numero = abs(numero)
    
    contador = 0
    while numero > 0:
        numero = numero // 10
        contador += 1
    
    print(contador)

if __name__ == "__main__":
    main()
