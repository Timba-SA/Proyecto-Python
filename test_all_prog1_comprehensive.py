"""
Script EXHAUSTIVO para testear TODOS los 67 ejercicios de Programación I

Este script:
1. Verifica que todos los archivos requeridos existan
2. Lee y valida la estructura de metadata.json y rubric.json
3. Ejecuta los tests contra solution_reference.py
4. Genera un reporte detallado por unidad y general
"""

import subprocess
import sys
from pathlib import Path
import json
import shutil

# Estructura de ejercicios por unidad
UNITS = {
    "Estructuras Secuenciales": [
        'sec_hola_mundo',
        'sec_saludo_personalizado',
        'sec_presentacion_completa',
        'sec_operaciones_aritmeticas',
        'sec_area_perimetro_circulo',
        'sec_celsius_a_fahrenheit',
        'sec_segundos_a_horas',
        'sec_promedio_tres_numeros',
        'sec_calculo_imc',
        'sec_tabla_multiplicar'
    ],
    "Estructuras Condicionales": [
        'cond_numero_par',
        'cond_mayor_edad',
        'cond_aprobado',
        'cond_mayor_de_dos',
        'cond_categorias_edad',
        'cond_validar_password',
        'cond_termina_vocal',
        'cond_transformar_nombre',
        'cond_terremoto'
    ],
    "Estructuras Repetitivas": [
        'er_suma_hasta_n',
        'er_suma_hasta_cero',
        'er_suma_entre_valores',
        'er_promedio_numeros',
        'er_pares_descendente',
        'er_numeros_0_a_100',
        'er_contar_digitos',
        'er_invertir_digitos',
        'er_analisis_numeros',
        'er_juego_adivinanza'
    ],
    "Listas": [
        'lista_suma_elementos',
        'lista_promedio',
        'lista_mayor_elemento',
        'lista_menor_elemento',
        'lista_invertir',
        'lista_contar_pares',
        'lista_filtrar_positivos',
        'lista_concatenar',
        'lista_buscar_elemento',
        'lista_eliminar_duplicados'
    ],
    "Funciones": [
        'func_hola_mundo',
        'func_saludar_usuario',
        'func_informacion_personal',
        'func_operaciones_basicas',
        'func_calcular_promedio',
        'func_celsius_a_fahrenheit',
        'func_area_perimetro_circulo',
        'func_calcular_imc',
        'func_segundos_a_horas',
        'func_tabla_multiplicar'
    ],
    "Estructuras de datos complejas": [
        'edc_lista_frutas',
        'edc_agregar_frutas',
        'edc_palabras_unicas',
        'edc_sets_estudiantes',
        'edc_promedio_alumnos',
        'edc_actualizar_precios',
        'edc_invertir_diccionario',
        'edc_agenda_telefonica',
        'edc_agenda_tuplas',
        'edc_gestion_stock'
    ],
    "Recursividad": [
        'rec_factorial',
        'rec_fibonacci',
        'rec_suma_digitos',
        'rec_potencia',
        'rec_palindromo',
        'rec_contar_digito',
        'rec_decimal_binario',
        'rec_bloques_piramide'
    ]
}

REQUIRED_FILES = ['prompt.md', 'starter.py', 'tests_public.py', 'tests_hidden.py', 'metadata.json', 'rubric.json']

class TestReport:
    def __init__(self):
        self.total_exercises = 0
        self.exercises_ok = 0
        self.exercises_with_issues = 0
        self.issues = []
        self.unit_stats = {}
        
def verify_files(problem_dir, problem_name):
    """Verifica que todos los archivos requeridos existan"""
    missing = []
    for file in REQUIRED_FILES:
        if not (problem_dir / file).exists():
            missing.append(file)
    return missing

def validate_metadata(problem_dir, problem_name, unit_name):
    """Valida la estructura del metadata.json"""
    issues = []
    metadata_file = problem_dir / 'metadata.json'
    
    try:
        with open(metadata_file, 'r', encoding='utf-8') as f:
            metadata = json.load(f)
        
        # Verificar campos requeridos
        required_fields = ['title', 'subject_id', 'unit_id', 'difficulty', 'tags']
        for field in required_fields:
            if field not in metadata:
                issues.append(f"metadata.json: falta campo '{field}'")
        
        # Verificar valores correctos
        if metadata.get('subject_id') != 'programacion-1':
            issues.append(f"metadata.json: subject_id debe ser 'programacion-1', es '{metadata.get('subject_id')}'")
        
        # Mapeo de nombres de unidad a IDs
        unit_id_map = {
            "Estructuras Secuenciales": "estructuras-secuenciales",
            "Estructuras Condicionales": "estructuras-condicionales",
            "Estructuras Repetitivas": "estructuras-repetitivas",
            "Listas": "listas",
            "Funciones": "funciones",
            "Estructuras de datos complejas": "estructuras-datos-complejas",
            "Recursividad": "recursividad"
        }
        
        expected_unit_id = unit_id_map.get(unit_name)
        actual_unit_id = metadata.get('unit_id')
        if expected_unit_id and actual_unit_id != expected_unit_id:
            issues.append(f"metadata.json: unit_id debe ser '{expected_unit_id}', es '{actual_unit_id}'")
            
    except json.JSONDecodeError as e:
        issues.append(f"metadata.json: Error de JSON: {e}")
    except Exception as e:
        issues.append(f"metadata.json: Error leyendo archivo: {e}")
    
    return issues

def validate_rubric(problem_dir, problem_name):
    """Valida la estructura del rubric.json"""
    issues = []
    rubric_file = problem_dir / 'rubric.json'
    
    try:
        with open(rubric_file, 'r', encoding='utf-8') as f:
            rubric = json.load(f)
        
        # Verificar estructura
        if 'tests' not in rubric:
            issues.append("rubric.json: falta campo 'tests'")
            return issues
        
        if 'max_points' not in rubric:
            issues.append("rubric.json: falta campo 'max_points'")
        
        # Verificar que la suma de puntos coincida
        total_points = sum(test.get('points', 0) for test in rubric['tests'])
        max_points = rubric.get('max_points', 0)
        
        if total_points != max_points:
            issues.append(f"rubric.json: suma de puntos ({total_points}) != max_points ({max_points})")
        
        # Verificar que cada test tenga nombre, puntos y visibility
        for i, test in enumerate(rubric['tests']):
            if 'name' not in test:
                issues.append(f"rubric.json: test {i} no tiene 'name'")
            if 'points' not in test:
                issues.append(f"rubric.json: test {i} no tiene 'points'")
            if 'visibility' not in test:
                issues.append(f"rubric.json: test {i} no tiene 'visibility'")
                
    except json.JSONDecodeError as e:
        issues.append(f"rubric.json: Error de JSON: {e}")
    except Exception as e:
        issues.append(f"rubric.json: Error leyendo archivo: {e}")
    
    return issues

def run_tests(problem_dir, problem_name):
    """Ejecuta pytest en el ejercicio"""
    solution_file = problem_dir / 'solution_reference.py'
    student_file = problem_dir / 'student_code.py'
    
    if not solution_file.exists():
        return None, "No existe solution_reference.py"
    
    # Copiar solution_reference.py a student_code.py
    try:
        shutil.copy2(solution_file, student_file)
    except Exception as e:
        return None, f"Error copiando archivo: {e}"
    
    try:
        # Ejecutar pytest
        result = subprocess.run(
            [sys.executable, '-m', 'pytest', 'tests_public.py', 'tests_hidden.py', '-v', '--tb=short', '--override-ini=addopts='],
            cwd=problem_dir,
            capture_output=True,
            text=True,
            timeout=10
        )
        
        output = result.stdout + result.stderr
        
        # Parsear resultados
        import re
        passed_match = re.search(r'(\d+) passed', output)
        failed_match = re.search(r'(\d+) failed', output)
        error_match = re.search(r'(\d+) error', output)
        
        passed = int(passed_match.group(1)) if passed_match else 0
        failed = int(failed_match.group(1)) if failed_match else 0
        errors = int(error_match.group(1)) if error_match else 0
        
        return {
            'passed': passed,
            'failed': failed,
            'errors': errors,
            'output': output
        }, None
        
    except subprocess.TimeoutExpired:
        return None, "TIMEOUT (>10s)"
    except Exception as e:
        return None, f"Error ejecutando tests: {e}"
    finally:
        # Limpiar student_code.py
        if student_file.exists():
            try:
                student_file.unlink()
            except:
                pass

def main():
    base_path = Path(__file__).parent / 'backend' / 'problems' / 'Programacion I'
    
    if not base_path.exists():
        print(f"ERROR: No existe el directorio {base_path}")
        return
    
    report = TestReport()
    
    print("="*100)
    print("ANALISIS EXHAUSTIVO DE PROGRAMACION I - 67 EJERCICIOS")
    print("="*100)
    print()
    
    # Procesar cada unidad
    for unit_name, exercises in UNITS.items():
        unit_dir = base_path / unit_name
        
        print("-" * 100)
        print(f"UNIDAD: {unit_name.upper()}")
        print("-" * 100)
        
        unit_issues = []
        unit_ok = 0
        
        for problem in exercises:
            problem_dir = unit_dir / problem
            report.total_exercises += 1
            
            print(f"  [{problem}]", end='', flush=True)
            
            problem_issues = []
            
            # 1. Verificar archivos
            missing_files = verify_files(problem_dir, problem)
            if missing_files:
                problem_issues.append(f"Archivos faltantes: {', '.join(missing_files)}")
            
            # 2. Validar metadata.json
            metadata_issues = validate_metadata(problem_dir, problem, unit_name)
            problem_issues.extend(metadata_issues)
            
            # 3. Validar rubric.json
            rubric_issues = validate_rubric(problem_dir, problem)
            problem_issues.extend(rubric_issues)
            
            # 4. Ejecutar tests
            test_result, test_error = run_tests(problem_dir, problem)
            
            if test_error:
                problem_issues.append(f"Tests: {test_error}")
            elif test_result:
                if test_result['failed'] > 0 or test_result['errors'] > 0:
                    problem_issues.append(f"Tests: {test_result['failed']} fallidos, {test_result['errors']} errores")
            
            # Resumen del ejercicio
            if problem_issues:
                print(f" [ERROR]")
                for issue in problem_issues:
                    print(f"    - {issue}")
                report.exercises_with_issues += 1
                report.issues.append({
                    'unit': unit_name,
                    'exercise': problem,
                    'issues': problem_issues
                })
                unit_issues.append(problem)
            else:
                tests_info = f"{test_result['passed']} tests OK" if test_result else "?"
                print(f" [OK] {tests_info}")
                report.exercises_ok += 1
                unit_ok += 1
        
        # Estadísticas de la unidad
        total_unit = len(exercises)
        print(f"\n  Resumen de unidad: {unit_ok}/{total_unit} OK, {len(unit_issues)}/{total_unit} con problemas")
        print()
        
        report.unit_stats[unit_name] = {
            'total': total_unit,
            'ok': unit_ok,
            'issues': len(unit_issues)
        }
    
    # RESUMEN FINAL
    print("\n" + "="*100)
    print("RESUMEN EJECUTIVO FINAL")
    print("="*100)
    print(f"\nTotal de ejercicios revisados: {report.total_exercises}")
    print(f"Ejercicios sin problemas: {report.exercises_ok} ({report.exercises_ok*100//report.total_exercises}%)")
    print(f"Ejercicios con problemas: {report.exercises_with_issues} ({report.exercises_with_issues*100//report.total_exercises}%)")
    
    print("\n" + "-"*100)
    print("RESUMEN POR UNIDAD:")
    print("-"*100)
    for unit_name, stats in report.unit_stats.items():
        percentage = stats['ok'] * 100 // stats['total']
        status = "[OK]" if stats['issues'] == 0 else "[!]"
        print(f"{status} {unit_name:<40} {stats['ok']:>2}/{stats['total']:>2} OK ({percentage:>3}%)")
    
    if report.issues:
        print("\n" + "="*100)
        print("DETALLE DE PROBLEMAS ENCONTRADOS")
        print("="*100)
        
        # Agrupar por tipo de problema
        issues_by_type = {}
        for item in report.issues:
            for issue in item['issues']:
                issue_type = issue.split(':')[0] if ':' in issue else 'Otro'
                if issue_type not in issues_by_type:
                    issues_by_type[issue_type] = []
                issues_by_type[issue_type].append(f"{item['exercise']} ({item['unit']}): {issue}")
        
        for issue_type, problems in sorted(issues_by_type.items()):
            print(f"\n{issue_type}:")
            for problem in problems:
                print(f"  - {problem}")
    
    print("\n" + "="*100)
    if report.exercises_with_issues == 0:
        print("EXCELENTE! TODOS LOS EJERCICIOS ESTAN CORRECTOS")
    else:
        print(f"Se encontraron problemas en {report.exercises_with_issues} ejercicios")
    print("="*100)

if __name__ == "__main__":
    main()
