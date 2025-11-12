import importlib.util
import os
from io import StringIO
import sys

spec = importlib.util.spec_from_file_location('student_code', os.path.join(os.getcwd(), 'student_code.py'))
student = importlib.util.module_from_spec(spec)
spec.loader.exec_module(student)

def test_contar_bloques_5():
    """Verifica contar_bloques(5)"""
    resultado = student.contar_bloques(5)
    assert resultado == 15, f"""❌ contar_bloques(5) debería ser 15, se obtuvo {resultado}"""

def test_contar_bloques_10():
    """Verifica contar_bloques(10)"""
    resultado = student.contar_bloques(10)
    assert resultado == 55, f"""❌ contar_bloques(10) debería ser 55, se obtuvo {resultado}"""

def test_salida_completa_1():
    """Verifica salida completa con n=1"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("1")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "Para una piramide de 1 niveles se necesitan 1 bloques"

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

    assert output == "Para una piramide de 5 niveles se necesitan 15 bloques"
