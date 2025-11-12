def main():
    """Agenda telefónica simple"""
    contactos = {}
    
    # Cargar 5 contactos
    for i in range(5):
        nombre = input()
        telefono = input()
        contactos[nombre] = telefono
    
    # Consultar un contacto
    nombre_buscar = input()
    if nombre_buscar in contactos:
        print(f"El número de {nombre_buscar} es: {contactos[nombre_buscar]}")
    else:
        print("Contacto no encontrado")

if __name__ == "__main__":
    main()
