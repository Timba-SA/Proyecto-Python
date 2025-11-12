import importlib.util
import os
from io import StringIO
import sys

spec = importlib.util.spec_from_file_location('student_code', os.path.join(os.getcwd(), 'student_code.py'))
student = importlib.util.module_from_spec(spec)
spec.loader.exec_module(student)

def test_numeros_consecutivos():
    """Verifica que números consecutivos dan suma 0"""
    old_stdout = sys.stdout
    old_stdin = sys.stdin
    
    sys.stdin = StringIO('5\n6\n')
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue()
    sys.stdout = old_stdout
    sys.stdin = old_stdin

    assert '0' in output, "Entre 5 y 6 no hay números, suma = 0"

def test_orden_inverso():
    """Verifica que funciona si los números están en orden inverso"""
    old_stdout = sys.stdout
    old_stdin = sys.stdin
    
    sys.stdin = StringIO('10\n5\n')
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue()
    sys.stdout = old_stdout
    sys.stdin = old_stdin

    assert '30' in output, "Entre 5 y 10 (excluyendo): 6+7+8+9 = 30"
