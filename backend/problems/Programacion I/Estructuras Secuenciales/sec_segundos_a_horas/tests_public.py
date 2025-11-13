"""
Tests para: Sec Segundos A Horas
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

def test_3600_segundos():
    """Test 3600 segundos (1 hora)"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("3600")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    expected = "3600 segundos equivalen a 1.0 horas"
    assert output == expected, f"""❌ Conversión incorrecta
   Para 3600 segundos: se esperaba '{expected}', se obtuvo '{output}'
   💡 Pista: 1 hora = 3600 segundos. Fórmula: horas = segundos / 3600"""

def test_7200_segundos():
    """Test 7200 segundos (2 horas)"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("7200")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    expected = "7200 segundos equivalen a 2.0 horas"
    assert output == expected, f"""❌ Conversión incorrecta
   Para 7200 segundos: se esperaba '{expected}', se obtuvo '{output}'
   💡 Pista: 7200 / 3600 = 2.0 horas"""

