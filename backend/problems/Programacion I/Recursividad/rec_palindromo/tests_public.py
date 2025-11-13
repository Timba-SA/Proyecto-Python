"""
Tests para: Rec Palindromo
Tema: Recursividad

Este archivo contiene tests públicos que el estudiante puede ver.
Los tests verifican que la solución cumpla con todos los requisitos.
"""

import importlib.util
import os
from io import StringIO
import sys
import inspect

spec = importlib.util.spec_from_file_location('student_code', os.path.join(os.getcwd(), 'student_code.py'))
student = importlib.util.module_from_spec(spec)
spec.loader.exec_module(student)

def test_existe_funcion():
    """Verifica que existe la función main"""
    assert hasattr(student, 'main'), 'Debe existir la función main'

def test_existe_funcion_es_palindromo():
    """Verifica que existe la función es_palindromo"""
    assert hasattr(student, 'es_palindromo'), 'Debe existir la función es_palindromo'

def test_es_palindromo_recursiva():
    """Verifica que la función es recursiva"""
    source = inspect.getsource(student.es_palindromo)
    assert 'es_palindromo(' in source and 'def es_palindromo' in source, """❌ La función debe ser recursiva
    💡 Pista: Debe llamarse a sí misma"""
    assert '[::-1]' not in source and 'reversed(' not in source, """❌ No debe usar [::-1] ni reversed()
    💡 Pista: Compara primer y último carácter, luego llama recursivamente"""

def test_palindromo_oso():
    """Verifica que 'oso' es palíndromo"""
    resultado = student.es_palindromo("oso")
    assert resultado == True, f"""❌ es_palindromo('oso') debería ser True, se obtuvo {resultado}"""

def test_palindromo_neuquen():
    """Verifica que 'neuquen' es palíndromo"""
    resultado = student.es_palindromo("neuquen")
    assert resultado == True, f"""❌ es_palindromo('neuquen') debería ser True, se obtuvo {resultado}"""

def test_no_palindromo_hola():
    """Verifica que 'hola' NO es palíndromo"""
    resultado = student.es_palindromo("hola")
    assert resultado == False, f"""❌ es_palindromo('hola') debería ser False, se obtuvo {resultado}"""

def test_salida_completa_palindromo():
    """Verifica salida completa con palíndromo"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("neuquen")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "La palabra neuquen es un palindromo", f"""❌ Formato incorrecto
    Se esperaba: 'La palabra neuquen es un palindromo'
    Se obtuvo: '{output}'"""

def test_salida_completa_no_palindromo():
    """Verifica salida completa con NO palíndromo"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("hola")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "La palabra hola no es un palindromo", f"""❌ Formato incorrecto
    Se esperaba: 'La palabra hola no es un palindromo'
    Se obtuvo: '{output}'"""
