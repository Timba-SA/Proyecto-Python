"""
Tests para: Cond Numero Par
Tema: Estructuras Condicionales

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

def test_numero_par_grande():
    """Verifica con número par grande"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("1000")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "Ha ingresado un número par"

def test_numero_negativo_par():
    """Verifica con número negativo par"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("-4")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "Ha ingresado un número par", f"""❌ Error con números negativos pares
   Para número=-4: se esperaba 'Ha ingresado un número par', se obtuvo '{output}'
   💡 Pista: -4 % 2 = 0, por lo tanto es par"""

def test_numero_negativo_impar():
    """Verifica con número negativo impar"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("-7")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "Por favor, ingrese un número par", f"""❌ Error con números negativos impares
   Para número=-7: se esperaba 'Por favor, ingrese un número par', se obtuvo '{output}'
   💡 Pista: -7 % 2 != 0, por lo tanto es impar"""
