import importlib.util
import os
from io import StringIO
import sys

spec = importlib.util.spec_from_file_location('student_code', os.path.join(os.getcwd(), 'student_code.py'))
student = importlib.util.module_from_spec(spec)
spec.loader.exec_module(student)

def test_promedio_decimales():
    """Verifica promedio con decimales"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("2.5 3.5 4.5")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "3.5", f"""❌ Error con decimales
   Para [2.5, 3.5, 4.5]: se esperaba '3.5', se obtuvo '{output}'
   💡 Pista: (2.5+3.5+4.5)/3 = 10.5/3 = 3.5"""

def test_promedio_negativos():
    """Verifica promedio con números negativos"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("-10 10 -5 5")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "0.0", f"""❌ Error con negativos
   Para [-10, 10, -5, 5]: se esperaba '0.0', se obtuvo '{output}'
   💡 Pista: Los números se cancelan: suma=0, promedio=0.0"""

def test_promedio_un_elemento():
    """Verifica promedio de un solo elemento"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("42")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "42.0", f"""❌ Error con un elemento
   Para [42]: se esperaba '42.0', se obtuvo '{output}'
   💡 Pista: El promedio de un elemento es el elemento mismo"""
