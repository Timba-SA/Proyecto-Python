"""
Script para validar todos los problemas de Programación I
Analiza:
- rubric.json: suma de puntos = 10, todos los tests tienen puntos > 0
- tests_public.py y tests_hidden.py: no duplicados, nombres coinciden con rubric
- solution_reference.py: existe y es válido
- starter.py: existe
- metadata.json: tiene hints de 4 niveles
- prompt.md: existe
"""

import json
from pathlib import Path
from collections import Counter

def validate_rubric(rubric_path):
    """Valida que rubric.json sea correcto"""
    errors = []
    
    with open(rubric_path, 'r', encoding='utf-8') as f:
        rubric = json.load(f)
    
    # Verificar que todos los tests tengan puntos > 0
    zero_point_tests = [t['name'] for t in rubric['tests'] if t['points'] == 0]
    if zero_point_tests:
        errors.append(f"❌ Tests con 0 puntos: {zero_point_tests}")
    
    # Verificar que la suma sea 10
    total = sum(t['points'] for t in rubric['tests'])
    if total != 10:
        errors.append(f"❌ Total de puntos: {total} (debe ser 10)")
    
    # Verificar max_points
    if rubric.get('max_points') != 10:
        errors.append(f"❌ max_points: {rubric.get('max_points')} (debe ser 10)")
    
    return errors, rubric

def extract_test_names(test_file):
    """Extrae nombres de tests de un archivo"""
    test_names = []
    if not test_file.exists():
        return test_names
    
    with open(test_file, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line.startswith('def test_'):
                test_name = line.split('(')[0].replace('def ', '')
                test_names.append(test_name)
    
    return test_names

def validate_tests(problem_dir, rubric):
    """Valida tests_public.py y tests_hidden.py"""
    errors = []
    
    public_file = problem_dir / 'tests_public.py'
    hidden_file = problem_dir / 'tests_hidden.py'
    
    public_tests = extract_test_names(public_file)
    hidden_tests = extract_test_names(hidden_file)
    
    # Verificar duplicados entre public y hidden
    all_tests = public_tests + hidden_tests
    duplicates = [name for name, count in Counter(all_tests).items() if count > 1]
    if duplicates:
        errors.append(f"❌ Tests duplicados: {duplicates}")
    
    # Verificar que todos los tests del rubric existan
    rubric_tests = {t['name'] for t in rubric['tests']}
    actual_tests = set(all_tests)
    
    missing_in_files = rubric_tests - actual_tests
    if missing_in_files:
        errors.append(f"❌ Tests en rubric pero no en archivos: {missing_in_files}")
    
    extra_in_files = actual_tests - rubric_tests
    if extra_in_files:
        errors.append(f"⚠️  Tests en archivos pero no en rubric: {extra_in_files}")
    
    return errors

def validate_required_files(problem_dir):
    """Valida que existan todos los archivos necesarios"""
    errors = []
    
    required_files = [
        'metadata.json',
        'prompt.md',
        'rubric.json',
        'solution_reference.py',
        'starter.py',
        'tests_public.py',
        'tests_hidden.py'
    ]
    
    for filename in required_files:
        if not (problem_dir / filename).exists():
            errors.append(f"❌ Archivo faltante: {filename}")
    
    return errors

def validate_metadata(metadata_path):
    """Valida que metadata.json tenga hints correctos"""
    errors = []
    
    if not metadata_path.exists():
        return errors
    
    with open(metadata_path, 'r', encoding='utf-8') as f:
        metadata = json.load(f)
    
    # Verificar que tenga hints
    if 'hints' not in metadata:
        errors.append(f"❌ No tiene hints")
        return errors
    
    hints = metadata['hints']
    if len(hints) < 4:
        errors.append(f"❌ Solo tiene {len(hints)} hints (debe tener 4)")
    
    # Verificar que los hints no estén vacíos
    for i, hint in enumerate(hints, 1):
        if not hint.strip():
            errors.append(f"❌ Hint {i} está vacío")
    
    return errors

def validate_problem(problem_dir):
    """Valida un problema completo"""
    print(f"\n{'='*80}")
    print(f"📁 {problem_dir.name}")
    print('='*80)
    
    all_errors = []
    
    # 1. Verificar archivos requeridos
    file_errors = validate_required_files(problem_dir)
    if file_errors:
        all_errors.extend(file_errors)
        for error in file_errors:
            print(error)
        return all_errors  # Si faltan archivos, no continuar
    
    # 2. Validar rubric.json
    rubric_path = problem_dir / 'rubric.json'
    rubric_errors, rubric = validate_rubric(rubric_path)
    if rubric_errors:
        all_errors.extend(rubric_errors)
        for error in rubric_errors:
            print(error)
    else:
        print(f"✅ rubric.json: {len(rubric['tests'])} tests, {sum(t['points'] for t in rubric['tests'])} puntos")
    
    # 3. Validar tests
    test_errors = validate_tests(problem_dir, rubric)
    if test_errors:
        all_errors.extend(test_errors)
        for error in test_errors:
            print(error)
    else:
        public_count = len(extract_test_names(problem_dir / 'tests_public.py'))
        hidden_count = len(extract_test_names(problem_dir / 'tests_hidden.py'))
        print(f"✅ Tests: {public_count} públicos, {hidden_count} ocultos, sin duplicados")
    
    # 4. Validar metadata.json
    metadata_errors = validate_metadata(problem_dir / 'metadata.json')
    if metadata_errors:
        all_errors.extend(metadata_errors)
        for error in metadata_errors:
            print(error)
    else:
        with open(problem_dir / 'metadata.json', 'r', encoding='utf-8') as f:
            metadata = json.load(f)
        print(f"✅ metadata.json: {len(metadata.get('hints', []))} hints")
    
    # 5. Verificar archivos Python
    if (problem_dir / 'solution_reference.py').exists():
        print(f"✅ solution_reference.py existe")
    if (problem_dir / 'starter.py').exists():
        print(f"✅ starter.py existe")
    if (problem_dir / 'prompt.md').exists():
        print(f"✅ prompt.md existe")
    
    if not all_errors:
        print(f"\n✅✅✅ PROBLEMA VÁLIDO ✅✅✅")
    else:
        print(f"\n❌❌❌ PROBLEMA CON ERRORES: {len(all_errors)} ❌❌❌")
    
    return all_errors

def main():
    base_path = Path(__file__).parent.parent / 'backend' / 'problems' / 'Programacion I'
    
    # Problemas Secuenciales
    secuenciales_dir = base_path / 'Estructuras Secuenciales'
    secuenciales = [
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
    ]
    
    # Problemas Condicionales
    condicionales_dir = base_path / 'Estructuras Condicionales'
    condicionales = [
        'cond_numero_par',
        'cond_mayor_edad',
        'cond_aprobado',
        'cond_mayor_de_dos',
        'cond_categorias_edad',
        'cond_validar_password',
        'cond_termina_vocal',
        'cond_transformar_nombre',
        'cond_terremoto'
    ]
    
    print("="*80)
    print("🔍 VALIDACIÓN COMPLETA DE PROBLEMAS PROGRAMACIÓN I")
    print("="*80)
    
    total_errors = {}
    
    print("\n\n" + "🔹"*40)
    print("ESTRUCTURAS SECUENCIALES (10 problemas)")
    print("🔹"*40)
    
    for problem in secuenciales:
        problem_dir = secuenciales_dir / problem
        if problem_dir.exists():
            errors = validate_problem(problem_dir)
            if errors:
                total_errors[problem] = errors
        else:
            print(f"\n❌ {problem}: DIRECTORIO NO EXISTE")
            total_errors[problem] = ["Directorio no existe"]
    
    print("\n\n" + "🔸"*40)
    print("ESTRUCTURAS CONDICIONALES (9 problemas)")
    print("🔸"*40)
    
    for problem in condicionales:
        problem_dir = condicionales_dir / problem
        if problem_dir.exists():
            errors = validate_problem(problem_dir)
            if errors:
                total_errors[problem] = errors
        else:
            print(f"\n❌ {problem}: DIRECTORIO NO EXISTE")
            total_errors[problem] = ["Directorio no existe"]
    
    # Resumen final
    print("\n\n" + "="*80)
    print("📊 RESUMEN FINAL")
    print("="*80)
    
    if not total_errors:
        print("\n✅✅✅ TODOS LOS PROBLEMAS ESTÁN CORRECTOS ✅✅✅")
    else:
        print(f"\n❌ PROBLEMAS CON ERRORES: {len(total_errors)}/{len(secuenciales) + len(condicionales)}\n")
        for problem, errors in total_errors.items():
            print(f"\n❌ {problem}:")
            for error in errors:
                print(f"   {error}")
    
    return len(total_errors) == 0

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)
