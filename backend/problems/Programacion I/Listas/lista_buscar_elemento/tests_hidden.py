import importlib.util
import os
from io import StringIO
import sys

spec = importlib.util.spec_from_file_location('student_code', os.path.join(os.getcwd(), 'student_code.py'))
student = importlib.util.module_from_spec(spec)
spec.loader.exec_module(student)

def test_buscar_primero():
    old_stdin, old_stdout = sys.stdin, sys.stdout
    sys.stdin, sys.stdout = StringIO("10 20 30\n10"), StringIO()
    student.main()
    output = sys.stdout.getvalue().strip()
    sys.stdin, sys.stdout = old_stdin, old_stdout
    assert output == "Si", f"❌ Para buscar 10 en [10,20,30]: esperaba 'Si', obtuve '{output}'"

def test_buscar_ultimo():
    old_stdin, old_stdout = sys.stdin, sys.stdout
    sys.stdin, sys.stdout = StringIO("10 20 30\n30"), StringIO()
    student.main()
    output = sys.stdout.getvalue().strip()
    sys.stdin, sys.stdout = old_stdin, old_stdout
    assert output == "Si", f"❌ Para buscar 30 en [10,20,30]: esperaba 'Si', obtuve '{output}'"

def test_buscar_negativo():
    old_stdin, old_stdout = sys.stdin, sys.stdout
    sys.stdin, sys.stdout = StringIO("-5 -3 -1\n-3"), StringIO()
    student.main()
    output = sys.stdout.getvalue().strip()
    sys.stdin, sys.stdout = old_stdin, old_stdout
    assert output == "Si", f"❌ Para buscar -3 en [-5,-3,-1]: esperaba 'Si', obtuve '{output}'"
