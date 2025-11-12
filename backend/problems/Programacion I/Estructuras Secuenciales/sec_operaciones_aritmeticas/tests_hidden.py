import importlib.util
import os
from io import StringIO
import sys

spec = importlib.util.spec_from_file_location('student_code', os.path.join(os.getcwd(), 'student_code.py'))
student = importlib.util.module_from_spec(spec)
spec.loader.exec_module(student)

def test_20_y_4():
    """Test con 20 y 4"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("20\n4")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    expected = "24\n16\n80\n5.0"
    assert output == expected, f"""❌ Operaciones incorrectas
   Para a=20, b=4: se esperaba '{expected}', se obtuvo '{output}'
   💡 Pista: Las 4 operaciones son: 20+4, 20-4, 20*4, 20/4"""

def test_7_y_2():
    """Test con división decimal"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("7\n2")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    expected = "9\n5\n14\n3.5"
    assert output == expected, f"""❌ Operaciones incorrectas con división decimal
   Para a=7, b=2: se esperaba '{expected}', se obtuvo '{output}'
   💡 Pista: 7/2 = 3.5 (usa / no // para división normal)"""

