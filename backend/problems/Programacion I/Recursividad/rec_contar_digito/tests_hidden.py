import importlib.util
import os
from io import StringIO
import sys

spec = importlib.util.spec_from_file_location('student_code', os.path.join(os.getcwd(), 'student_code.py'))
student = importlib.util.module_from_spec(spec)
spec.loader.exec_module(student)

def test_contar_digito_un_digito():
    """Verifica contar_digito(9, 9)"""
    resultado = student.contar_digito(9, 9)
    assert resultado == 1

def test_contar_digito_varios():
    """Verifica contar_digito(111222333, 2)"""
    resultado = student.contar_digito(111222333, 2)
    assert resultado == 3

def test_salida_completa_5555():
    """Verifica salida completa con 5555, 5"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("5555\n5")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "El digito 5 aparece 4 veces en el numero 5555"

def test_salida_completa_no_existe():
    """Verifica salida completa cuando no existe"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("123456\n7")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "El digito 7 aparece 0 veces en el numero 123456"
