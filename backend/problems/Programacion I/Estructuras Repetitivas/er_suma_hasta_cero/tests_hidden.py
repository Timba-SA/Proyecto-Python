import importlib.util
import os
from io import StringIO
import sys

spec = importlib.util.spec_from_file_location('student_code', os.path.join(os.getcwd(), 'student_code.py'))
student = importlib.util.module_from_spec(spec)
spec.loader.exec_module(student)

def test_solo_cero():
    """Verifica que si se ingresa 0 de inmediato, la suma es 0"""
    old_stdout = sys.stdout
    old_stdin = sys.stdin
    
    sys.stdin = StringIO('0\n')
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue()
    sys.stdout = old_stdout
    sys.stdin = old_stdin

    assert '0' in output, "Si solo se ingresa 0, la suma debe ser 0"
