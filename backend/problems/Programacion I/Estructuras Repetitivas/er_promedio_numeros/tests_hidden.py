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

def test_promedio_100_negativos_positivos():
    """Verifica promedio con números negativos y positivos balanceados"""
    old_stdout = sys.stdout
    old_stdin = sys.stdin
    
    # 50 números con valor -50 y 50 números con valor 50 -> promedio = 0
    numeros = '\n'.join(['-50'] * 50 + ['50'] * 50)
    sys.stdin = StringIO(numeros + '\n')
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue()
    sys.stdout = old_stdout
    sys.stdin = old_stdin

    assert '0' in output, "El promedio debe ser 0"
