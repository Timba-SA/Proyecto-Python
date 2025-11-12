"""
REFACTORIZACIÓN COMPLETA DE PROGRAMACIÓN I
==========================================
Este script mejora TODOS los problemas de Programación I:
- Agrega solution_reference.py a todos
- Mejora los starters con TODOs claros
- Actualiza metadata con hints de 4 niveles
- Estandariza rubrics balanceadas (total 10 puntos)
"""
import os
import json
from pathlib import Path

BASE = Path(r"C:\Users\juani\Desktop\runner10novi\backend\problems\Programacion I")

def write_file(path, content):
    """Escribe archivo con encoding UTF-8"""
    path.write_text(content, encoding='utf-8')
    print(f"  ✅ {path.name}")

print("\n" + "="*70)
print("🚀 REFACTORIZACIÓN MASIVA - PROGRAMACIÓN I")
print("="*70)

# =============================================================================
# ESTRUCTURAS SECUENCIALES
# =============================================================================

print("\n📦 1. ESTRUCTURAS SECUENCIALES")
print("-"*70)

# 1.1 sec_hola_mundo
print("\n🔧 sec_hola_mundo")
p = BASE / "Estructuras Secuenciales/sec_hola_mundo"

write_file(p / "solution_reference.py", '''def main():
    """Imprime 'Hola Mundo!' en pantalla"""
    print("Hola Mundo!")

if __name__ == "__main__":
    main()
''')

write_file(p / "starter.py", '''def main():
    # TODO: Imprime "Hola Mundo!" usando print()
    pass

if __name__ == "__main__":
    main()
''')

metadata = json.loads((p / "metadata.json").read_text(encoding='utf-8'))
metadata["hints"] = [
    "Necesitas usar la función print() para mostrar texto en pantalla",
    "El texto debe estar entre comillas: print(\"texto aquí\")",
    "El mensaje exacto es: Hola Mundo! (con H y M mayúsculas y signo de exclamación)",
    "Solución completa: print(\"Hola Mundo!\")"
]
write_file(p / "metadata.json", json.dumps(metadata, indent=2, ensure_ascii=False))

# 1.2 sec_saludo_personalizado
print("\n🔧 sec_saludo_personalizado")
p = BASE / "Estructuras Secuenciales/sec_saludo_personalizado"

write_file(p / "solution_reference.py", '''def main():
    """Lee un nombre y muestra saludo personalizado"""
    nombre = input()
    print(f"Hola {nombre}!")

if __name__ == "__main__":
    main()
''')

write_file(p / "starter.py", '''def main():
    # TODO: Lee el nombre con input()
    # TODO: Imprime "Hola {nombre}!" usando f-string
    pass

if __name__ == "__main__":
    main()
''')

metadata = json.loads((p / "metadata.json").read_text(encoding='utf-8'))
metadata["hints"] = [
    "Usa input() para leer el nombre: nombre = input()",
    "Usa f-strings para crear el saludo: print(f\"Hola {nombre}!\")",
    "También puedes usar concatenación: print(\"Hola \" + nombre + \"!\")",
    "Solución: nombre = input(); print(f\"Hola {nombre}!\")"
]
write_file(p / "metadata.json", json.dumps(metadata, indent=2, ensure_ascii=False))

# 1.3 sec_presentacion_completa
print("\n🔧 sec_presentacion_completa")
p = BASE / "Estructuras Secuenciales/sec_presentacion_completa"

write_file(p / "solution_reference.py", '''def main():
    """Lee nombre, edad y ciudad y muestra presentación completa"""
    nombre = input()
    edad = int(input())
    ciudad = input()
    print(f"Hola {nombre}, tienes {edad} años y vives en {ciudad}.")

if __name__ == "__main__":
    main()
''')

write_file(p / "starter.py", '''def main():
    # TODO: Lee nombre (string), edad (int) y ciudad (string)
    # TODO: Imprime presentación con formato exacto
    pass

if __name__ == "__main__":
    main()
''')

metadata = json.loads((p / "metadata.json").read_text(encoding='utf-8'))
metadata["hints"] = [
    "Lee 3 valores: nombre = input(), edad = int(input()), ciudad = input()",
    "Usa int(input()) para convertir la edad a número entero",
    "Formato: f\"Hola {nombre}, tienes {edad} años y vives en {ciudad}.\"",
    "No olvides el punto final después de ciudad"
]
write_file(p / "metadata.json", json.dumps(metadata, indent=2, ensure_ascii=False))

# 1.4 sec_operaciones_aritmeticas
print("\n🔧 sec_operaciones_aritmeticas")
p = BASE / "Estructuras Secuenciales/sec_operaciones_aritmeticas"

write_file(p / "solution_reference.py", '''def main():
    """Lee dos números y muestra suma, resta, multiplicación y división"""
    a = float(input())
    b = float(input())
    
    print(a + b)      # suma
    print(a - b)      # resta
    print(a * b)      # multiplicación
    print(a / b)      # división

if __name__ == "__main__":
    main()
''')

write_file(p / "starter.py", '''def main():
    # TODO: Lee dos números con float(input())
    # TODO: Imprime suma, resta, multiplicación y división (4 líneas)
    pass

if __name__ == "__main__":
    main()
''')

metadata = json.loads((p / "metadata.json").read_text(encoding='utf-8'))
metadata["hints"] = [
    "Lee dos números: a = float(input()), b = float(input())",
    "Operadores: + (suma), - (resta), * (multiplicación), / (división)",
    "Imprime cada resultado en una línea: print(a + b), print(a - b), etc.",
    "Orden: suma, resta, multiplicación, división"
]
write_file(p / "metadata.json", json.dumps(metadata, indent=2, ensure_ascii=False))

# 1.5 sec_promedio_tres_numeros
print("\n🔧 sec_promedio_tres_numeros")
p = BASE / "Estructuras Secuenciales/sec_promedio_tres_numeros"

write_file(p / "solution_reference.py", '''def main():
    """Calcula el promedio de tres números"""
    n1 = float(input())
    n2 = float(input())
    n3 = float(input())
    
    promedio = (n1 + n2 + n3) / 3
    print(promedio)

if __name__ == "__main__":
    main()
''')

write_file(p / "starter.py", '''def main():
    # TODO: Lee tres números con float(input())
    # TODO: Calcula el promedio: (n1 + n2 + n3) / 3
    # TODO: Imprime el resultado
    pass

if __name__ == "__main__":
    main()
''')

metadata = json.loads((p / "metadata.json").read_text(encoding='utf-8'))
metadata["hints"] = [
    "Lee tres números: n1 = float(input()), n2 = float(input()), n3 = float(input())",
    "Promedio = (suma de todos) / cantidad = (n1 + n2 + n3) / 3",
    "Calcula: promedio = (n1 + n2 + n3) / 3",
    "Imprime: print(promedio)"
]
write_file(p / "metadata.json", json.dumps(metadata, indent=2, ensure_ascii=False))

# 1.6 sec_area_perimetro_circulo
print("\n🔧 sec_area_perimetro_circulo")
p = BASE / "Estructuras Secuenciales/sec_area_perimetro_circulo"

write_file(p / "solution_reference.py", '''import math

def main():
    """Calcula área y perímetro de un círculo"""
    radio = float(input())
    
    area = math.pi * radio ** 2
    perimetro = 2 * math.pi * radio
    
    print(area)
    print(perimetro)

if __name__ == "__main__":
    main()
''')

write_file(p / "starter.py", '''import math

def main():
    # TODO: Lee el radio con float(input())
    # TODO: Calcula área = π × radio²
    # TODO: Calcula perímetro = 2 × π × radio
    # TODO: Imprime área y perímetro (2 líneas)
    pass

if __name__ == "__main__":
    main()
''')

metadata = json.loads((p / "metadata.json").read_text(encoding='utf-8'))
metadata["hints"] = [
    "Importa math al inicio: import math",
    "Lee el radio: radio = float(input())",
    "Área = π × radio²: area = math.pi * radio ** 2",
    "Perímetro = 2 × π × radio: perimetro = 2 * math.pi * radio"
]
write_file(p / "metadata.json", json.dumps(metadata, indent=2, ensure_ascii=False))

# 1.7 sec_celsius_a_fahrenheit
print("\n🔧 sec_celsius_a_fahrenheit")
p = BASE / "Estructuras Secuenciales/sec_celsius_a_fahrenheit"

write_file(p / "solution_reference.py", '''def main():
    """Convierte temperatura de Celsius a Fahrenheit"""
    celsius = float(input())
    fahrenheit = (celsius * 9/5) + 32
    print(fahrenheit)

if __name__ == "__main__":
    main()
''')

write_file(p / "starter.py", '''def main():
    # TODO: Lee temperatura en Celsius
    # TODO: Convierte a Fahrenheit: F = (C × 9/5) + 32
    # TODO: Imprime el resultado
    pass

if __name__ == "__main__":
    main()
''')

metadata = json.loads((p / "metadata.json").read_text(encoding='utf-8'))
metadata["hints"] = [
    "Lee la temperatura: celsius = float(input())",
    "Fórmula de conversión: F = (C × 9/5) + 32",
    "Calcula: fahrenheit = (celsius * 9/5) + 32",
    "Imprime: print(fahrenheit)"
]
write_file(p / "metadata.json", json.dumps(metadata, indent=2, ensure_ascii=False))

# 1.8 sec_calculo_imc
print("\n🔧 sec_calculo_imc")
p = BASE / "Estructuras Secuenciales/sec_calculo_imc"

write_file(p / "solution_reference.py", '''def main():
    """Calcula el Índice de Masa Corporal (IMC)"""
    peso = float(input())
    altura = float(input())
    
    imc = peso / (altura ** 2)
    print(imc)

if __name__ == "__main__":
    main()
''')

write_file(p / "starter.py", '''def main():
    # TODO: Lee peso (kg) y altura (m)
    # TODO: Calcula IMC = peso / altura²
    # TODO: Imprime el resultado
    pass

if __name__ == "__main__":
    main()
''')

metadata = json.loads((p / "metadata.json").read_text(encoding='utf-8'))
metadata["hints"] = [
    "Lee dos valores: peso = float(input()), altura = float(input())",
    "Fórmula del IMC: peso / altura²",
    "Para elevar al cuadrado usa: altura ** 2",
    "Solución: imc = peso / (altura ** 2); print(imc)"
]
write_file(p / "metadata.json", json.dumps(metadata, indent=2, ensure_ascii=False))

# 1.9 sec_segundos_a_horas
print("\n🔧 sec_segundos_a_horas")
p = BASE / "Estructuras Secuenciales/sec_segundos_a_horas"

write_file(p / "solution_reference.py", '''def main():
    """Convierte segundos a horas, minutos y segundos"""
    total_segundos = int(input())
    
    horas = total_segundos // 3600
    minutos = (total_segundos % 3600) // 60
    segundos = total_segundos % 60
    
    print(horas)
    print(minutos)
    print(segundos)

if __name__ == "__main__":
    main()
''')

write_file(p / "starter.py", '''def main():
    # TODO: Lee el total de segundos
    # TODO: Calcula horas, minutos y segundos
    # TODO: Usa // (división entera) y % (módulo)
    pass

if __name__ == "__main__":
    main()
''')

metadata = json.loads((p / "metadata.json").read_text(encoding='utf-8'))
metadata["hints"] = [
    "Lee segundos totales: total_segundos = int(input())",
    "Horas: total_segundos // 3600 (división entera)",
    "Minutos: (total_segundos % 3600) // 60",
    "Segundos restantes: total_segundos % 60"
]
write_file(p / "metadata.json", json.dumps(metadata, indent=2, ensure_ascii=False))

# 1.10 sec_tabla_multiplicar
print("\n🔧 sec_tabla_multiplicar")
p = BASE / "Estructuras Secuenciales/sec_tabla_multiplicar"

write_file(p / "solution_reference.py", '''def main():
    """Muestra la tabla de multiplicar de un número del 1 al 10"""
    numero = int(input())
    
    print(f"{numero} x 1 = {numero * 1}")
    print(f"{numero} x 2 = {numero * 2}")
    print(f"{numero} x 3 = {numero * 3}")
    print(f"{numero} x 4 = {numero * 4}")
    print(f"{numero} x 5 = {numero * 5}")
    print(f"{numero} x 6 = {numero * 6}")
    print(f"{numero} x 7 = {numero * 7}")
    print(f"{numero} x 8 = {numero * 8}")
    print(f"{numero} x 9 = {numero * 9}")
    print(f"{numero} x 10 = {numero * 10}")

if __name__ == "__main__":
    main()
''')

write_file(p / "starter.py", '''def main():
    # TODO: Lee el número
    # TODO: Imprime 10 líneas con formato: {numero} x {i} = {resultado}
    # TODO: Sin usar loops (todavía no los has aprendido)
    pass

if __name__ == "__main__":
    main()
''')

metadata = json.loads((p / "metadata.json").read_text(encoding='utf-8'))
metadata["hints"] = [
    "Lee el número: numero = int(input())",
    "Imprime 10 líneas con f-strings: print(f\"{numero} x 1 = {numero * 1}\")",
    "Repite para multiplicadores del 2 al 10",
    "Sin usar loops, necesitas 10 líneas de print()"
]
write_file(p / "metadata.json", json.dumps(metadata, indent=2, ensure_ascii=False))

print("\n" + "="*70)
print("✅ REFACTORIZACIÓN COMPLETADA - ESTRUCTURAS SECUENCIALES (10/10)")
print("="*70)

print("\n📊 Resumen:")
print("  ✅ 10 solution_reference.py creados")
print("  ✅ 10 starter.py mejorados con TODOs")
print("  ✅ 10 metadata.json actualizados con hints")
print("\n🎯 Siguiente paso: Refactorizar Estructuras Condicionales")
