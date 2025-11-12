"""
Script para testear TODOS los problemas de Programación I con pytest
Este script ejecuta todos los tests y verifica que las solution_reference.py funcionen
"""

import subprocess
from pathlib import Path
import json

def test_problem(problem_dir):
    """Ejecuta pytest en un problema específico"""
    problem_name = problem_dir.name
    
    # Copiar solution_reference.py a student_code.py para testear
    solution_file = problem_dir / 'solution_reference.py'
    student_file = problem_dir / 'student_code.py'
    
    if not solution_file.exists():
        return None, "No existe solution_reference.py"
    
    # Copiar solución de referencia
    with open(solution_file, 'r', encoding='utf-8') as f:
        solution_code = f.read()
    
    with open(student_file, 'w', encoding='utf-8') as f:
        f.write(solution_code)
    
    try:
        # Ejecutar pytest
        result = subprocess.run(
            ['pytest', 'tests_public.py', 'tests_hidden.py', '-v', '--override-ini=addopts=', '--tb=short'],
            cwd=problem_dir,
            capture_output=True,
            text=True,
            timeout=10
        )
        
        # Parsear resultados
        output = result.stdout + result.stderr
        
        # Contar tests pasados/fallados
        if "passed" in output:
            # Extraer número de tests
            import re
            match = re.search(r'(\d+) passed', output)
            if match:
                passed = int(match.group(1))
                
                # Verificar si hay tests fallados
                failed_match = re.search(r'(\d+) failed', output)
                failed = int(failed_match.group(1)) if failed_match else 0
                
                return passed, failed, output
        
        return 0, 0, output
        
    except subprocess.TimeoutExpired:
        return None, "TIMEOUT (>10s)"
    except Exception as e:
        return None, str(e)
    finally:
        # Limpiar student_code.py
        if student_file.exists():
            student_file.unlink()

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
    print("🧪 TESTING COMPLETO DE PROGRAMACIÓN I CON PYTEST")
    print("="*80)
    print("Ejecutando solution_reference.py contra todos los tests...")
    print()
    
    results = {}
    total_problems = 0
    total_passed = 0
    total_failed = 0
    
    print("🔹"*40)
    print("ESTRUCTURAS SECUENCIALES")
    print("🔹"*40 + "\n")
    
    for problem in secuenciales:
        problem_dir = secuenciales_dir / problem
        if not problem_dir.exists():
            print(f"❌ {problem}: DIRECTORIO NO EXISTE\n")
            continue
        
        total_problems += 1
        print(f"📁 {problem}... ", end='', flush=True)
        
        result = test_problem(problem_dir)
        if isinstance(result, tuple) and len(result) == 3:
            passed, failed, output = result
            if failed == 0 and passed > 0:
                print(f"✅ {passed} tests pasados")
                total_passed += 1
                results[problem] = "✅ PASS"
            else:
                print(f"❌ {passed} passed, {failed} failed")
                total_failed += 1
                results[problem] = f"❌ FAIL ({failed} failed)"
                # Mostrar detalles del fallo
                if "FAILED" in output:
                    print("   Detalles:")
                    for line in output.split('\n'):
                        if "FAILED" in line or "AssertionError" in line:
                            print(f"   {line}")
        else:
            passed, error = result
            print(f"❌ ERROR: {error}")
            total_failed += 1
            results[problem] = f"❌ ERROR: {error}"
    
    print("\n" + "🔸"*40)
    print("ESTRUCTURAS CONDICIONALES")
    print("🔸"*40 + "\n")
    
    for problem in condicionales:
        problem_dir = condicionales_dir / problem
        if not problem_dir.exists():
            print(f"❌ {problem}: DIRECTORIO NO EXISTE\n")
            continue
        
        total_problems += 1
        print(f"📁 {problem}... ", end='', flush=True)
        
        result = test_problem(problem_dir)
        if isinstance(result, tuple) and len(result) == 3:
            passed, failed, output = result
            if failed == 0 and passed > 0:
                print(f"✅ {passed} tests pasados")
                total_passed += 1
                results[problem] = "✅ PASS"
            else:
                print(f"❌ {passed} passed, {failed} failed")
                total_failed += 1
                results[problem] = f"❌ FAIL ({failed} failed)"
                # Mostrar detalles del fallo
                if "FAILED" in output:
                    print("   Detalles:")
                    for line in output.split('\n'):
                        if "FAILED" in line or "AssertionError" in line:
                            print(f"   {line}")
        else:
            passed, error = result
            print(f"❌ ERROR: {error}")
            total_failed += 1
            results[problem] = f"❌ ERROR: {error}"
    
    # Resumen
    print("\n" + "="*80)
    print("📊 RESUMEN FINAL")
    print("="*80)
    print(f"Total de problemas: {total_problems}")
    print(f"✅ Pasaron todos los tests: {total_passed}/{total_problems}")
    print(f"❌ Fallaron o errores: {total_failed}/{total_problems}")
    print()
    
    if total_failed > 0:
        print("Problemas con errores:")
        for problem, result in results.items():
            if "❌" in result:
                print(f"  {problem}: {result}")
    else:
        print("✅✅✅ TODOS LOS PROBLEMAS PASARON CORRECTAMENTE ✅✅✅")
    
    return total_failed == 0

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)
