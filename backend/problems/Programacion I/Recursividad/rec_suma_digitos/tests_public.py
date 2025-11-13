"""
Tests para: Rec Suma Digitos
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

def test_existe_funcion_suma_digitos():
    """Verifica que existe la función suma_digitos"""
    assert hasattr(student, 'suma_digitos'), 'Debe existir la función suma_digitos'

def test_suma_digitos_es_recursiva():
    """Verifica que la función es recursiva"""
    source = inspect.getsource(student.suma_digitos)
    assert 'suma_digitos(' in source and 'def suma_digitos' in source, """❌ La función debe ser recursiva
    💡 Pista: Debe llamarse a sí misma"""
    assert 'str(' not in source and 'while' not in source and 'for' not in source, """❌ No debe usar str(), while ni for
    💡 Pista: Usa solo operaciones matemáticas: %, //, +"""

def test_suma_digitos_0():
    """Verifica suma de dígitos de 0"""
    resultado = student.suma_digitos(0)
    assert resultado == 0, f"""❌ suma_digitos(0) debería ser 0, se obtuvo {resultado}"""

def test_suma_digitos_9():
    """Verifica suma de dígitos de 9"""
    resultado = student.suma_digitos(9)
    assert resultado == 9, f"""❌ suma_digitos(9) debería ser 9, se obtuvo {resultado}"""

def test_suma_digitos_1234():
    """Verifica suma de dígitos de 1234"""
    resultado = student.suma_digitos(1234)
    assert resultado == 10, f"""❌ suma_digitos(1234) debería ser 10, se obtuvo {resultado}
    💡 Pista: 1 + 2 + 3 + 4 = 10"""

def test_suma_digitos_305():
    """Verifica suma de dígitos de 305"""
    resultado = student.suma_digitos(305)
    assert resultado == 8, f"""❌ suma_digitos(305) debería ser 8, se obtuvo {resultado}
    💡 Pista: 3 + 0 + 5 = 8"""

def test_salida_completa():
    """Verifica salida completa con n=1234"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("1234")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "La suma de los digitos de 1234 es 10", f"""❌ Formato incorrecto
    Se esperaba: 'La suma de los digitos de 1234 es 10'
    Se obtuvo: '{output}'"""
