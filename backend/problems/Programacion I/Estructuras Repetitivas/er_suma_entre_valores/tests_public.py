import importlib.util
import os
from io import StringIO
import sys

spec = importlib.util.spec_from_file_location('student_code', os.path.join(os.getcwd(), 'student_code.py'))
student = importlib.util.module_from_spec(spec)
spec.loader.exec_module(student)

def test_existe_funcion():
    """Verifica que existe la función main"""
    assert hasattr(student, 'main'), 'Debe existir la función main'

def test_suma_3_a_7():
    """Verifica suma entre 3 y 7 (excluidos)"""
    old_stdout = sys.stdout
    old_stdin = sys.stdin
    
    sys.stdin = StringIO('3\n7\n')
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue()
    sys.stdout = old_stdout
    sys.stdin = old_stdin

    assert '15' in output, "La suma entre 3 y 7 (excluyendo extremos) es 15"
