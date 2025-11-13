"""
Tests para: Sec Promedio Tres Numeros
Tema: Estructuras Secuenciales

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

def test_existe_funcion():
    """Verifica que existe la función main"""
    assert hasattr(student, 'main'), 'Debe existir la función main'

def test_promedio_10_20_30():
    """Test promedio de 10, 20, 30"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("10\n20\n30")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    expected = "20.0"
    assert output == expected, f"""❌ Promedio incorrecto
   Para (10, 20, 30): se esperaba '{expected}', se obtuvo '{output}'
   💡 Pista: El promedio es (10 + 20 + 30) / 3 = 60 / 3 = 20.0"""

def test_promedio_5_10_15():
    """Test promedio de 5, 10, 15"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("5\n10\n15")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    expected = "10.0"
    assert output == expected, f"""❌ Promedio incorrecto
   Para (5, 10, 15): se esperaba '{expected}', se obtuvo '{output}'
   💡 Pista: El promedio es (5 + 10 + 15) / 3 = 30 / 3 = 10.0"""

