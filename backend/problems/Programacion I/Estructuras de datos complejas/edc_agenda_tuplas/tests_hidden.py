import importlib.util
import os
from io import StringIO
import sys

spec = importlib.util.spec_from_file_location('student_code', os.path.join(os.getcwd(), 'student_code.py'))
student = importlib.util.module_from_spec(spec)
spec.loader.exec_module(student)

def test_actividad_no_encontrada():
    """Verifica el mensaje cuando no hay actividad"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("viernes\n10:00")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert "no hay" in output.lower() or "no existe" in output.lower(), "Debe indicar que no hay actividad"
