import importlib.util
import os
from io import StringIO
import sys

spec = importlib.util.spec_from_file_location('student_code', os.path.join(os.getcwd(), 'student_code.py'))
student = importlib.util.module_from_spec(spec)
spec.loader.exec_module(student)

def test_numero_cero():
    """Verifica que el 0 tiene 1 dígito"""
    old_stdout = sys.stdout
    old_stdin = sys.stdin
    
    sys.stdin = StringIO('0\n')
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue()
    sys.stdout = old_stdout
    sys.stdin = old_stdin

    assert '1' in output, "0 tiene 1 dígito"

def test_numero_grande():
    """Verifica un número de 5 dígitos"""
    old_stdout = sys.stdout
    old_stdin = sys.stdin
    
    sys.stdin = StringIO('12345\n')
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue()
    sys.stdout = old_stdout
    sys.stdin = old_stdin

    assert '5' in output, "12345 tiene 5 dígitos"
