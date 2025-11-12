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

def test_inversion_correcta():
    """Verifica que las capitales son claves"""
    old_stdout = sys.stdout
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue()
    sys.stdout = old_stdout

    assert "'Buenos Aires'" in output or '"Buenos Aires"' in output, "Buenos Aires debe ser clave"
    assert "'Santiago'" in output or '"Santiago"' in output, "Santiago debe ser clave"
    assert "'Argentina'" in output or '"Argentina"' in output, "Argentina debe ser valor"
