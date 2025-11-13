"""
Tests para: Lista Mayor Elemento
Tema: Listas

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

def test_mayor_simple():
    """Verifica mayor elemento simple"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("5 2 9 1 7")
    sys.stdout = StringIO()
    student.main()
    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout
    assert output == "9", f"❌ Para [5,2,9,1,7]: esperaba '9', obtuve '{output}'"

def test_mayor_negativos():
    """Verifica mayor con negativos"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("-5 -2 -9 -1")
    sys.stdout = StringIO()
    student.main()
    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout
    assert output == "-1", f"❌ Para [-5,-2,-9,-1]: esperaba '-1', obtuve '{output}'"

def test_mayor_un_elemento():
    """Verifica con un solo elemento"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("42")
    sys.stdout = StringIO()
    student.main()
    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout
    assert output == "42", f"❌ Para [42]: esperaba '42', obtuve '{output}'"
