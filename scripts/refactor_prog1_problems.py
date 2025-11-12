"""
Script para refactorizar todos los problemas de Programación I
Mejora prompts, tests, rubrics y agrega solution_reference.py
"""
import os
import json
from pathlib import Path

# Rutas base
BASE_DIR = Path(__file__).parent.parent
PROBLEMS_DIR = BASE_DIR / "backend" / "problems" / "Programacion I"

def create_solution_reference(problem_dir: Path, solution_code: str):
    """Crear archivo solution_reference.py"""
    solution_file = problem_dir / "solution_reference.py"
    solution_file.write_text(solution_code, encoding='utf-8')
    print(f"  ✅ Creado: solution_reference.py")

def update_starter_file(problem_dir: Path, starter_code: str):
    """Actualizar archivo starter.py"""
    starter_file = problem_dir / "starter.py"
    starter_file.write_text(starter_code, encoding='utf-8')
    print(f"  ✅ Actualizado: starter.py")

def update_metadata(problem_dir: Path, metadata: dict):
    """Actualizar metadata.json con hints mejorados"""
    metadata_file = problem_dir / "metadata.json"
    
    if metadata_file.exists():
        current = json.loads(metadata_file.read_text(encoding='utf-8'))
        current.update(metadata)
        metadata_file.write_text(json.dumps(current, indent=2, ensure_ascii=False), encoding='utf-8')
        print(f"  ✅ Actualizado: metadata.json")

def update_rubric(problem_dir: Path, rubric: dict):
    """Actualizar rubric.json"""
    rubric_file = problem_dir / "rubric.json"
    rubric_file.write_text(json.dumps(rubric, indent=2, ensure_ascii=False), encoding='utf-8')
    print(f"  ✅ Actualizado: rubric.json")


# ========== ESTRUCTURAS SECUENCIALES ==========

def refactor_hola_mundo():
    """Refactorizar sec_hola_mundo"""
    print("\n🔧 Refactorizando: sec_hola_mundo")
    problem_dir = PROBLEMS_DIR / "Estructuras Secuenciales" / "sec_hola_mundo"
    
    # Solution reference
    solution = '''def main():
    """Imprime 'Hola Mundo!' en pantalla"""
    print("Hola Mundo!")

if __name__ == "__main__":
    main()
'''
    create_solution_reference(problem_dir, solution)
    
    # Starter mejorado
    starter = '''def main():
    # TODO: Imprime "Hola Mundo!" usando print()
    pass

if __name__ == "__main__":
    main()
'''
    update_starter_file(problem_dir, starter)
    
    # Metadata mejorada
    metadata = {
        "hints": [
            "Necesitas usar la función print() para mostrar texto en pantalla",
            "El texto debe estar entre comillas dobles: print(\"texto aquí\")",
            "El mensaje exacto es: Hola Mundo! (con H y M mayúsculas y signo de exclamación)",
            "Solución completa: print(\"Hola Mundo!\")"
        ]
    }
    update_metadata(problem_dir, metadata)
    
    # Rubric balanceada
    rubric = {
        "tests": [
            {"name": "test_existe_funcion", "points": 2, "visibility": "public"},
            {"name": "test_mensaje_correcto", "points": 4, "visibility": "public"},
            {"name": "test_sin_entrada", "points": 2, "visibility": "public"},
            {"name": "test_formato_exacto", "points": 2, "visibility": "public"}
        ],
        "max_points": 10
    }
    update_rubric(problem_dir, rubric)


def refactor_saludo_personalizado():
    """Refactorizar sec_saludo_personalizado"""
    print("\n🔧 Refactorizando: sec_saludo_personalizado")
    problem_dir = PROBLEMS_DIR / "Estructuras Secuenciales" / "sec_saludo_personalizado"
    
    # Solution reference
    solution = '''def main():
    """Lee un nombre y muestra un saludo personalizado"""
    nombre = input()
    print(f"Hola {nombre}!")

if __name__ == "__main__":
    main()
'''
    create_solution_reference(problem_dir, solution)
    
    # Starter mejorado
    starter = '''def main():
    # TODO: Lee un nombre con input()
    # TODO: Imprime "Hola {nombre}!" usando f-string
    pass

if __name__ == "__main__":
    main()
'''
    update_starter_file(problem_dir, starter)
    
    # Metadata
    metadata = {
        "hints": [
            "Usa input() para leer el nombre del usuario: nombre = input()",
            "Usa f-strings para concatenar: print(f\"Hola {nombre}!\")",
            "También puedes usar concatenación: print(\"Hola \" + nombre + \"!\")",
            "Solución completa: nombre = input(); print(f\"Hola {nombre}!\")"
        ]
    }
    update_metadata(problem_dir, metadata)
    
    # Rubric
    rubric = {
        "tests": [
            {"name": "test_existe_funcion", "points": 1, "visibility": "public"},
            {"name": "test_saludo_juan", "points": 3, "visibility": "public"},
            {"name": "test_saludo_maria", "points": 2, "visibility": "public"},
            {"name": "test_nombre_con_espacios", "points": 2, "visibility": "hidden"},
            {"name": "test_nombre_corto", "points": 1, "visibility": "hidden"},
            {"name": "test_nombre_con_acentos", "points": 1, "visibility": "hidden"}
        ],
        "max_points": 10
    }
    update_rubric(problem_dir, rubric)


def refactor_operaciones_aritmeticas():
    """Refactorizar sec_operaciones_aritmeticas"""
    print("\n🔧 Refactorizando: sec_operaciones_aritmeticas")
    problem_dir = PROBLEMS_DIR / "Estructuras Secuenciales" / "sec_operaciones_aritmeticas"
    
    # Solution reference
    solution = '''def main():
    """Lee dos números y muestra suma, resta, multiplicación y división"""
    a = float(input())
    b = float(input())
    
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b
    
    print(suma)
    print(resta)
    print(multiplicacion)
    print(division)

if __name__ == "__main__":
    main()
'''
    create_solution_reference(problem_dir, solution)
    
    # Metadata
    metadata = {
        "hints": [
            "Lee dos números con float(input()), uno por línea: a = float(input()); b = float(input())",
            "Calcula: suma = a + b, resta = a - b, multiplicacion = a * b, division = a / b",
            "Imprime cada resultado en una línea separada con print()",
            "Orden: suma, resta, multiplicación, división (4 líneas de print)"
        ]
    }
    update_metadata(problem_dir, metadata)


def refactor_area_perimetro_circulo():
    """Refactorizar sec_area_perimetro_circulo"""
    print("\n🔧 Refactorizando: sec_area_perimetro_circulo")
    problem_dir = PROBLEMS_DIR / "Estructuras Secuenciales" / "sec_area_perimetro_circulo"
    
    # Solution reference
    solution = '''import math

def main():
    """Calcula área y perímetro de un círculo dado su radio"""
    radio = float(input())
    
    area = math.pi * radio ** 2
    perimetro = 2 * math.pi * radio
    
    print(area)
    print(perimetro)

if __name__ == "__main__":
    main()
'''
    create_solution_reference(problem_dir, solution)
    
    # Metadata
    metadata = {
        "hints": [
            "Importa el módulo math para usar math.pi: import math al inicio del archivo",
            "Lee el radio con float(input()): radio = float(input())",
            "Área = π × radio²: area = math.pi * radio ** 2",
            "Perímetro = 2 × π × radio: perimetro = 2 * math.pi * radio"
        ]
    }
    update_metadata(problem_dir, metadata)


def refactor_celsius_fahrenheit():
    """Refactorizar sec_celsius_a_fahrenheit"""
    print("\n🔧 Refactorizando: sec_celsius_a_fahrenheit")
    problem_dir = PROBLEMS_DIR / "Estructuras Secuenciales" / "sec_celsius_a_fahrenheit"
    
    # Solution reference
    solution = '''def main():
    """Convierte temperatura de Celsius a Fahrenheit"""
    celsius = float(input())
    fahrenheit = (celsius * 9/5) + 32
    print(fahrenheit)

if __name__ == "__main__":
    main()
'''
    create_solution_reference(problem_dir, solution)
    
    # Metadata
    metadata = {
        "hints": [
            "Lee la temperatura en Celsius: celsius = float(input())",
            "Fórmula: F = (C × 9/5) + 32",
            "Calcula: fahrenheit = (celsius * 9/5) + 32",
            "Imprime el resultado: print(fahrenheit)"
        ]
    }
    update_metadata(problem_dir, metadata)


# ========== MAIN ==========

def main():
    """Ejecutar todas las refactorizaciones"""
    print("=" * 60)
    print("🚀 REFACTORIZACIÓN DE PROGRAMACIÓN I")
    print("=" * 60)
    
    # Estructuras Secuenciales
    print("\n📦 ESTRUCTURAS SECUENCIALES")
    print("-" * 60)
    
    refactor_hola_mundo()
    refactor_saludo_personalizado()
    refactor_operaciones_aritmeticas()
    refactor_area_perimetro_circulo()
    refactor_celsius_fahrenheit()
    
    print("\n" + "=" * 60)
    print("✅ Refactorización completada!")
    print("=" * 60)
    print("\n📝 Próximos pasos:")
    print("  1. Revisar los archivos generados")
    print("  2. Ejecutar tests: docker compose exec backend pytest backend/problems/...")
    print("  3. Completar los problemas restantes")


if __name__ == "__main__":
    main()
