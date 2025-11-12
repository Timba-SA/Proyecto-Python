import importlib.util
import os
from io import StringIO
import sys

spec = importlib.util.spec_from_file_location('student_code', os.path.join(os.getcwd(), 'student_code.py'))
student = importlib.util.module_from_spec(spec)
spec.loader.exec_module(student)

def test_saludo_nombre_largo():
    """Verifica saludo con nombre largo"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("Anastasia")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    expected = "Hola Anastasia!"
    assert output == expected, f"""❌ Saludo incorrecto
   Para nombre='Anastasia': se esperaba '{expected}', se obtuvo '{output}'
   💡 Pista: Debe funcionar con nombres de cualquier longitud"""

def test_formato_exacto():
    """Verifica formato exacto"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("Ana")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    expected = "Hola Ana!"
    assert output == expected, f"""❌ Formato incorrecto
   Para nombre='Ana': se esperaba '{expected}', se obtuvo '{output}'
   💡 Pista: Revisa que no haya espacios extra y que esté el signo !"""

