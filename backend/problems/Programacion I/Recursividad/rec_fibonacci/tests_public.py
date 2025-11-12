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

def test_existe_funcion_fibonacci():
    """Verifica que existe la función fibonacci"""
    assert hasattr(student, 'fibonacci'), 'Debe existir la función fibonacci'

def test_fibonacci_es_recursiva():
    """Verifica que la función fibonacci es recursiva"""
    source = inspect.getsource(student.fibonacci)
    assert 'fibonacci(' in source and 'def fibonacci' in source, """❌ La función fibonacci debe ser recursiva
    💡 Pista: Una función recursiva se llama a sí misma. Debe contener fibonacci(n-1) y fibonacci(n-2)"""

def test_fibonacci_0():
    """Verifica fibonacci de 0"""
    resultado = student.fibonacci(0)
    assert resultado == 0, f"""❌ fibonacci(0) debería ser 0, se obtuvo {resultado}
    💡 Pista: El primer caso base es fibonacci(0) = 0"""

def test_fibonacci_1():
    """Verifica fibonacci de 1"""
    resultado = student.fibonacci(1)
    assert resultado == 1, f"""❌ fibonacci(1) debería ser 1, se obtuvo {resultado}
    💡 Pista: El segundo caso base es fibonacci(1) = 1"""

def test_fibonacci_5():
    """Verifica fibonacci de 5"""
    resultado = student.fibonacci(5)
    assert resultado == 5, f"""❌ fibonacci(5) debería ser 5, se obtuvo {resultado}
    💡 Pista: fibonacci(5) = fibonacci(4) + fibonacci(3) = 3 + 2 = 5"""

def test_salida_completa_n5():
    """Verifica salida completa con n=5"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("5")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "0, 1, 1, 2, 3, 5", f"""❌ Se esperaba '0, 1, 1, 2, 3, 5', se obtuvo '{output}'
    💡 Pista: Los valores deben estar separados por ', ' (coma y espacio)"""
