def potencia(base, exponente):
    """Calcula base^exponente de forma recursiva"""
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

def main():
    """Calcula y muestra la potencia de un número"""
    base = int(input())
    exponente = int(input())
    
    resultado = potencia(base, exponente)
    print(f"El resultado de {base} elevado a {exponente} es {resultado}")

if __name__ == "__main__":
    main()
