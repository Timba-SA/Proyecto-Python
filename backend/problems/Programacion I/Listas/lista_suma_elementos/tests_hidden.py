import importlib.util
import os
from io import StringIO
import sys

spec = importlib.util.spec_from_file_location('student_code', os.path.join(os.getcwd(), 'student_code.py'))
student = importlib.util.module_from_spec(spec)
spec.loader.exec_module(student)

def test_suma_cero():
    """Verifica suma que resulta en cero"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("0 0 0")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "0", f"""❌ Error con ceros
   Para [0, 0, 0]: se esperaba '0', se obtuvo '{output}'
   💡 Pista: La suma de ceros es cero"""

def test_suma_grande():
    """Verifica suma de números grandes"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("100 200 300 400")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "1000", f"""❌ Error con números grandes
   Para [100, 200, 300, 400]: se esperaba '1000', se obtuvo '{output}'
   💡 Pista: Suma correctamente: 100+200+300+400 = 1000"""

def test_suma_mixta():
    """Verifica suma mixta positivos y negativos"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("10 -5 20 -3 8")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "30", f"""❌ Error con números mixtos
   Para [10, -5, 20, -3, 8]: se esperaba '30', se obtuvo '{output}'
   💡 Pista: 10-5+20-3+8 = 30"""
