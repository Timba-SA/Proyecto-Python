def main():
    """Transforma nombre según opción: 1=MAYÚSCULAS, 2=minúsculas, 3=Título"""
    nombre = input()
    opcion = int(input())
    
    if opcion == 1:
        print(nombre.upper())
    elif opcion == 2:
        print(nombre.lower())
    elif opcion == 3:
        print(nombre.title())
    else:
        print("Opción inválida")

if __name__ == "__main__":
    main()
