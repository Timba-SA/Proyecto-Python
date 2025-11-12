import importlib.util
import os
from io import StringIO
import sys

spec = importlib.util.spec_from_file_location('student_code', os.path.join(os.getcwd(), 'student_code.py'))
student = importlib.util.module_from_spec(spec)
spec.loader.exec_module(student)

def test_mayor_primero():
    """Verifica cuando el mayor es el primero"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("10 5 3 1")
    sys.stdout = StringIO()
    student.main()
    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout
    assert output == "10", f"❌ Para [10,5,3,1]: esperaba '10', obtuve '{output}'"

def test_mayor_ultimo():
    """Verifica cuando el mayor es el último"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("1 3 5 10")
    sys.stdout = StringIO()
    student.main()
    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout
    assert output == "10", f"❌ Para [1,3,5,10]: esperaba '10', obtuve '{output}'"

def test_mayor_repetido():
    """Verifica cuando hay repetidos"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("5 5 5 5")
    sys.stdout = StringIO()
    student.main()
    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout
    assert output == "5", f"❌ Para [5,5,5,5]: esperaba '5', obtuve '{output}'"
