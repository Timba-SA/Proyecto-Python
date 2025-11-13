"""
Tests para: Rec Fibonacci
Tema: Recursividad

Este archivo contiene tests públicos que el estudiante puede ver.
Los tests verifican que la solución cumpla con todos los requisitos.
"""

import importlib.util
import os
from io import StringIO
import sys

spec = importlib.util.spec_from_file_location('student_code', os.path.join(os.getcwd(), 'student_code.py'))
student = importlib.util.module_from_spec(spec)
spec.loader.exec_module(student)

def test_fibonacci_7():
    """Verifica fibonacci de 7"""
    resultado = student.fibonacci(7)
    assert resultado == 13, f"""❌ fibonacci(7) debería ser 13, se obtuvo {resultado}"""

def test_fibonacci_10():
    """Verifica fibonacci de 10"""
    resultado = student.fibonacci(10)
    assert resultado == 55, f"""❌ fibonacci(10) debería ser 55, se obtuvo {resultado}"""

def test_salida_completa_n0():
    """Verifica salida completa con n=0"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("0")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "0", f"""❌ Se esperaba '0', se obtuvo '{output}'"""

def test_salida_completa_n7():
    """Verifica salida completa con n=7"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("7")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "0, 1, 1, 2, 3, 5, 8, 13", f"""❌ Se esperaba '0, 1, 1, 2, 3, 5, 8, 13', se obtuvo '{output}'"""

def test_salida_completa_n10():
    """Verifica salida completa con n=10"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("10")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55"
