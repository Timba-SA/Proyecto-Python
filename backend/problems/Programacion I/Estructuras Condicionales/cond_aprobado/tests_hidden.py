import importlib.util
import os
from io import StringIO
import sys

spec = importlib.util.spec_from_file_location('student_code', os.path.join(os.getcwd(), 'student_code.py'))
student = importlib.util.module_from_spec(spec)
spec.loader.exec_module(student)

def test_nota_perfecta():
    """Verifica caso de nota perfecta"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("10")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "Aprobado", f"""❌ Error con nota perfecta
   Para nota=10: se esperaba 'Aprobado', se obtuvo '{output}'
   💡 Pista: 10 >= 6, por lo tanto aprobó"""

def test_nota_muy_baja():
    """Verifica caso de nota muy baja"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("1")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "Desaprobado", f"""❌ Error con nota muy baja
   Para nota=1: se esperaba 'Desaprobado', se obtuvo '{output}'
   💡 Pista: 1 < 6, por lo tanto desaprobó"""

def test_nota_decimal_aprobado():
    """Verifica con nota decimal aprobado"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("6.5")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "Aprobado", f"""❌ Error con decimales
   Para nota=6.5: se esperaba 'Aprobado', se obtuvo '{output}'
   💡 Pista: 6.5 >= 6, por lo tanto aprobó"""

def test_nota_decimal_desaprobado():
    """Verifica con nota decimal desaprobado"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("5.9")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "Desaprobado", f"""❌ Error con decimales cercanos al límite
   Para nota=5.9: se esperaba 'Desaprobado', se obtuvo '{output}'
   💡 Pista: 5.9 < 6, por lo tanto desaprobó (falta 0.1 para aprobar)"""
