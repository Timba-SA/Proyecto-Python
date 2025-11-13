"""
Tests para: Edc Promedio Alumnos
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

def test_tres_alumnos():
    """Verifica que procesa los 3 alumnos"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("Sofía\n10\n9\n8\nLuis\n6\n7\n7\nAna\n9\n8\n10")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert "Sofía" in output, "Debe mostrar a Sofía"
    assert "Luis" in output, "Debe mostrar a Luis"
    assert "Ana" in output, "Debe mostrar a Ana"
