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

def test_promedio_5_numeros():
    """Verifica promedio de 5 números (debe estar preparado para 100)"""
    old_stdout = sys.stdout
    old_stdin = sys.stdin
    
    # 10, 20, 30, 40, 50 -> promedio = 30
    sys.stdin = StringIO('10\n20\n30\n40\n50\n')
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue()
    sys.stdout = old_stdout
    sys.stdin = old_stdin

    # El promedio puede ser 30 o 30.0
    assert '30' in output, "El promedio de 10,20,30,40,50 debe ser 30"
