"""
Tests para: Er Promedio Numeros
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

def test_promedio_con_negativos():
    """Verifica promedio con números negativos"""
    old_stdout = sys.stdout
    old_stdin = sys.stdin
    
    # -10, 10, -20, 20, 0 -> promedio = 0
    sys.stdin = StringIO('-10\n10\n-20\n20\n0\n')
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue()
    sys.stdout = old_stdout
    sys.stdin = old_stdin

    assert '0' in output, "El promedio debe ser 0"
