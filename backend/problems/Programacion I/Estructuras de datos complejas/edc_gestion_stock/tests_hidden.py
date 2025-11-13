"""
Tests para: Edc Gestion Stock
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

def test_agregar_nuevo():
    """Verifica que agrega un producto nuevo"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("Naranjas\n10")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert "Naranjas" in output, "Debe mencionar Naranjas"
    assert "10" in output, "Debe mostrar stock de 10"
    assert "agregado" in output.lower() or "nuevo" in output.lower(), "Debe indicar que es un producto nuevo"
