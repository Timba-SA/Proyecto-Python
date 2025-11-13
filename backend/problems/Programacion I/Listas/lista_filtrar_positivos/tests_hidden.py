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

def test_solo_positivos():
    old_stdin, old_stdout = sys.stdin, sys.stdout
    sys.stdin, sys.stdout = StringIO("1 2 3 4"), StringIO()
    student.main()
    output = sys.stdout.getvalue().strip()
    sys.stdin, sys.stdout = old_stdin, old_stdout
    assert output == "1 2 3 4", f"❌ Para [1,2,3,4]: esperaba '1 2 3 4', obtuve '{output}'"

def test_con_cero():
    old_stdin, old_stdout = sys.stdin, sys.stdout
    sys.stdin, sys.stdout = StringIO("0 1 0 2 0"), StringIO()
    student.main()
    output = sys.stdout.getvalue().strip()
    sys.stdin, sys.stdout = old_stdin, old_stdout
    assert output == "1 2", f"❌ Para [0,1,0,2,0]: esperaba '1 2' (0 no es positivo), obtuve '{output}'"

def test_un_positivo():
    old_stdin, old_stdout = sys.stdin, sys.stdout
    sys.stdin, sys.stdout = StringIO("-5 -3 10 -1"), StringIO()
    student.main()
    output = sys.stdout.getvalue().strip()
    sys.stdin, sys.stdout = old_stdin, old_stdout
    assert output == "10", f"❌ Para [-5,-3,10,-1]: esperaba '10', obtuve '{output}'"
