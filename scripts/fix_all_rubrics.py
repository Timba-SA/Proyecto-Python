"""
CORRECCIÓN DE RÚBRICAS - PROGRAMACIÓN I
========================================
Actualiza todas las rúbricas para que coincidan con los tests reales
y estén balanceadas correctamente (total 10 puntos)
"""
import os
import json
from pathlib import Path

BASE = Path(r"C:\Users\juani\Desktop\runner10novi\backend\problems\Programacion I")

def write_file(path, content):
    """Escribe archivo con encoding UTF-8"""
    path.write_text(content, encoding='utf-8')
    print(f"  ✅ {path.parent.name}/rubric.json")

print("\n" + "="*70)
print("🔧 CORRECCIÓN DE RÚBRICAS - PROGRAMACIÓN I")
print("="*70)

# =============================================================================
# ESTRUCTURAS SECUENCIALES - RÚBRICAS CORREGIDAS
# =============================================================================

print("\n📦 ESTRUCTURAS SECUENCIALES")
print("-"*70)

# 1. sec_hola_mundo
p = BASE / "Estructuras Secuenciales/sec_hola_mundo"
rubric = {
    "tests": [
        {"name": "test_existe_funcion", "points": 2, "visibility": "public"},
        {"name": "test_mensaje_correcto", "points": 4, "visibility": "public"},
        {"name": "test_sin_entrada", "points": 2, "visibility": "public"},
        {"name": "test_formato_exacto", "points": 2, "visibility": "hidden"}
    ],
    "max_points": 10
}
write_file(p / "rubric.json", json.dumps(rubric, indent=2, ensure_ascii=False))

# 2. sec_saludo_personalizado
p = BASE / "Estructuras Secuenciales/sec_saludo_personalizado"
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
write_file(p / "rubric.json", json.dumps(rubric, indent=2, ensure_ascii=False))

# 3. sec_presentacion_completa
p = BASE / "Estructuras Secuenciales/sec_presentacion_completa"
rubric = {
    "tests": [
        {"name": "test_existe_funcion", "points": 1, "visibility": "public"},
        {"name": "test_presentacion_basica", "points": 3, "visibility": "public"},
        {"name": "test_presentacion_diferente", "points": 2, "visibility": "public"},
        {"name": "test_con_acentos", "points": 2, "visibility": "hidden"},
        {"name": "test_edad_mayor", "points": 1, "visibility": "hidden"},
        {"name": "test_ciudad_larga", "points": 1, "visibility": "hidden"}
    ],
    "max_points": 10
}
write_file(p / "rubric.json", json.dumps(rubric, indent=2, ensure_ascii=False))

# 4. sec_operaciones_aritmeticas
p = BASE / "Estructuras Secuenciales/sec_operaciones_aritmeticas"
rubric = {
    "tests": [
        {"name": "test_existe_funcion", "points": 1, "visibility": "public"},
        {"name": "test_suma", "points": 2, "visibility": "public"},
        {"name": "test_resta", "points": 2, "visibility": "public"},
        {"name": "test_multiplicacion", "points": 2, "visibility": "public"},
        {"name": "test_division", "points": 2, "visibility": "hidden"},
        {"name": "test_negativos", "points": 1, "visibility": "hidden"}
    ],
    "max_points": 10
}
write_file(p / "rubric.json", json.dumps(rubric, indent=2, ensure_ascii=False))

# 5. sec_promedio_tres_numeros
p = BASE / "Estructuras Secuenciales/sec_promedio_tres_numeros"
rubric = {
    "tests": [
        {"name": "test_existe_funcion", "points": 1, "visibility": "public"},
        {"name": "test_promedio_simple", "points": 3, "visibility": "public"},
        {"name": "test_promedio_decimal", "points": 3, "visibility": "public"},
        {"name": "test_promedio_negativos", "points": 2, "visibility": "hidden"},
        {"name": "test_promedio_cero", "points": 1, "visibility": "hidden"}
    ],
    "max_points": 10
}
write_file(p / "rubric.json", json.dumps(rubric, indent=2, ensure_ascii=False))

# 6. sec_area_perimetro_circulo - ¡ESTE ES EL PROBLEMA!
p = BASE / "Estructuras Secuenciales/sec_area_perimetro_circulo"
rubric = {
    "tests": [
        {"name": "test_existe_funcion", "points": 1, "visibility": "public"},
        {"name": "test_radio_5", "points": 2, "visibility": "public"},
        {"name": "test_radio_1", "points": 2, "visibility": "public"},
        {"name": "test_radio_10", "points": 1, "visibility": "public"},
        {"name": "test_radio_0", "points": 1, "visibility": "hidden"},
        {"name": "test_radio_1000", "points": 1, "visibility": "hidden"},
        {"name": "test_radio_2_5_decimal", "points": 1, "visibility": "hidden"},
        {"name": "test_radio_3_7_decimal", "points": 1, "visibility": "hidden"}
    ],
    "max_points": 10
}
write_file(p / "rubric.json", json.dumps(rubric, indent=2, ensure_ascii=False))

# 7. sec_celsius_a_fahrenheit
p = BASE / "Estructuras Secuenciales/sec_celsius_a_fahrenheit"
rubric = {
    "tests": [
        {"name": "test_existe_funcion", "points": 1, "visibility": "public"},
        {"name": "test_cero_celsius", "points": 2, "visibility": "public"},
        {"name": "test_100_celsius", "points": 2, "visibility": "public"},
        {"name": "test_temperatura_negativa", "points": 2, "visibility": "hidden"},
        {"name": "test_temperatura_decimal", "points": 2, "visibility": "hidden"},
        {"name": "test_temperatura_extrema", "points": 1, "visibility": "hidden"}
    ],
    "max_points": 10
}
write_file(p / "rubric.json", json.dumps(rubric, indent=2, ensure_ascii=False))

# 8. sec_calculo_imc
p = BASE / "Estructuras Secuenciales/sec_calculo_imc"
rubric = {
    "tests": [
        {"name": "test_existe_funcion", "points": 1, "visibility": "public"},
        {"name": "test_imc_normal", "points": 3, "visibility": "public"},
        {"name": "test_imc_sobrepeso", "points": 2, "visibility": "public"},
        {"name": "test_imc_bajo_peso", "points": 2, "visibility": "hidden"},
        {"name": "test_imc_obesidad", "points": 1, "visibility": "hidden"},
        {"name": "test_imc_decimal", "points": 1, "visibility": "hidden"}
    ],
    "max_points": 10
}
write_file(p / "rubric.json", json.dumps(rubric, indent=2, ensure_ascii=False))

# 9. sec_segundos_a_horas
p = BASE / "Estructuras Secuenciales/sec_segundos_a_horas"
rubric = {
    "tests": [
        {"name": "test_existe_funcion", "points": 1, "visibility": "public"},
        {"name": "test_conversion_simple", "points": 3, "visibility": "public"},
        {"name": "test_una_hora", "points": 2, "visibility": "public"},
        {"name": "test_varios_dias", "points": 2, "visibility": "hidden"},
        {"name": "test_solo_segundos", "points": 1, "visibility": "hidden"},
        {"name": "test_solo_minutos", "points": 1, "visibility": "hidden"}
    ],
    "max_points": 10
}
write_file(p / "rubric.json", json.dumps(rubric, indent=2, ensure_ascii=False))

# 10. sec_tabla_multiplicar
p = BASE / "Estructuras Secuenciales/sec_tabla_multiplicar"
rubric = {
    "tests": [
        {"name": "test_existe_funcion", "points": 1, "visibility": "public"},
        {"name": "test_tabla_5", "points": 3, "visibility": "public"},
        {"name": "test_tabla_1", "points": 2, "visibility": "public"},
        {"name": "test_tabla_10", "points": 2, "visibility": "hidden"},
        {"name": "test_tabla_negativo", "points": 1, "visibility": "hidden"},
        {"name": "test_formato_exacto", "points": 1, "visibility": "hidden"}
    ],
    "max_points": 10
}
write_file(p / "rubric.json", json.dumps(rubric, indent=2, ensure_ascii=False))

# =============================================================================
# ESTRUCTURAS CONDICIONALES - RÚBRICAS CORREGIDAS
# =============================================================================

print("\n📦 ESTRUCTURAS CONDICIONALES")
print("-"*70)

# 1. cond_mayor_edad
p = BASE / "Estructuras Condicionales/cond_mayor_edad"
rubric = {
    "tests": [
        {"name": "test_existe_funcion", "points": 1, "visibility": "public"},
        {"name": "test_mayor_edad_18", "points": 2, "visibility": "public"},
        {"name": "test_mayor_edad_25", "points": 2, "visibility": "public"},
        {"name": "test_menor_edad_17", "points": 2, "visibility": "public"},
        {"name": "test_menor_edad_10", "points": 2, "visibility": "hidden"},
        {"name": "test_limite_edad", "points": 1, "visibility": "hidden"}
    ],
    "max_points": 10
}
write_file(p / "rubric.json", json.dumps(rubric, indent=2, ensure_ascii=False))

# 2. cond_numero_par
p = BASE / "Estructuras Condicionales/cond_numero_par"
rubric = {
    "tests": [
        {"name": "test_existe_funcion", "points": 1, "visibility": "public"},
        {"name": "test_par_positivo", "points": 2, "visibility": "public"},
        {"name": "test_impar_positivo", "points": 2, "visibility": "public"},
        {"name": "test_cero", "points": 2, "visibility": "public"},
        {"name": "test_par_negativo", "points": 2, "visibility": "hidden"},
        {"name": "test_impar_negativo", "points": 1, "visibility": "hidden"}
    ],
    "max_points": 10
}
write_file(p / "rubric.json", json.dumps(rubric, indent=2, ensure_ascii=False))

# 3. cond_mayor_de_dos
p = BASE / "Estructuras Condicionales/cond_mayor_de_dos"
rubric = {
    "tests": [
        {"name": "test_existe_funcion", "points": 1, "visibility": "public"},
        {"name": "test_primer_numero_mayor", "points": 2, "visibility": "public"},
        {"name": "test_segundo_numero_mayor", "points": 2, "visibility": "public"},
        {"name": "test_numeros_iguales", "points": 2, "visibility": "public"},
        {"name": "test_negativos", "points": 2, "visibility": "hidden"},
        {"name": "test_decimales", "points": 1, "visibility": "hidden"}
    ],
    "max_points": 10
}
write_file(p / "rubric.json", json.dumps(rubric, indent=2, ensure_ascii=False))

# 4. cond_aprobado
p = BASE / "Estructuras Condicionales/cond_aprobado"
rubric = {
    "tests": [
        {"name": "test_existe_funcion", "points": 1, "visibility": "public"},
        {"name": "test_aprobado_6", "points": 2, "visibility": "public"},
        {"name": "test_aprobado_10", "points": 2, "visibility": "public"},
        {"name": "test_reprobado_5", "points": 2, "visibility": "public"},
        {"name": "test_reprobado_0", "points": 2, "visibility": "hidden"},
        {"name": "test_nota_decimal", "points": 1, "visibility": "hidden"}
    ],
    "max_points": 10
}
write_file(p / "rubric.json", json.dumps(rubric, indent=2, ensure_ascii=False))

# 5. cond_categorias_edad
p = BASE / "Estructuras Condicionales/cond_categorias_edad"
rubric = {
    "tests": [
        {"name": "test_existe_funcion", "points": 1, "visibility": "public"},
        {"name": "test_nino", "points": 2, "visibility": "public"},
        {"name": "test_adolescente", "points": 2, "visibility": "public"},
        {"name": "test_adulto", "points": 2, "visibility": "public"},
        {"name": "test_adulto_mayor", "points": 2, "visibility": "hidden"},
        {"name": "test_limites", "points": 1, "visibility": "hidden"}
    ],
    "max_points": 10
}
write_file(p / "rubric.json", json.dumps(rubric, indent=2, ensure_ascii=False))

# 6. cond_terremoto
p = BASE / "Estructuras Condicionales/cond_terremoto"
rubric = {
    "tests": [
        {"name": "test_existe_funcion", "points": 1, "visibility": "public"},
        {"name": "test_micro", "points": 1, "visibility": "public"},
        {"name": "test_menor", "points": 1, "visibility": "public"},
        {"name": "test_ligero", "points": 2, "visibility": "public"},
        {"name": "test_moderado", "points": 2, "visibility": "hidden"},
        {"name": "test_fuerte", "points": 2, "visibility": "hidden"},
        {"name": "test_mayor", "points": 1, "visibility": "hidden"}
    ],
    "max_points": 10
}
write_file(p / "rubric.json", json.dumps(rubric, indent=2, ensure_ascii=False))

# 7. cond_termina_vocal
p = BASE / "Estructuras Condicionales/cond_termina_vocal"
rubric = {
    "tests": [
        {"name": "test_existe_funcion", "points": 1, "visibility": "public"},
        {"name": "test_termina_a", "points": 2, "visibility": "public"},
        {"name": "test_termina_consonante", "points": 2, "visibility": "public"},
        {"name": "test_mayuscula", "points": 2, "visibility": "hidden"},
        {"name": "test_palabra_corta", "points": 2, "visibility": "hidden"},
        {"name": "test_palabra_larga", "points": 1, "visibility": "hidden"}
    ],
    "max_points": 10
}
write_file(p / "rubric.json", json.dumps(rubric, indent=2, ensure_ascii=False))

# 8. cond_transformar_nombre
p = BASE / "Estructuras Condicionales/cond_transformar_nombre"
rubric = {
    "tests": [
        {"name": "test_existe_funcion", "points": 1, "visibility": "public"},
        {"name": "test_nombre_corto_mayuscula", "points": 3, "visibility": "public"},
        {"name": "test_nombre_largo_minuscula", "points": 3, "visibility": "public"},
        {"name": "test_nombre_limite", "points": 2, "visibility": "hidden"},
        {"name": "test_nombre_muy_largo", "points": 1, "visibility": "hidden"}
    ],
    "max_points": 10
}
write_file(p / "rubric.json", json.dumps(rubric, indent=2, ensure_ascii=False))

# 9. cond_validar_password
p = BASE / "Estructuras Condicionales/cond_validar_password"
rubric = {
    "tests": [
        {"name": "test_existe_funcion", "points": 1, "visibility": "public"},
        {"name": "test_password_valida_8", "points": 2, "visibility": "public"},
        {"name": "test_password_valida_14", "points": 2, "visibility": "public"},
        {"name": "test_password_muy_corta", "points": 2, "visibility": "public"},
        {"name": "test_password_muy_larga", "points": 2, "visibility": "hidden"},
        {"name": "test_password_intermedia", "points": 1, "visibility": "hidden"}
    ],
    "max_points": 10
}
write_file(p / "rubric.json", json.dumps(rubric, indent=2, ensure_ascii=False))

print("\n" + "="*70)
print("✅ RÚBRICAS CORREGIDAS")
print("="*70)
print("\n📊 Total: 19 rubric.json actualizados")
print("  • Todos balanceados a 10 puntos")
print("  • Tests públicos y ocultos distribuidos")
print("  • Nombres de tests corregidos")
print("\n🎯 Ahora todos los problemas darán 10/10 cuando estén correctos!")
