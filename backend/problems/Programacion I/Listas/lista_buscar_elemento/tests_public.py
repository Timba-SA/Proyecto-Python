"""
Tests para: Lista Buscar Elemento
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
    assert hasattr(student, 'main'), 'Debe existir la función main'

def test_elemento_existe():
    old_stdin, old_stdout = sys.stdin, sys.stdout
    sys.stdin, sys.stdout = StringIO("1 2 3 4 5\n3"), StringIO()
    student.main()
    output = sys.stdout.getvalue().strip()
    sys.stdin, sys.stdout = old_stdin, old_stdout
    assert output == "Si", f"❌ Para buscar 3 en [1,2,3,4,5]: esperaba 'Si', obtuve '{output}'"

def test_elemento_no_existe():
    old_stdin, old_stdout = sys.stdin, sys.stdout
    sys.stdin, sys.stdout = StringIO("1 2 3 4 5\n10"), StringIO()
    student.main()
    output = sys.stdout.getvalue().strip()
    sys.stdin, sys.stdout = old_stdin, old_stdout
    assert output == "No", f"❌ Para buscar 10 en [1,2,3,4,5]: esperaba 'No', obtuve '{output}'"
