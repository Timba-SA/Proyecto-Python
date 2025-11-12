def suma_digitos(n):
    """Calcula la suma de los dígitos de n de forma recursiva"""
    if n == 0:
        return 0
    else:
        return (n % 10) + suma_digitos(n // 10)

def main():
    """Calcula y muestra la suma de dígitos de un número"""
    n = int(input())
    
    suma = suma_digitos(n)
    print(f"La suma de los digitos de {n} es {suma}")

if __name__ == "__main__":
    main()
