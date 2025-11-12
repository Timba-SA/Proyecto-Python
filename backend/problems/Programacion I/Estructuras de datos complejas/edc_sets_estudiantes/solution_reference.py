def main():
    """Operaciones con sets de estudiantes que aprobaron parciales"""
    # Sets de estudiantes que aprobaron cada parcial
    parcial1 = {1, 2, 3, 4, 5}
    parcial2 = {4, 5, 6, 7, 8}
    
    # Aprobaron ambos parciales (intersección)
    ambos = parcial1 & parcial2
    print(f"Aprobaron ambos: {ambos}")
    
    # Aprobaron solo uno (diferencia simétrica)
    solo_uno = parcial1 ^ parcial2
    print(f"Aprobaron solo uno: {solo_uno}")
    
    # Aprobaron al menos uno (unión)
    al_menos_uno = parcial1 | parcial2
    print(f"Aprobaron al menos uno: {al_menos_uno}")

if __name__ == "__main__":
    main()
