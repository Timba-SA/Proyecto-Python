import importlib.util
import os
from io import StringIO
import sys

spec = importlib.util.spec_from_file_location('student_code', os.path.join(os.getcwd(), 'student_code.py'))
student = importlib.util.module_from_spec(spec)
spec.loader.exec_module(student)

def test_invertir_123():
    """Verifica inversión de 123"""
    old_stdout = sys.stdout
    old_stdin = sys.stdin
    
    sys.stdin = StringIO('123\n')
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue()
    sys.stdout = old_stdout
    sys.stdin = old_stdin

    assert '321' in output, "123 invertido es 321"

def test_un_digito():
    """Verifica número de un dígito"""
    old_stdout = sys.stdout
    old_stdin = sys.stdin
    
    sys.stdin = StringIO('9\n')
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue()
    sys.stdout = old_stdout
    sys.stdin = old_stdin

    assert '9' in output, "9 invertido es 9"
