import importlib.util
import os
from io import StringIO
import sys

spec = importlib.util.spec_from_file_location('student_code', os.path.join(os.getcwd(), 'student_code.py'))
student = importlib.util.module_from_spec(spec)
spec.loader.exec_module(student)

def test_multiples_contactos():
    """Verifica que almacena correctamente múltiples contactos"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("Juan\n123456\nAna\n987654\nPedro\n555111\nMaria\n444222\nLuis\n333999\nAna")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert "987654" in output, "Debe encontrar el número de Ana correctamente"
