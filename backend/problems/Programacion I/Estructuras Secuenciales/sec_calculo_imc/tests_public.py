"""
Tests para: Sec Calculo Imc
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

def test_imc_normal():
    """Test IMC normal"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("1.75\n70")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    expected = "22.86"
    assert output == expected, f"""❌ IMC incorrecto
   Para altura=1.75m y peso=70kg: se esperaba '{expected}', se obtuvo '{output}'
   💡 Pista: IMC = peso / (altura²). Recuerda usar formato .2f para 2 decimales"""

def test_imc_bajo():
    """Test IMC bajo"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("1.80\n60")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    expected = "18.52"
    assert output == expected, f"""❌ IMC incorrecto
   Para altura=1.80m y peso=60kg: se esperaba '{expected}', se obtuvo '{output}'
   💡 Pista: IMC = peso / (altura²). Recuerda usar formato .2f para 2 decimales"""

