import importlib.util
import os
from io import StringIO
import sys

spec = importlib.util.spec_from_file_location('student_code', os.path.join(os.getcwd(), 'student_code.py'))
student = importlib.util.module_from_spec(spec)
spec.loader.exec_module(student)

def test_existe_funcion():
    assert hasattr(student, 'main'), 'Debe existir la función main'

def test_concatenar_simple():
    old_stdin, old_stdout = sys.stdin, sys.stdout
    sys.stdin, sys.stdout = StringIO("1 2 3\n4 5 6"), StringIO()
    student.main()
    output = sys.stdout.getvalue().strip()
    sys.stdin, sys.stdout = old_stdin, old_stdout
    assert output == "1 2 3 4 5 6", f"❌ Para [1,2,3]+[4,5,6]: esperaba '1 2 3 4 5 6', obtuve '{output}'"

def test_concatenar_vacia():
    old_stdin, old_stdout = sys.stdin, sys.stdout
    sys.stdin, sys.stdout = StringIO("1 2 3\n"), StringIO()
    student.main()
    output = sys.stdout.getvalue().strip()
    sys.stdin, sys.stdout = old_stdin, old_stdout
    assert output == "1 2 3", f"❌ Para [1,2,3]+[]: esperaba '1 2 3', obtuve '{output}'"
