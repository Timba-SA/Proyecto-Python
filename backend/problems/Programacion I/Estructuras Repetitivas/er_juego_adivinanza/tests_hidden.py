"""
Tests para: Er Juego Adivinanza
Tema: Estructuras Repetitivas

Este archivo contiene tests públicos que el estudiante puede ver.
Los tests verifican que la solución cumpla con todos los requisitos.
"""

import importlib.util
import os
from io import StringIO
import sys
import random

spec = importlib.util.spec_from_file_location('student_code', os.path.join(os.getcwd(), 'student_code.py'))
student = importlib.util.module_from_spec(spec)

def test_primer_intento():
    """Verifica cuando acierta en el primer intento"""
    random.seed(42)
    spec.loader.exec_module(student)
    
    old_stdout = sys.stdout
    old_stdin = sys.stdin
    
    # Con seed 42, el número es 1
    sys.stdin = StringIO('1\n')
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue()
    sys.stdout = old_stdout
    sys.stdin = old_stdin

    assert '1' in output, "Debe mostrar 1 intento"
