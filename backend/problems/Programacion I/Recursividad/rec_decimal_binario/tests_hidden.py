import importlib.util
import os
from io import StringIO
import sys

spec = importlib.util.spec_from_file_location('student_code', os.path.join(os.getcwd(), 'student_code.py'))
student = importlib.util.module_from_spec(spec)
spec.loader.exec_module(student)

def test_decimal_a_binario_8():
    """Verifica conversión de 8"""
    resultado = student.decimal_a_binario(8)
    assert resultado == "1000", f"""❌ decimal_a_binario(8) debería ser '1000', se obtuvo '{resultado}'"""

def test_decimal_a_binario_255():
    """Verifica conversión de 255"""
    resultado = student.decimal_a_binario(255)
    assert resultado == "11111111", f"""❌ decimal_a_binario(255) debería ser '11111111', se obtuvo '{resultado}'"""

def test_salida_completa_0():
    """Verifica salida completa con n=0"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("0")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "La representación binaria de 0 es 0"

def test_salida_completa_5():
    """Verifica salida completa con n=5"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("5")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "La representación binaria de 5 es 101"

def test_salida_completa_255():
    """Verifica salida completa con n=255"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("255")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "La representación binaria de 255 es 11111111"
