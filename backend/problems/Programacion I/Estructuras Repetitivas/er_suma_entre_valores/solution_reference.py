def main():
    """Suma números entre dos valores, excluyendo los extremos"""
    num1 = int(input())
    num2 = int(input())
    
    # Asegurar que num1 sea el menor
    if num1 > num2:
        num1, num2 = num2, num1
    
    suma = 0
    for i in range(num1 + 1, num2):
        suma += i
    
    print(suma)

if __name__ == "__main__":
    main()
