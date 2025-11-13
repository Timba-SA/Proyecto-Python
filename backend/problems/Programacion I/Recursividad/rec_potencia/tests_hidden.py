"""
Tests para: Rec Potencia
Tema: Recursividad

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

def test_potencia_10_2():
    """Verifica 10 elevado a 2"""
    resultado = student.potencia(10, 2)
    assert resultado == 100

def test_potencia_2_10():
    """Verifica 2 elevado a 10"""
    resultado = student.potencia(2, 10)
    assert resultado == 1024

def test_salida_5_0():
    """Verifica salida con base=5, exponente=0"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("5\n0")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "El resultado de 5 elevado a 0 es 1"

def test_salida_10_2():
    """Verifica salida con base=10, exponente=2"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("10\n2")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "El resultado de 10 elevado a 2 es 100"
