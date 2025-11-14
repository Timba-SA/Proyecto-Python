"""
Script para corregir problemas menores en Programación I
- Cambiar 'easy' -> 'facil', 'medium' -> 'medio', 'hard' -> 'dificil'
- Asegurar que haya tests públicos visibles
"""

import json
from pathlib import Path

UNITS = {
    "Estructuras Secuenciales": [
        'sec_hola_mundo', 'sec_saludo_personalizado', 'sec_presentacion_completa',
        'sec_operaciones_aritmeticas', 'sec_area_perimetro_circulo', 'sec_celsius_a_fahrenheit',
        'sec_segundos_a_horas', 'sec_promedio_tres_numeros', 'sec_calculo_imc', 'sec_tabla_multiplicar'
    ],
    "Estructuras Condicionales": [
        'cond_numero_par', 'cond_mayor_edad', 'cond_aprobado', 'cond_mayor_de_dos',
        'cond_categorias_edad', 'cond_validar_password', 'cond_termina_vocal',
        'cond_transformar_nombre', 'cond_terremoto'
    ],
    "Estructuras Repetitivas": [
        'er_suma_hasta_n', 'er_suma_hasta_cero', 'er_suma_entre_valores', 'er_promedio_numeros',
        'er_pares_descendente', 'er_numeros_0_a_100', 'er_contar_digitos', 'er_invertir_digitos',
        'er_analisis_numeros', 'er_juego_adivinanza'
    ],
    "Listas": [
        'lista_suma_elementos', 'lista_promedio', 'lista_mayor_elemento', 'lista_menor_elemento',
        'lista_invertir', 'lista_contar_pares', 'lista_filtrar_positivos', 'lista_concatenar',
        'lista_buscar_elemento', 'lista_eliminar_duplicados'
    ],
    "Funciones": [
        'func_hola_mundo', 'func_saludar_usuario', 'func_informacion_personal', 'func_operaciones_basicas',
        'func_calcular_promedio', 'func_celsius_a_fahrenheit', 'func_area_perimetro_circulo',
        'func_calcular_imc', 'func_segundos_a_horas', 'func_tabla_multiplicar'
    ],
    "Estructuras de datos complejas": [
        'edc_lista_frutas', 'edc_agregar_frutas', 'edc_palabras_unicas', 'edc_sets_estudiantes',
        'edc_promedio_alumnos', 'edc_actualizar_precios', 'edc_invertir_diccionario',
        'edc_agenda_telefonica', 'edc_agenda_tuplas', 'edc_gestion_stock'
    ],
    "Recursividad": [
        'rec_factorial', 'rec_fibonacci', 'rec_suma_digitos', 'rec_potencia',
        'rec_palindromo', 'rec_contar_digito', 'rec_decimal_binario', 'rec_bloques_piramide'
    ]
}

DIFFICULTY_MAP = {
    'easy': 'facil',
    'medium': 'medio',
    'hard': 'dificil'
}

def fix_metadata(problem_dir):
    """Corrige la dificultad en metadata.json"""
    metadata_file = problem_dir / 'metadata.json'
    try:
        with open(metadata_file, 'r', encoding='utf-8') as f:
            metadata = json.load(f)
        
        changed = False
        difficulty = metadata.get('difficulty', '')
        
        if difficulty in DIFFICULTY_MAP:
            metadata['difficulty'] = DIFFICULTY_MAP[difficulty]
            changed = True
        
        if changed:
            with open(metadata_file, 'w', encoding='utf-8') as f:
                json.dump(metadata, f, indent=2, ensure_ascii=False)
            return True
        
    except Exception as e:
        print(f"    Error corrigiendo metadata: {e}")
    
    return False

def fix_rubric(problem_dir):
    """Asegura que al menos 1 test sea público"""
    rubric_file = problem_dir / 'rubric.json'
    try:
        with open(rubric_file, 'r', encoding='utf-8') as f:
            rubric = json.load(f)
        
        if 'tests' not in rubric:
            return False
        
        # Contar tests públicos
        public_count = sum(1 for t in rubric['tests'] if t.get('visibility') == 'visible')
        
        if public_count == 0 and len(rubric['tests']) > 0:
            # Hacer el primer test público
            rubric['tests'][0]['visibility'] = 'visible'
            
            with open(rubric_file, 'w', encoding='utf-8') as f:
                json.dump(rubric, f, indent=2, ensure_ascii=False)
            return True
        
    except Exception as e:
        print(f"    Error corrigiendo rubric: {e}")
    
    return False

def main():
    base_path = Path(__file__).parent / 'backend' / 'problems' / 'Programacion I'
    
    total_metadata_fixed = 0
    total_rubric_fixed = 0
    
    print("="*100)
    print("CORRIGIENDO PROBLEMAS MENORES EN PROGRAMACION I")
    print("="*100)
    print()
    
    for unit_name, exercises in UNITS.items():
        unit_dir = base_path / unit_name
        
        print(f"Procesando: {unit_name}")
        
        for problem in exercises:
            problem_dir = unit_dir / problem
            
            metadata_fixed = fix_metadata(problem_dir)
            rubric_fixed = fix_rubric(problem_dir)
            
            if metadata_fixed:
                total_metadata_fixed += 1
                print(f"  - {problem}: metadata corregido")
            
            if rubric_fixed:
                total_rubric_fixed += 1
                print(f"  - {problem}: rubric corregido")
    
    print("\n" + "="*100)
    print("RESUMEN DE CORRECCIONES")
    print("="*100)
    print(f"Metadatos corregidos: {total_metadata_fixed}")
    print(f"Rúbricas corregidas: {total_rubric_fixed}")
    print("="*100)

if __name__ == "__main__":
    main()
