import importlib.util
import os
from io import StringIO
import sys

spec = importlib.util.spec_from_file_location('student_code', os.path.join(os.getcwd(), 'student_code.py'))
student = importlib.util.module_from_spec(spec)
spec.loader.exec_module(student)

def test_union():
    """Verifica la unión (al menos uno)"""
    old_stdout = sys.stdout
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue()
    sys.stdout = old_stdout

    numeros = ["1", "2", "3", "4", "5", "6", "7", "8"]
    for num in numeros:
        assert num in output, f"Debe contener {num} en la unión"
