"""
Tests para: Lista Filtrar Positivos
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

def test_filtrar_mixtos():
    old_stdin, old_stdout = sys.stdin, sys.stdout
    sys.stdin, sys.stdout = StringIO("-5 3 -1 8 0 2"), StringIO()
    student.main()
    output = sys.stdout.getvalue().strip()
    sys.stdin, sys.stdout = old_stdin, old_stdout
    assert output == "3 8 2", f"❌ Para [-5,3,-1,8,0,2]: esperaba '3 8 2', obtuve '{output}'"

def test_solo_negativos():
    old_stdin, old_stdout = sys.stdin, sys.stdout
    sys.stdin, sys.stdout = StringIO("-1 -2 -3"), StringIO()
    student.main()
    output = sys.stdout.getvalue().strip()
    sys.stdin, sys.stdout = old_stdin, old_stdout
    assert output == "", f"❌ Para [-1,-2,-3]: esperaba '', obtuve '{output}'"
