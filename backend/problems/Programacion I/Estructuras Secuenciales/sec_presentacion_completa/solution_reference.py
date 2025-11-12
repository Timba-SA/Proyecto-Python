def main():
    """Lee nombre, apellido, edad y ciudad y muestra presentación completa"""
    nombre = input()
    apellido = input()
    edad = int(input())
    ciudad = input()
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {ciudad}")

if __name__ == "__main__":
    main()
