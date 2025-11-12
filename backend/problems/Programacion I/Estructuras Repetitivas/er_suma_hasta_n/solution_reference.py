def main():
    """Calcula la suma de todos los números de 0 hasta N"""
    n = int(input())
    
    suma = 0
    for i in range(n + 1):
        suma += i
    
    print(suma)

if __name__ == "__main__":
    main()
