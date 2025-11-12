import importlib.util
import os
from io import StringIO
import sys

spec = importlib.util.spec_from_file_location('student_code', os.path.join(os.getcwd(), 'student_code.py'))
student = importlib.util.module_from_spec(spec)
spec.loader.exec_module(student)

def test_existe_funcion():
    assert hasattr(student, 'main'), 'Debe existir la función main'

def test_menor_simple():
    old_stdin, old_stdout = sys.stdin, sys.stdout
    sys.stdin, sys.stdout = StringIO("5 2 9 1 7"), StringIO()
    student.main()
    output = sys.stdout.getvalue().strip()
    sys.stdin, sys.stdout = old_stdin, old_stdout
    assert output == "1", f"❌ Para [5,2,9,1,7]: esperaba '1', obtuve '{output}'"

def test_menor_negativos():
    old_stdin, old_stdout = sys.stdin, sys.stdout
    sys.stdin, sys.stdout = StringIO("-5 -2 -9 -1"), StringIO()
    student.main()
    output = sys.stdout.getvalue().strip()
    sys.stdin, sys.stdout = old_stdin, old_stdout
    assert output == "-9", f"❌ Para [-5,-2,-9,-1]: esperaba '-9', obtuve '{output}'"
