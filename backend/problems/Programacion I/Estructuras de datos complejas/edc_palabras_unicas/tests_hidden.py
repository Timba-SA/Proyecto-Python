"""
Tests para: Edc Palabras Unicas
Tema: Estructuras de datos complejas

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

def test_recuento():
    """Verifica que cuenta correctamente las apariciones"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("hola mundo hola")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert "Recuento" in output or "recuento" in output, "Debe mostrar 'Recuento'"
    assert "'hola': 2" in output or '"hola": 2' in output, "hola debe aparecer 2 veces"
    assert "'mundo': 1" in output or '"mundo": 1' in output, "mundo debe aparecer 1 vez"
