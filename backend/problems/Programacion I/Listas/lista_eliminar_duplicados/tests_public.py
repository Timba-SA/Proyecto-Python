import importlib.util
import os
from io import StringIO
import sys

spec = importlib.util.spec_from_file_location('student_code', os.path.join(os.getcwd(), 'student_code.py'))
student = importlib.util.module_from_spec(spec)
spec.loader.exec_module(student)

def test_existe_funcion():
    assert hasattr(student, 'main'), 'Debe existir la función main'

def test_eliminar_duplicados_simple():
    old_stdin, old_stdout = sys.stdin, sys.stdout
    sys.stdin, sys.stdout = StringIO("1 2 2 3 3 3 4"), StringIO()
    student.main()
    output = sys.stdout.getvalue().strip()
    sys.stdin, sys.stdout = old_stdin, old_stdout
    assert output == "1 2 3 4", f"❌ Para [1,2,2,3,3,3,4]: esperaba '1 2 3 4', obtuve '{output}'"

def test_sin_duplicados():
    old_stdin, old_stdout = sys.stdin, sys.stdout
    sys.stdin, sys.stdout = StringIO("1 2 3 4"), StringIO()
    student.main()
    output = sys.stdout.getvalue().strip()
    sys.stdin, sys.stdout = old_stdin, old_stdout
    assert output == "1 2 3 4", f"❌ Para [1,2,3,4]: esperaba '1 2 3 4', obtuve '{output}'"
