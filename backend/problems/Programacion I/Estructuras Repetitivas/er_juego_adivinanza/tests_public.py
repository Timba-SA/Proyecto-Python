import importlib.util
import os
from io import StringIO
import sys
import random

spec = importlib.util.spec_from_file_location('student_code', os.path.join(os.getcwd(), 'student_code.py'))
student = importlib.util.module_from_spec(spec)

def test_existe_funcion():
    """Verifica que existe la función main"""
    spec.loader.exec_module(student)
    assert hasattr(student, 'main'), 'Debe existir la función main'

def test_cuenta_intentos():
    """Verifica que cuenta los intentos correctamente"""
    # Fijar semilla para tener un número predecible
    random.seed(42)
    spec.loader.exec_module(student)
    
    old_stdout = sys.stdout
    old_stdin = sys.stdin
    
    # Con seed 42, el número es 1
    sys.stdin = StringIO('5\n3\n1\n')
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue()
    sys.stdout = old_stdout
    sys.stdin = old_stdin

    assert '3' in output, "Debe mostrar 3 intentos"
