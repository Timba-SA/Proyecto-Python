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

def test_nota_aprobada():
    """Verifica caso de nota aprobada"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("7")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "Aprobado", f"""❌ Respuesta incorrecta
   Para nota=7: se esperaba 'Aprobado', se obtuvo '{output}'
   💡 Pista: Si nota >= 6, está aprobado"""

def test_nota_desaprobada():
    """Verifica caso de nota desaprobada"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("4")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "Desaprobado", f"""❌ Respuesta incorrecta
   Para nota=4: se esperaba 'Desaprobado', se obtuvo '{output}'
   💡 Pista: Si nota < 6, está desaprobado"""

def test_nota_limite_aprobado():
    """Verifica el caso límite de 6 (aprobado)"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("6")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "Aprobado", f"""❌ Error en caso límite
   Para nota=6 (límite): se esperaba 'Aprobado', se obtuvo '{output}'
   💡 Pista: nota=6 es el mínimo para aprobar (condición: nota >= 6)"""
