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

def test_suma_simple():
    """Verifica suma de números positivos simples"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("1 2 3 4 5")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "15", f"""❌ Respuesta incorrecta
   Para [1, 2, 3, 4, 5]: se esperaba '15', se obtuvo '{output}'
   💡 Pista: Suma todos los elementos: 1+2+3+4+5 = 15"""

def test_suma_negativos():
    """Verifica suma con números negativos"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("-5 5 -3 3")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "0", f"""❌ Respuesta incorrecta
   Para [-5, 5, -3, 3]: se esperaba '0', se obtuvo '{output}'
   💡 Pista: Los números se cancelan: -5+5-3+3 = 0"""

def test_un_elemento():
    """Verifica con lista de un solo elemento"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("100")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "100", f"""❌ Error con un solo elemento
   Para [100]: se esperaba '100', se obtuvo '{output}'
   💡 Pista: La suma de un solo elemento es el elemento mismo"""
