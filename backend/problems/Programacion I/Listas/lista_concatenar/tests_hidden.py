import importlib.util
import os
from io import StringIO
import sys

spec = importlib.util.spec_from_file_location('student_code', os.path.join(os.getcwd(), 'student_code.py'))
student = importlib.util.module_from_spec(spec)
spec.loader.exec_module(student)

def test_concatenar_un_elemento():
    old_stdin, old_stdout = sys.stdin, sys.stdout
    sys.stdin, sys.stdout = StringIO("1\n2"), StringIO()
    student.main()
    output = sys.stdout.getvalue().strip()
    sys.stdin, sys.stdout = old_stdin, old_stdout
    assert output == "1 2", f"❌ Para [1]+[2]: esperaba '1 2', obtuve '{output}'"

def test_concatenar_negativos():
    old_stdin, old_stdout = sys.stdin, sys.stdout
    sys.stdin, sys.stdout = StringIO("-1 -2\n-3 -4"), StringIO()
    student.main()
    output = sys.stdout.getvalue().strip()
    sys.stdin, sys.stdout = old_stdin, old_stdout
    assert output == "-1 -2 -3 -4", f"❌ Para [-1,-2]+[-3,-4]: esperaba '-1 -2 -3 -4', obtuve '{output}'"

def test_concatenar_desiguales():
    old_stdin, old_stdout = sys.stdin, sys.stdout
    sys.stdin, sys.stdout = StringIO("1\n2 3 4 5"), StringIO()
    student.main()
    output = sys.stdout.getvalue().strip()
    sys.stdin, sys.stdout = old_stdin, old_stdout
    assert output == "1 2 3 4 5", f"❌ Para [1]+[2,3,4,5]: esperaba '1 2 3 4 5', obtuve '{output}'"
