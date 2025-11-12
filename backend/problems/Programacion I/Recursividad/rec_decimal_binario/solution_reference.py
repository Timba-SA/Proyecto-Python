def decimal_a_binario(n):
    """Convierte un número decimal a binario de forma recursiva"""
    if n == 0:
        return ""
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

def main():
    """Convierte y muestra un número decimal en binario"""
    n = int(input())
    
    if n == 0:
        binario = "0"
    else:
        binario = decimal_a_binario(n)
    
    print(f"La representación binaria de {n} es {binario}")

if __name__ == "__main__":
    main()
