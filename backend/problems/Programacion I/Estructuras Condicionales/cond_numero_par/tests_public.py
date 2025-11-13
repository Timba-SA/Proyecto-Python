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

def test_existe_funcion():
    """Verifica que existe la función main"""
    assert hasattr(student, 'main'), 'Debe existir la función main'

def test_numero_par_basico():
    """Verifica con número par básico"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("4")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "Ha ingresado un número par", f"""❌ Respuesta incorrecta
   Para número=4 (par): se esperaba 'Ha ingresado un número par', se obtuvo '{output}'
   💡 Pista: Usa el operador módulo %. Si numero % 2 == 0, es par"""

def test_numero_impar_basico():
    """Verifica con número impar básico"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("7")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "Por favor, ingrese un número par", f"""❌ Respuesta incorrecta
   Para número=7 (impar): se esperaba 'Por favor, ingrese un número par', se obtuvo '{output}'
   💡 Pista: Si numero % 2 != 0, es impar"""

def test_cero_es_par():
    """Verifica que cero es par"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("0")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "Ha ingresado un número par", f"""❌ Error con el cero
   Para número=0: se esperaba 'Ha ingresado un número par', se obtuvo '{output}'
   💡 Pista: 0 es par porque 0 % 2 = 0 (ver nota pedagógica en el enunciado)"""
