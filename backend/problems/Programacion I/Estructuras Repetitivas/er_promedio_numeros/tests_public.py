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

def test_existe_funcion():
    """Verifica que existe la función main"""
    assert hasattr(student, 'main'), 'Debe existir la función main'

def test_promedio_100_numeros():
    """Verifica promedio de 100 números"""
    old_stdout = sys.stdout
    old_stdin = sys.stdin
    
    # 100 números del 1 al 100 -> promedio = 50.5
    numeros = '\n'.join(str(i) for i in range(1, 101))
    sys.stdin = StringIO(numeros + '\n')
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue()
    sys.stdout = old_stdout
    sys.stdin = old_stdin

    # El promedio de 1..100 es 50.5
    assert '50.5' in output, "El promedio de 1..100 debe ser 50.5"
