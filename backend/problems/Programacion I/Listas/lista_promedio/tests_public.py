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

def test_promedio_simple():
    """Verifica promedio de números simples"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("10 20 30 40")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "25.0", f"""❌ Respuesta incorrecta
   Para [10, 20, 30, 40]: se esperaba '25.0', se obtuvo '{output}'
   💡 Pista: (10+20+30+40)/4 = 100/4 = 25.0"""

def test_promedio_iguales():
    """Verifica promedio de números iguales"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("5 5 5 5 5")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "5.0", f"""❌ Respuesta incorrecta
   Para [5, 5, 5, 5, 5]: se esperaba '5.0', se obtuvo '{output}'
   💡 Pista: Si todos son iguales, el promedio es ese número"""

def test_promedio_tres():
    """Verifica promedio de tres números"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("7 8 9")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "8.0", f"""❌ Respuesta incorrecta
   Para [7, 8, 9]: se esperaba '8.0', se obtuvo '{output}'
   💡 Pista: (7+8+9)/3 = 24/3 = 8.0"""
