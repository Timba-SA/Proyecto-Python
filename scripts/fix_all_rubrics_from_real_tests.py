"""
Script para regenerar TODOS los rubric.json basándose en los tests REALES
que existen en tests_public.py y tests_hidden.py
"""

import json
from pathlib import Path
from collections import Counter

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

def calculate_points(num_tests):
    """Calcula distribución de puntos para que sumen 10"""
    if num_tests == 0:
        return []
    
    base_points = 10 // num_tests
    remainder = 10 % num_tests
    
    points = [base_points] * num_tests
    
    # Distribuir el resto entre los primeros tests
    for i in range(remainder):
        points[i] += 1
    
    # Asegurar que al menos un test tenga 2 puntos (generalmente el primero importante)
    # y que test_existe_funcion tenga 1 punto
    if num_tests >= 2:
        if points[1] == 1:
            points[1] = 2
            points[0] = points[0] - 1 if points[0] > 1 else points[0]
    
    return points

def regenerate_rubric(problem_dir):
    """Regenera rubric.json basándose en los tests reales"""
    public_file = problem_dir / 'tests_public.py'
    hidden_file = problem_dir / 'tests_hidden.py'
    rubric_file = problem_dir / 'rubric.json'
    
    # Extraer tests
    public_tests = extract_test_names(public_file)
    hidden_tests = extract_test_names(hidden_file)
    
    # Verificar duplicados
    all_tests = public_tests + hidden_tests
    duplicates = [name for name, count in Counter(all_tests).items() if count > 1]
    
    if duplicates:
        print(f"  ⚠️  DUPLICADOS ENCONTRADOS: {duplicates}")
        # Eliminar duplicados de hidden (mantener en public)
        for dup in duplicates:
            if dup in hidden_tests:
                hidden_tests.remove(dup)
                print(f"     Eliminado {dup} de tests_hidden.py")
    
    # Calcular puntos
    total_tests = len(public_tests) + len(hidden_tests)
    if total_tests == 0:
        print(f"  ❌ No hay tests!")
        return False
    
    points_dist = calculate_points(total_tests)
    
    # Crear rubric
    tests = []
    
    # Tests públicos
    for i, test_name in enumerate(public_tests):
        tests.append({
            "name": test_name,
            "points": points_dist[i],
            "visibility": "public"
        })
    
    # Tests ocultos
    for i, test_name in enumerate(hidden_tests):
        tests.append({
            "name": test_name,
            "points": points_dist[len(public_tests) + i],
            "visibility": "hidden"
        })
    
    # Verificar suma
    total_points = sum(t['points'] for t in tests)
    if total_points != 10:
        print(f"  ⚠️  Ajustando puntos: suma={total_points}")
        # Ajustar el primer test con 2+ puntos
        for t in tests:
            if t['points'] >= 2 and total_points > 10:
                diff = total_points - 10
                t['points'] -= diff
                break
            elif t['points'] >= 1 and total_points < 10:
                diff = 10 - total_points
                t['points'] += diff
                break
    
    # Crear estructura final
    rubric = {
        "tests": tests,
        "max_points": 10
    }
    
    # Guardar
    with open(rubric_file, 'w', encoding='utf-8') as f:
        json.dump(rubric, f, indent=2, ensure_ascii=False)
    
    print(f"  ✅ Generado: {len(public_tests)} public, {len(hidden_tests)} hidden = {total_tests} tests, {sum(t['points'] for t in tests)} pts")
    
    # Eliminar duplicados de archivos si los hay
    if duplicates:
        remove_duplicate_tests(hidden_file, duplicates)
    
    return True

def remove_duplicate_tests(test_file, duplicates):
    """Elimina tests duplicados de un archivo"""
    if not test_file.exists():
        return
    
    with open(test_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    new_lines = []
    skip_until_next_def = False
    current_test = None
    
    for i, line in enumerate(lines):
        if line.strip().startswith('def test_'):
            # Detectar nombre del test
            test_name = line.split('(')[0].replace('def ', '').strip()
            
            if test_name in duplicates:
                skip_until_next_def = True
                current_test = test_name
                print(f"     Eliminando {test_name} de {test_file.name}")
                continue
            else:
                skip_until_next_def = False
        
        if not skip_until_next_def:
            new_lines.append(line)
        elif line.strip().startswith('def ') and not line.strip().startswith('def test_'):
            # Encontramos otra función, dejar de saltear
            skip_until_next_def = False
            new_lines.append(line)
    
    # Guardar archivo modificado
    with open(test_file, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)

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
    print("🔧 REGENERACIÓN DE TODOS LOS RUBRICS")
    print("="*80)
    
    success_count = 0
    
    print("\n" + "🔹"*40)
    print("ESTRUCTURAS SECUENCIALES")
    print("🔹"*40)
    
    for problem in secuenciales:
        problem_dir = secuenciales_dir / problem
        print(f"\n📁 {problem}")
        if problem_dir.exists():
            if regenerate_rubric(problem_dir):
                success_count += 1
        else:
            print(f"  ❌ Directorio no existe")
    
    print("\n" + "🔸"*40)
    print("ESTRUCTURAS CONDICIONALES")
    print("🔸"*40)
    
    for problem in condicionales:
        problem_dir = condicionales_dir / problem
        print(f"\n📁 {problem}")
        if problem_dir.exists():
            if regenerate_rubric(problem_dir):
                success_count += 1
        else:
            print(f"  ❌ Directorio no existe")
    
    print("\n" + "="*80)
    print(f"✅ REGENERADOS: {success_count}/19 rubrics")
    print("="*80)

if __name__ == "__main__":
    main()
