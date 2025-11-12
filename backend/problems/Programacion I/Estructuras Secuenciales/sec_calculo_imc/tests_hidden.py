import importlib.util
import os
from io import StringIO
import sys

spec = importlib.util.spec_from_file_location('student_code', os.path.join(os.getcwd(), 'student_code.py'))
student = importlib.util.module_from_spec(spec)
spec.loader.exec_module(student)

def test_imc_alto():
    """Test IMC alto"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("1.65\n85")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    expected = "31.22"
    assert output == expected, f"""❌ IMC incorrecto
   Para altura=1.65m y peso=85kg: se esperaba '{expected}', se obtuvo '{output}'
   💡 Pista: IMC = peso / (altura²). Recuerda usar formato .2f para 2 decimales"""

def test_formato_decimales():
    """Verifica formato 2 decimales"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("1.70\n65")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    expected = "22.49"
    assert output == expected, f"""❌ Formato incorrecto
   Para altura=1.70m y peso=65kg: se esperaba '{expected}', se obtuvo '{output}'
   💡 Pista: Debes usar format() o f-string con :.2f para mostrar exactamente 2 decimales"""

