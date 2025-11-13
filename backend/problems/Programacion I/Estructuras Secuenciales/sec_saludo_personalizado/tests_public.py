"""
Tests para: Sec Saludo Personalizado
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

def test_saludo_juan():
    """Verifica saludo con nombre Juan"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("Juan")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    expected = "Hola Juan!"
    assert output == expected, f"""❌ Saludo incorrecto
   Para nombre='Juan': se esperaba '{expected}', se obtuvo '{output}'
   💡 Pista: Formato debe ser "Hola {{nombre}}!" (con espacio después de Hola y ! al final)"""

def test_saludo_maria():
    """Verifica saludo con nombre María"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("María")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    expected = "Hola María!"
    assert output == expected, f"""❌ Saludo incorrecto
   Para nombre='María': se esperaba '{expected}', se obtuvo '{output}'
   💡 Pista: Formato debe ser "Hola {{nombre}}!" (con acento en í)"""

