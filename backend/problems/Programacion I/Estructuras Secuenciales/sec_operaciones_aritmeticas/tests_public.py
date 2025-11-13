"""
Tests para: Sec Operaciones Aritmeticas
Tema: Estructuras Secuenciales

Este archivo contiene tests públicos que el estudiante puede ver.
Los tests verifican que la solución cumpla con todos los requisitos.
"""

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

def test_10_y_2():
    """Test con 10 y 2"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("10\n2")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    expected = "12\n8\n20\n5.0"
    assert output == expected, f"""❌ Operaciones incorrectas
   Para a=10, b=2: se esperaba:
   12 (suma)
   8 (resta)
   20 (multiplicación)
   5.0 (división)
   Pero se obtuvo: '{output}'
   💡 Pista: Debes imprimir 4 líneas con los resultados de +, -, *, /"""

def test_15_y_3():
    """Test con 15 y 3"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("15\n3")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    expected = "18\n12\n45\n5.0"
    assert output == expected, f"""❌ Operaciones incorrectas
   Para a=15, b=3: se esperaba:
   18 (suma)
   12 (resta)
   45 (multiplicación)
   5.0 (división)
   Pero se obtuvo: '{output}'
   💡 Pista: Debes imprimir 4 líneas con los resultados de +, -, *, /"""

