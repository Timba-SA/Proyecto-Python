def main():
    """Calcula el promedio de notas de 3 alumnos"""
    alumnos = {}
    
    # Cargar 3 alumnos con sus 3 notas
    for i in range(3):
        nombre = input()
        nota1 = int(input())
        nota2 = int(input())
        nota3 = int(input())
        alumnos[nombre] = (nota1, nota2, nota3)
    
    # Mostrar promedio de cada alumno
    for nombre, notas in alumnos.items():
        promedio = sum(notas) / len(notas)
        print(f"{nombre}: {promedio}")

if __name__ == "__main__":
    main()
