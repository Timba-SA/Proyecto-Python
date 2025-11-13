"""
Tests para: Lista Invertir
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

def test_invertir_negativos():
    old_stdin, old_stdout = sys.stdin, sys.stdout
    sys.stdin, sys.stdout = StringIO("-1 -2 -3"), StringIO()
    student.main()
    output = sys.stdout.getvalue().strip()
    sys.stdin, sys.stdout = old_stdin, old_stdout
    assert output == "-3 -2 -1", f"❌ Para [-1,-2,-3]: esperaba '-3 -2 -1', obtuve '{output}'"

def test_invertir_pares():
    old_stdin, old_stdout = sys.stdin, sys.stdout
    sys.stdin, sys.stdout = StringIO("10 20"), StringIO()
    student.main()
    output = sys.stdout.getvalue().strip()
    sys.stdin, sys.stdout = old_stdin, old_stdout
    assert output == "20 10", f"❌ Para [10,20]: esperaba '20 10', obtuve '{output}'"
