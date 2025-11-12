def main():
    """Verifica si una palabra termina en vocal y agrega ! si es así"""
    palabra = input()
    
    if palabra[-1] in "aeiouAEIOU":
        print(f"{palabra}!")
    else:
        print(palabra)

if __name__ == "__main__":
    main()
