def main():
    """Verifica si una persona es mayor de edad (>= 19 años)"""
    edad = int(input())
    
    if edad >= 19:
        print("Es mayor de edad")
    else:
        print("Es menor de edad")

if __name__ == "__main__":
    main()
