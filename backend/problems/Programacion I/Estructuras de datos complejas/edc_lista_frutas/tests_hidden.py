import importlib.util
import os
from io import StringIO
import sys

spec = importlib.util.spec_from_file_location('student_code', os.path.join(os.getcwd(), 'student_code.py'))
student = importlib.util.module_from_spec(spec)
spec.loader.exec_module(student)

def test_contiene_frutas():
    """Verifica que la lista contiene todas las frutas"""
    old_stdout = sys.stdout
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdout = old_stdout

    frutas = ['Banana', 'Ananá', 'Melón', 'Uva', 'Naranja', 'Manzana', 'Pera']
    for fruta in frutas:
        assert fruta in output, f"Falta {fruta} en la lista"
