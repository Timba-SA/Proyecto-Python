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

def test_empieza_100_termina_0():
    """Verifica que empieza en 100 y termina en 0"""
    old_stdout = sys.stdout
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue()
    sys.stdout = old_stdout

    lineas = output.strip().split('\n')
    assert '100' in lineas[0], "Debe empezar con 100"
    assert '0' in lineas[-1], "Debe terminar con 0"
