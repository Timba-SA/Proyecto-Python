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

def test_mayor_edad_basico():
    """Verifica caso básico mayor de edad (20 años)"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("20")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "Es mayor de edad", f"""❌ Respuesta incorrecta
   Para edad=20: se esperaba 'Es mayor de edad', se obtuvo '{output}'
   💡 Pista: La condición debe ser edad >= 19"""

def test_menor_edad_basico():
    """Verifica caso básico menor de edad (15 años)"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("15")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "Es menor de edad", f"""❌ Respuesta incorrecta
   Para edad=15: se esperaba 'Es menor de edad', se obtuvo '{output}'
   💡 Pista: Si edad < 19, es menor de edad"""

def test_edad_limite_18():
    """Verifica el caso límite de 18 años (menor de edad)"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("18")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "Es menor de edad", f"Con 18 años debe ser 'Es menor de edad' (condición: edad >= 19), se obtuvo '{output}'"

def test_edad_limite_19():
    """Verifica el caso límite de 19 años (mayor de edad)"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("19")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "Es mayor de edad", f"Con 19 años debe ser 'Es mayor de edad' (condición: edad >= 19), se obtuvo '{output}'"
