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

def test_interseccion():
    """Verifica la intersección (ambos parciales)"""
    old_stdout = sys.stdout
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue()
    sys.stdout = old_stdout

    assert "4" in output and "5" in output, "Debe mostrar 4 y 5 en la intersección"
    assert "ambos" in output.lower(), "Debe mencionar 'ambos'"

def test_diferencia_simetrica():
    """Verifica la diferencia simétrica (solo uno)"""
    old_stdout = sys.stdout
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue()
    sys.stdout = old_stdout

    numeros = ["1", "2", "3", "6", "7", "8"]
    for num in numeros:
        assert num in output, f"Debe contener {num} en solo uno"
