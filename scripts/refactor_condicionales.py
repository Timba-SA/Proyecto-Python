"""
REFACTORIZACIÓN - ESTRUCTURAS CONDICIONALES
============================================
Mejora de 9 problemas de condicionales con if, elif, else
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
print("🚀 REFACTORIZACIÓN - ESTRUCTURAS CONDICIONALES")
print("="*70)

# =============================================================================
# ESTRUCTURAS CONDICIONALES
# =============================================================================

print("\n📦 2. ESTRUCTURAS CONDICIONALES")
print("-"*70)

# 2.1 cond_mayor_edad
print("\n🔧 cond_mayor_edad")
p = BASE / "Estructuras Condicionales/cond_mayor_edad"

write_file(p / "solution_reference.py", '''def main():
    """Verifica si una persona es mayor de edad (>= 18 años)"""
    edad = int(input())
    
    if edad >= 18:
        print("Mayor de edad")
    else:
        print("Menor de edad")

if __name__ == "__main__":
    main()
''')

write_file(p / "starter.py", '''def main():
    # TODO: Lee la edad con int(input())
    # TODO: Si edad >= 18, imprime "Mayor de edad"
    # TODO: Si no, imprime "Menor de edad"
    pass

if __name__ == "__main__":
    main()
''')

metadata = json.loads((p / "metadata.json").read_text(encoding='utf-8'))
metadata["hints"] = [
    "Lee la edad: edad = int(input())",
    "Usa if-else: if edad >= 18: ... else: ...",
    "Mayor de edad es >= 18 años (18 incluido)",
    "Solución: if edad >= 18: print(\"Mayor de edad\") else: print(\"Menor de edad\")"
]
write_file(p / "metadata.json", json.dumps(metadata, indent=2, ensure_ascii=False))

# 2.2 cond_numero_par
print("\n🔧 cond_numero_par")
p = BASE / "Estructuras Condicionales/cond_numero_par"

write_file(p / "solution_reference.py", '''def main():
    """Determina si un número es par o impar"""
    numero = int(input())
    
    if numero % 2 == 0:
        print("Par")
    else:
        print("Impar")

if __name__ == "__main__":
    main()
''')

write_file(p / "starter.py", '''def main():
    # TODO: Lee el número
    # TODO: Usa módulo % para verificar si es par
    # TODO: Si numero % 2 == 0, es par; si no, es impar
    pass

if __name__ == "__main__":
    main()
''')

metadata = json.loads((p / "metadata.json").read_text(encoding='utf-8'))
metadata["hints"] = [
    "Lee el número: numero = int(input())",
    "Operador módulo %: numero % 2 da el residuo de dividir entre 2",
    "Si numero % 2 == 0, el número es par (residuo 0)",
    "Si numero % 2 == 1 o != 0, el número es impar"
]
write_file(p / "metadata.json", json.dumps(metadata, indent=2, ensure_ascii=False))

# 2.3 cond_mayor_de_dos
print("\n🔧 cond_mayor_de_dos")
p = BASE / "Estructuras Condicionales/cond_mayor_de_dos"

write_file(p / "solution_reference.py", '''def main():
    """Determina el mayor de dos números"""
    a = float(input())
    b = float(input())
    
    if a > b:
        print(a)
    else:
        print(b)

if __name__ == "__main__":
    main()
''')

write_file(p / "starter.py", '''def main():
    # TODO: Lee dos números con float(input())
    # TODO: Compara con > para determinar el mayor
    # TODO: Imprime el número mayor
    pass

if __name__ == "__main__":
    main()
''')

metadata = json.loads((p / "metadata.json").read_text(encoding='utf-8'))
metadata["hints"] = [
    "Lee dos números: a = float(input()), b = float(input())",
    "Compara con >: if a > b, entonces a es mayor",
    "Si a > b imprime a, si no imprime b (cubre caso a == b también)",
    "Solución: if a > b: print(a) else: print(b)"
]
write_file(p / "metadata.json", json.dumps(metadata, indent=2, ensure_ascii=False))

# 2.4 cond_aprobado
print("\n🔧 cond_aprobado")
p = BASE / "Estructuras Condicionales/cond_aprobado"

write_file(p / "solution_reference.py", '''def main():
    """Determina si un estudiante aprobó (nota >= 6)"""
    nota = float(input())
    
    if nota >= 6:
        print("Aprobado")
    else:
        print("Reprobado")

if __name__ == "__main__":
    main()
''')

write_file(p / "starter.py", '''def main():
    # TODO: Lee la nota del estudiante
    # TODO: Si nota >= 6, imprime "Aprobado"
    # TODO: Si no, imprime "Reprobado"
    pass

if __name__ == "__main__":
    main()
''')

metadata = json.loads((p / "metadata.json").read_text(encoding='utf-8'))
metadata["hints"] = [
    "Lee la nota: nota = float(input())",
    "Condición de aprobado: nota >= 6",
    "Usa if-else para decidir el mensaje",
    "Solución: if nota >= 6: print(\"Aprobado\") else: print(\"Reprobado\")"
]
write_file(p / "metadata.json", json.dumps(metadata, indent=2, ensure_ascii=False))

# 2.5 cond_categorias_edad
print("\n🔧 cond_categorias_edad")
p = BASE / "Estructuras Condicionales/cond_categorias_edad"

write_file(p / "solution_reference.py", '''def main():
    """Clasifica persona por edad: Niño, Adolescente, Adulto, Adulto mayor"""
    edad = int(input())
    
    if edad < 13:
        print("Niño")
    elif edad < 18:
        print("Adolescente")
    elif edad < 60:
        print("Adulto")
    else:
        print("Adulto mayor")

if __name__ == "__main__":
    main()
''')

write_file(p / "starter.py", '''def main():
    # TODO: Lee la edad
    # TODO: Usa if-elif-else para clasificar:
    #       < 13: Niño
    #       13-17: Adolescente
    #       18-59: Adulto
    #       >= 60: Adulto mayor
    pass

if __name__ == "__main__":
    main()
''')

metadata = json.loads((p / "metadata.json").read_text(encoding='utf-8'))
metadata["hints"] = [
    "Usa if-elif-else para múltiples condiciones",
    "Orden: if edad < 13, elif edad < 18, elif edad < 60, else",
    "Categorías: Niño (< 13), Adolescente (13-17), Adulto (18-59), Adulto mayor (>= 60)",
    "Las condiciones deben ir de menor a mayor para funcionar correctamente"
]
write_file(p / "metadata.json", json.dumps(metadata, indent=2, ensure_ascii=False))

# 2.6 cond_terremoto
print("\n🔧 cond_terremoto")
p = BASE / "Estructuras Condicionales/cond_terremoto"

write_file(p / "solution_reference.py", '''def main():
    """Clasifica intensidad de terremoto según escala de Richter"""
    magnitud = float(input())
    
    if magnitud < 2.0:
        print("Micro")
    elif magnitud < 4.0:
        print("Menor")
    elif magnitud < 5.0:
        print("Ligero")
    elif magnitud < 6.0:
        print("Moderado")
    elif magnitud < 7.0:
        print("Fuerte")
    else:
        print("Mayor")

if __name__ == "__main__":
    main()
''')

write_file(p / "starter.py", '''def main():
    # TODO: Lee la magnitud del terremoto
    # TODO: Clasifica según rangos:
    #       < 2.0: Micro
    #       2.0-3.9: Menor
    #       4.0-4.9: Ligero
    #       5.0-5.9: Moderado
    #       6.0-6.9: Fuerte
    #       >= 7.0: Mayor
    pass

if __name__ == "__main__":
    main()
''')

metadata = json.loads((p / "metadata.json").read_text(encoding='utf-8'))
metadata["hints"] = [
    "Lee magnitud: magnitud = float(input())",
    "Usa cadena de if-elif-else con 6 categorías",
    "Condiciones: < 2.0, < 4.0, < 5.0, < 6.0, < 7.0, >= 7.0",
    "Categorías: Micro, Menor, Ligero, Moderado, Fuerte, Mayor"
]
write_file(p / "metadata.json", json.dumps(metadata, indent=2, ensure_ascii=False))

# 2.7 cond_termina_vocal
print("\n🔧 cond_termina_vocal")
p = BASE / "Estructuras Condicionales/cond_termina_vocal"

write_file(p / "solution_reference.py", '''def main():
    """Verifica si una palabra termina en vocal"""
    palabra = input()
    ultima_letra = palabra[-1].lower()
    
    if ultima_letra in "aeiou":
        print("Termina en vocal")
    else:
        print("No termina en vocal")

if __name__ == "__main__":
    main()
''')

write_file(p / "starter.py", '''def main():
    # TODO: Lee la palabra
    # TODO: Obtén la última letra: palabra[-1]
    # TODO: Verifica si está en "aeiou" usando operador in
    pass

if __name__ == "__main__":
    main()
''')

metadata = json.loads((p / "metadata.json").read_text(encoding='utf-8'))
metadata["hints"] = [
    "Lee la palabra: palabra = input()",
    "Última letra: palabra[-1] (índice negativo desde el final)",
    "Convierte a minúscula: palabra[-1].lower() para comparar",
    "Usa operador in: if ultima_letra in \"aeiou\""
]
write_file(p / "metadata.json", json.dumps(metadata, indent=2, ensure_ascii=False))

# 2.8 cond_transformar_nombre
print("\n🔧 cond_transformar_nombre")
p = BASE / "Estructuras Condicionales/cond_transformar_nombre"

write_file(p / "solution_reference.py", '''def main():
    """Transforma nombre según longitud"""
    nombre = input()
    
    if len(nombre) < 5:
        print(nombre.upper())
    else:
        print(nombre.lower())

if __name__ == "__main__":
    main()
''')

write_file(p / "starter.py", '''def main():
    # TODO: Lee el nombre
    # TODO: Si len(nombre) < 5, imprime en mayúsculas (upper())
    # TODO: Si no, imprime en minúsculas (lower())
    pass

if __name__ == "__main__":
    main()
''')

metadata = json.loads((p / "metadata.json").read_text(encoding='utf-8'))
metadata["hints"] = [
    "Lee el nombre: nombre = input()",
    "Usa len(nombre) para obtener la longitud",
    "Métodos de string: upper() para mayúsculas, lower() para minúsculas",
    "if len(nombre) < 5: print(nombre.upper()) else: print(nombre.lower())"
]
write_file(p / "metadata.json", json.dumps(metadata, indent=2, ensure_ascii=False))

# 2.9 cond_validar_password
print("\n🔧 cond_validar_password")
p = BASE / "Estructuras Condicionales/cond_validar_password"

write_file(p / "solution_reference.py", '''def main():
    """Valida que la contraseña tenga entre 8 y 14 caracteres"""
    password = input()
    
    if 8 <= len(password) <= 14:
        print("Ha ingresado una contraseña correcta")
    else:
        print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

if __name__ == "__main__":
    main()
''')

write_file(p / "starter.py", '''def main():
    # TODO: Lee la contraseña
    # TODO: Verifica que len(password) esté entre 8 y 14 (inclusivo)
    # TODO: Usa comparación encadenada: 8 <= len(password) <= 14
    pass

if __name__ == "__main__":
    main()
''')

metadata = json.loads((p / "metadata.json").read_text(encoding='utf-8'))
metadata["hints"] = [
    "Lee la contraseña: password = input()",
    "Rango válido: 8 <= longitud <= 14 (ambos inclusivos)",
    "Python permite comparación encadenada: 8 <= len(password) <= 14",
    "Mensaje éxito: 'Ha ingresado una contraseña correcta', error: 'Por favor, ingrese una contraseña de entre 8 y 14 caracteres'"
]
write_file(p / "metadata.json", json.dumps(metadata, indent=2, ensure_ascii=False))

print("\n" + "="*70)
print("✅ REFACTORIZACIÓN COMPLETADA - ESTRUCTURAS CONDICIONALES (9/9)")
print("="*70)

print("\n📊 Resumen:")
print("  ✅ 9 solution_reference.py creados")
print("  ✅ 9 starter.py mejorados con TODOs")
print("  ✅ 9 metadata.json actualizados con hints")

print("\n" + "="*70)
print("🎉 PROGRAMACIÓN I - 100% REFACTORIZADO")
print("="*70)
print("\n📈 Total:")
print("  ✅ 19 solution_reference.py creados")
print("  ✅ 19 starter.py mejorados")
print("  ✅ 19 metadata.json actualizados")
print("\n🚀 Listo para usar!")
