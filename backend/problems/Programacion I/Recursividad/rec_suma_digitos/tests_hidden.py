import importlib.util
import os
from io import StringIO
import sys

spec = importlib.util.spec_from_file_location('student_code', os.path.join(os.getcwd(), 'student_code.py'))
student = importlib.util.module_from_spec(spec)
spec.loader.exec_module(student)

def test_suma_digitos_9999():
    """Verifica suma de dígitos de 9999"""
    resultado = student.suma_digitos(9999)
    assert resultado == 36, f"""❌ suma_digitos(9999) debería ser 36, se obtuvo {resultado}"""

def test_suma_digitos_100():
    """Verifica suma de dígitos de 100"""
    resultado = student.suma_digitos(100)
    assert resultado == 1, f"""❌ suma_digitos(100) debería ser 1, se obtuvo {resultado}"""

def test_salida_completa_9():
    """Verifica salida completa con n=9"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("9")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "La suma de los digitos de 9 es 9"

def test_salida_completa_305():
    """Verifica salida completa con n=305"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("305")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "La suma de los digitos de 305 es 8"
