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

def test_opcion_mayusculas():
    """Verifica opción 1 (mayúsculas)"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("pedro\n1")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "PEDRO", f"""❌ Transformación incorrecta
   Para nombre='pedro' y opción=1: se esperaba 'PEDRO', se obtuvo '{output}'
   💡 Pista: Usa .upper() para convertir a mayúsculas"""

def test_opcion_minusculas():
    """Verifica opción 2 (minúsculas)"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("MARIA\n2")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "maria", f"""❌ Transformación incorrecta
   Para nombre='MARIA' y opción=2: se esperaba 'maria', se obtuvo '{output}'
   💡 Pista: Usa .lower() para convertir a minúsculas"""

def test_opcion_title():
    """Verifica opción 3 (primera letra mayúscula)"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("juan\n3")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "Juan", f"""❌ Transformación incorrecta
   Para nombre='juan' y opción=3: se esperaba 'Juan', se obtuvo '{output}'
   💡 Pista: Usa .title() o .capitalize() para primera letra mayúscula"""

def test_opcion_invalida():
    """Verifica opción inválida"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("ana\n5")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "Opción inválida", f"""❌ Error con opción inválida
   Para opción=5: se esperaba 'Opción inválida', se obtuvo '{output}'
   💡 Pista: Si opción no es 1, 2 o 3, devuelve 'Opción inválida'"""
