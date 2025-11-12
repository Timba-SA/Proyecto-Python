import importlib.util
import os
from io import StringIO
import sys

spec = importlib.util.spec_from_file_location('student_code', os.path.join(os.getcwd(), 'student_code.py'))
student = importlib.util.module_from_spec(spec)
spec.loader.exec_module(student)

def test_palindromo_reconocer():
    """Verifica que 'reconocer' es palíndromo"""
    resultado = student.es_palindromo("reconocer")
    assert resultado == True

def test_palindromo_anilina():
    """Verifica que 'anilina' es palíndromo"""
    resultado = student.es_palindromo("anilina")
    assert resultado == True

def test_palindromo_un_caracter():
    """Verifica que un solo carácter es palíndromo"""
    resultado = student.es_palindromo("a")
    assert resultado == True

def test_no_palindromo_python():
    """Verifica que 'python' NO es palíndromo"""
    resultado = student.es_palindromo("python")
    assert resultado == False

def test_salida_mayusculas():
    """Verifica que maneja mayúsculas correctamente"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("Reconocer")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "La palabra reconocer es un palindromo"
