import importlib.util
import os
from io import StringIO
import sys
import inspect

spec = importlib.util.spec_from_file_location('student_code', os.path.join(os.getcwd(), 'student_code.py'))
student = importlib.util.module_from_spec(spec)
spec.loader.exec_module(student)

def test_existe_funcion():
    """Verifica que existe la función main"""
    assert hasattr(student, 'main'), 'Debe existir la función main'

def test_existe_funcion_factorial():
    """Verifica que existe la función factorial"""
    assert hasattr(student, 'factorial'), 'Debe existir la función factorial'

def test_factorial_es_recursiva():
    """Verifica que la función factorial es recursiva"""
    source = inspect.getsource(student.factorial)
    assert 'factorial(' in source and 'def factorial' in source, """❌ La función factorial debe ser recursiva
    💡 Pista: Una función recursiva se llama a sí misma. Debe contener factorial(n-1)"""

def test_factorial_1():
    """Verifica factorial de 1"""
    resultado = student.factorial(1)
    assert resultado == 1, f"""❌ factorial(1) debería ser 1, se obtuvo {resultado}
    💡 Pista: El caso base es factorial(1) = 1"""

def test_factorial_5():
    """Verifica factorial de 5"""
    resultado = student.factorial(5)
    assert resultado == 120, f"""❌ factorial(5) debería ser 120, se obtuvo {resultado}
    💡 Pista: 5! = 5 × 4 × 3 × 2 × 1 = 120"""

def test_salida_completa_n3():
    """Verifica salida completa con n=3"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("3")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    lineas = output.strip().split('\n')
    assert len(lineas) == 3, f"""❌ Se esperaban 3 líneas, se obtuvieron {len(lineas)}
    💡 Pista: Debe mostrar el factorial de todos los números desde 1 hasta n"""
    
    assert lineas[0] == "El factorial de 1 es 1"
    assert lineas[1] == "El factorial de 2 es 2"
    assert lineas[2] == "El factorial de 3 es 6"

def test_salida_completa_n5():
    """Verifica salida completa con n=5"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("5")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    lineas = output.strip().split('\n')
    assert len(lineas) == 5, f"""❌ Se esperaban 5 líneas, se obtuvieron {len(lineas)}"""
    
    assert "El factorial de 1 es 1" in lineas[0]
    assert "El factorial de 5 es 120" in lineas[4]
