def main():
    """Agenda con tuplas (día, hora) como claves"""
    agenda = {
        ("lunes", "10:00"): "Reunión",
        ("martes", "15:00"): "Clase de inglés",
        ("miércoles", "09:00"): "Dentista",
        ("jueves", "14:00"): "Gimnasio"
    }
    
    # Leer día y hora para consultar
    dia = input()
    hora = input()
    
    # Buscar en la agenda
    clave = (dia, hora)
    if clave in agenda:
        print(f"Actividad: {agenda[clave]}")
    else:
        print("No hay actividad programada")

if __name__ == "__main__":
    main()
