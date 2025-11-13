"""
Tests para: Cond Mayor Edad
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

def test_mayor_edad_avanzado():
    """Verifica con edad muy alta (100 años)"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("100")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "Es mayor de edad", f"Con 100 años debe ser mayor de edad, se obtuvo '{output}'"

def test_menor_edad_nino():
    """Verifica con edad muy baja (5 años)"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("5")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "Es menor de edad", f"Con 5 años debe ser menor de edad, se obtuvo '{output}'"

def test_edad_cero():
    """Verifica con edad 0"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("0")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "Es menor de edad", f"Con 0 años debe ser menor de edad, se obtuvo '{output}'"

def test_edad_17():
    """Verifica límite inferior: 17 años (último menor de edad)"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("17")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "Es menor de edad", f"Con 17 años debe ser menor de edad, se obtuvo '{output}'"

def test_edad_20():
    """Verifica claramente mayor de edad: 20 años"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("20")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "Es mayor de edad", f"Con 20 años debe ser mayor de edad, se obtuvo '{output}'"
