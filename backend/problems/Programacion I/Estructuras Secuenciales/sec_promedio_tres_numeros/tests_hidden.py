import importlib.util
import os
from io import StringIO
import sys

spec = importlib.util.spec_from_file_location('student_code', os.path.join(os.getcwd(), 'student_code.py'))
student = importlib.util.module_from_spec(spec)
spec.loader.exec_module(student)

def test_promedio_decimales():
    """Test con decimales"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("7.5\n8.5\n9.0")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    expected = "8.333333333333334"
    assert output == expected, f"""❌ Promedio incorrecto con decimales
   Para (7.5, 8.5, 9.0): se esperaba '{expected}', se obtuvo '{output}'
   💡 Pista: El promedio es (7.5 + 8.5 + 9.0) / 3 = 25.0 / 3"""

def test_promedio_iguales():
    """Test números iguales"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("15\n15\n15")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    expected = "15.0"
    assert output == expected, f"""❌ Promedio incorrecto con números iguales
   Para (15, 15, 15): se esperaba '{expected}', se obtuvo '{output}'
   💡 Pista: Si los tres números son iguales, el promedio es ese mismo número"""

def test_promedio_con_negativos():
    """Test con números negativos"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("-5\n10\n15")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    # Promedio: (-5 + 10 + 15) / 3 = 20 / 3 = 6.666666666666667
    expected = "6.666666666666667"
    assert output == expected, f"❌ Promedio incorrecto con números negativos\n   Para (-5, 10, 15): se esperaba '{expected}', se obtuvo '{output}'\n   💡 Pista: El promedio es la suma de los tres números dividida entre 3"

