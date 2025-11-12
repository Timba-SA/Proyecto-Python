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

def test_mayor_primero():
    """Verifica cuando el primer número es mayor"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("10\n5")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "10" or output == "10.0", f"""❌ No devuelve el mayor
   Para a=10, b=5: se esperaba '10', se obtuvo '{output}'
   💡 Pista: Usa if a > b para comparar"""

def test_mayor_segundo():
    """Verifica cuando el segundo número es mayor"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("3\n8")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "8" or output == "8.0", f"""❌ No devuelve el mayor
   Para a=3, b=8: se esperaba '8', se obtuvo '{output}'
   💡 Pista: Si a no es mayor que b, entonces b es el mayor"""

def test_iguales():
    """Verifica cuando ambos números son iguales"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("5\n5")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "5" or output == "5.0", f"""❌ Error cuando son iguales
   Para a=5, b=5: se esperaba '5', se obtuvo '{output}'
   💡 Pista: Si a == b, puedes devolver cualquiera de los dos (son iguales)"""

