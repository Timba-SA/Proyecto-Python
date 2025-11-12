import importlib.util
import os
from io import StringIO
import sys

spec = importlib.util.spec_from_file_location('student_code', os.path.join(os.getcwd(), 'student_code.py'))
student = importlib.util.module_from_spec(spec)
spec.loader.exec_module(student)

def test_factorial_0():
    """Verifica factorial de 0"""
    resultado = student.factorial(0)
    assert resultado == 1, f"""❌ factorial(0) debería ser 1, se obtuvo {resultado}
    💡 Pista: Por definición matemática, 0! = 1"""

def test_factorial_10():
    """Verifica factorial de 10"""
    resultado = student.factorial(10)
    assert resultado == 3628800, f"""❌ factorial(10) debería ser 3628800, se obtuvo {resultado}"""

def test_salida_completa_n1():
    """Verifica salida completa con n=1"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("1")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    lineas = output.strip().split('\n')
    assert len(lineas) == 1
    assert lineas[0] == "El factorial de 1 es 1"

def test_salida_completa_n7():
    """Verifica salida completa con n=7"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("7")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    lineas = output.strip().split('\n')
    assert len(lineas) == 7
    assert "El factorial de 7 es 5040" in lineas[6]
