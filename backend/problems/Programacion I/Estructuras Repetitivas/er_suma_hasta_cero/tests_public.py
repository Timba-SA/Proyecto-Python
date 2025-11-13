"""
Tests para: Er Suma Hasta Cero
Tema: Estructuras Repetitivas

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

def test_suma_varios_numeros():
    """Verifica suma de varios números"""
    old_stdout = sys.stdout
    old_stdin = sys.stdin
    
    sys.stdin = StringIO('5\n10\n3\n0\n')
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue()
    sys.stdout = old_stdout
    sys.stdin = old_stdin

    assert '18' in output, "5+10+3 = 18"
