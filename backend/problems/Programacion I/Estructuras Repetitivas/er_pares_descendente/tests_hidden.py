import importlib.util
import os
from io import StringIO
import sys

spec = importlib.util.spec_from_file_location('student_code', os.path.join(os.getcwd(), 'student_code.py'))
student = importlib.util.module_from_spec(spec)
spec.loader.exec_module(student)

def test_cantidad_correcta():
    """Verifica que imprime exactamente 51 números pares"""
    old_stdout = sys.stdout
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue()
    sys.stdout = old_stdout

    lineas = [l for l in output.strip().split('\n') if l.strip()]
    assert len(lineas) == 51, f"Debe imprimir 51 pares (0 a 100), imprimió {len(lineas)}"
