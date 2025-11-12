import importlib.util
import os
from io import StringIO
import sys

spec = importlib.util.spec_from_file_location('student_code', os.path.join(os.getcwd(), 'student_code.py'))
student = importlib.util.module_from_spec(spec)
spec.loader.exec_module(student)

def test_todos_duplicados():
    old_stdin, old_stdout = sys.stdin, sys.stdout
    sys.stdin, sys.stdout = StringIO("5 5 5 5"), StringIO()
    student.main()
    output = sys.stdout.getvalue().strip()
    sys.stdin, sys.stdout = old_stdin, old_stdout
    assert output == "5", f"❌ Para [5,5,5,5]: esperaba '5', obtuve '{output}'"

def test_duplicados_desordenados():
    old_stdin, old_stdout = sys.stdin, sys.stdout
    sys.stdin, sys.stdout = StringIO("3 1 2 1 3 2"), StringIO()
    student.main()
    output = sys.stdout.getvalue().strip()
    sys.stdin, sys.stdout = old_stdin, old_stdout
    assert output == "1 2 3", f"❌ Para [3,1,2,1,3,2]: esperaba '1 2 3', obtuve '{output}'"

def test_negativos_duplicados():
    old_stdin, old_stdout = sys.stdin, sys.stdout
    sys.stdin, sys.stdout = StringIO("-1 -1 0 0 1 1"), StringIO()
    student.main()
    output = sys.stdout.getvalue().strip()
    sys.stdin, sys.stdout = old_stdin, old_stdout
    assert output == "-1 0 1", f"❌ Para [-1,-1,0,0,1,1]: esperaba '-1 0 1', obtuve '{output}'"
