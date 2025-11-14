"""
Script para verificar la calidad completa de Programación I
Verifica: metadatos, rúbricas, enunciados, código starter, hints, etc.
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

UNIT_ID_MAP = {
    "Estructuras Secuenciales": "estructuras-secuenciales",
    "Estructuras Condicionales": "estructuras-condicionales",
    "Estructuras Repetitivas": "estructuras-repetitivas",
    "Listas": "listas",
    "Funciones": "funciones",
    "Estructuras de datos complejas": "estructuras-datos-complejas",
    "Recursividad": "recursividad"
}

class QualityReport:
    def __init__(self):
        self.issues = []
        self.warnings = []
        self.total_exercises = 0
        self.perfect_exercises = 0
        
def check_metadata(problem_dir, problem_name, unit_name):
    """Verifica calidad del metadata.json"""
    issues = []
    warnings = []
    
    metadata_file = problem_dir / 'metadata.json'
    try:
        with open(metadata_file, 'r', encoding='utf-8') as f:
            metadata = json.load(f)
        
        # Verificar campos
        if not metadata.get('title'):
            issues.append("metadata: título vacío")
        
        if metadata.get('subject_id') != 'programacion-1':
            issues.append(f"metadata: subject_id incorrecto: {metadata.get('subject_id')}")
        
        expected_unit_id = UNIT_ID_MAP.get(unit_name)
        if metadata.get('unit_id') != expected_unit_id:
            issues.append(f"metadata: unit_id debe ser '{expected_unit_id}', es '{metadata.get('unit_id')}'")
        
        if not metadata.get('difficulty') in ['facil', 'medio', 'dificil']:
            warnings.append(f"metadata: dificultad '{metadata.get('difficulty')}' no estándar")
        
        if not metadata.get('tags') or len(metadata.get('tags', [])) == 0:
            warnings.append("metadata: sin tags")
            
    except Exception as e:
        issues.append(f"metadata: error leyendo: {e}")
    
    return issues, warnings

def check_rubric(problem_dir, problem_name):
    """Verifica calidad del rubric.json"""
    issues = []
    warnings = []
    
    rubric_file = problem_dir / 'rubric.json'
    try:
        with open(rubric_file, 'r', encoding='utf-8') as f:
            rubric = json.load(f)
        
        if 'tests' not in rubric or not rubric['tests']:
            issues.append("rubric: sin tests")
            return issues, warnings
        
        total_points = sum(test.get('points', 0) for test in rubric['tests'])
        max_points = rubric.get('max_points', 0)
        
        if total_points != max_points:
            issues.append(f"rubric: suma de puntos ({total_points}) != max_points ({max_points})")
        
        if max_points != 10:
            warnings.append(f"rubric: max_points es {max_points}, debería ser 10")
        
        # Verificar que haya tests públicos y ocultos
        public_count = sum(1 for t in rubric['tests'] if t.get('visibility') == 'visible')
        hidden_count = sum(1 for t in rubric['tests'] if t.get('visibility') == 'hidden')
        
        if public_count == 0:
            warnings.append("rubric: sin tests públicos")
        if hidden_count == 0:
            warnings.append("rubric: sin tests ocultos")
            
    except Exception as e:
        issues.append(f"rubric: error leyendo: {e}")
    
    return issues, warnings

def check_prompt(problem_dir, problem_name):
    """Verifica calidad del prompt.md"""
    issues = []
    warnings = []
    
    prompt_file = problem_dir / 'prompt.md'
    try:
        with open(prompt_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if len(content) < 200:
            warnings.append("prompt: muy corto (< 200 caracteres)")
        
        # Verificar secciones importantes
        required_sections = ['Objetivo', 'Entrada', 'Salida']
        for section in required_sections:
            if section not in content:
                warnings.append(f"prompt: falta sección '{section}'")
        
        # Verificar que tenga ejemplos
        if 'Ejemplo' not in content and 'ejemplo' not in content:
            warnings.append("prompt: sin ejemplos")
        
        # Verificar que tenga pistas
        if 'Pista' not in content and 'pista' not in content:
            warnings.append("prompt: sin pistas")
            
    except Exception as e:
        issues.append(f"prompt: error leyendo: {e}")
    
    return issues, warnings

def check_starter(problem_dir, problem_name):
    """Verifica calidad del starter.py"""
    issues = []
    warnings = []
    
    starter_file = problem_dir / 'starter.py'
    try:
        with open(starter_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if len(content) < 50:
            warnings.append("starter: muy básico (< 50 caracteres)")
        
        # Verificar que tenga estructura básica
        if 'def main()' not in content and 'def ' not in content:
            warnings.append("starter: sin estructura de función")
        
        # Verificar que tenga comentarios guía
        if '#' not in content and '"""' not in content:
            warnings.append("starter: sin comentarios/docstrings guía")
            
    except Exception as e:
        issues.append(f"starter: error leyendo: {e}")
    
    return issues, warnings

def main():
    base_path = Path(__file__).parent / 'backend' / 'problems' / 'Programacion I'
    report = QualityReport()
    
    print("="*100)
    print("VERIFICACIÓN DE CALIDAD DE PROGRAMACIÓN I")
    print("="*100)
    print()
    
    for unit_name, exercises in UNITS.items():
        unit_dir = base_path / unit_name
        
        print(f"\n{'='*100}")
        print(f"UNIDAD: {unit_name}")
        print(f"{'='*100}")
        
        for problem in exercises:
            problem_dir = unit_dir / problem
            report.total_exercises += 1
            
            print(f"\n  [{problem}]")
            
            all_issues = []
            all_warnings = []
            
            # Verificar metadata
            issues, warnings = check_metadata(problem_dir, problem, unit_name)
            all_issues.extend(issues)
            all_warnings.extend(warnings)
            
            # Verificar rubric
            issues, warnings = check_rubric(problem_dir, problem)
            all_issues.extend(issues)
            all_warnings.extend(warnings)
            
            # Verificar prompt
            issues, warnings = check_prompt(problem_dir, problem)
            all_issues.extend(issues)
            all_warnings.extend(warnings)
            
            # Verificar starter
            issues, warnings = check_starter(problem_dir, problem)
            all_issues.extend(issues)
            all_warnings.extend(warnings)
            
            # Mostrar resultados
            if all_issues:
                print(f"    [ERROR] ERRORES CRITICOS:")
                for issue in all_issues:
                    print(f"       - {issue}")
                report.issues.append({'exercise': problem, 'issues': all_issues})
            
            if all_warnings:
                print(f"    [WARN] ADVERTENCIAS:")
                for warning in all_warnings:
                    print(f"       - {warning}")
                report.warnings.append({'exercise': problem, 'warnings': all_warnings})
            
            if not all_issues and not all_warnings:
                print(f"    [OK] PERFECTO")
                report.perfect_exercises += 1
    
    # Resumen final
    print("\n" + "="*100)
    print("RESUMEN FINAL DE CALIDAD")
    print("="*100)
    print(f"\nTotal de ejercicios: {report.total_exercises}")
    print(f"Ejercicios perfectos: {report.perfect_exercises} ({report.perfect_exercises*100//report.total_exercises}%)")
    print(f"Ejercicios con errores: {len(report.issues)}")
    print(f"Ejercicios con advertencias: {len(report.warnings)}")
    
    if len(report.issues) == 0 and len(report.warnings) == 0:
        print("\n" + "="*100)
        print("EXCELENTE! PROGRAMACION I ESTA 100% COMPLETO Y CON CALIDAD PERFECTA")
        print("="*100)
    else:
        print("\n" + "="*100)
        print("HAY ALGUNOS DETALLES A MEJORAR")
        print("="*100)

if __name__ == "__main__":
    main()
