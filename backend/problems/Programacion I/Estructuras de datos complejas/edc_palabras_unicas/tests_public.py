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

def test_existe_funcion():
    """Verifica que existe la función main"""
    assert hasattr(student, 'main'), 'Debe existir la función main'

def test_palabras_unicas():
    """Verifica que muestra palabras únicas"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("hola mundo hola")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert "Palabras únicas" in output or "palabras únicas" in output, "Debe mostrar 'Palabras únicas'"
    assert "hola" in output and "mundo" in output, "Debe contener las palabras únicas"
