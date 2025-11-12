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

def test_existe_funcion_decimal_a_binario():
    """Verifica que existe la función decimal_a_binario"""
    assert hasattr(student, 'decimal_a_binario'), 'Debe existir la función decimal_a_binario'

def test_decimal_a_binario_es_recursiva():
    """Verifica que la función es recursiva"""
    source = inspect.getsource(student.decimal_a_binario)
    assert 'decimal_a_binario(' in source and 'def decimal_a_binario' in source, """❌ La función debe ser recursiva
    💡 Pista: Debe llamarse a sí misma con decimal_a_binario(n // 2)"""
    assert 'bin(' not in source and 'while' not in source and 'for' not in source, """❌ No debe usar bin(), while ni for
    💡 Pista: Usa solo recursión y operadores // y %"""

def test_decimal_a_binario_1():
    """Verifica conversión de 1"""
    resultado = student.decimal_a_binario(1)
    assert resultado == "1", f"""❌ decimal_a_binario(1) debería ser '1', se obtuvo '{resultado}'"""

def test_decimal_a_binario_5():
    """Verifica conversión de 5"""
    resultado = student.decimal_a_binario(5)
    assert resultado == "101", f"""❌ decimal_a_binario(5) debería ser '101', se obtuvo '{resultado}'
    💡 Pista: 5 ÷ 2 = 2 resto 1, 2 ÷ 2 = 1 resto 0, 1 ÷ 2 = 0 resto 1 → 101"""

def test_decimal_a_binario_10():
    """Verifica conversión de 10"""
    resultado = student.decimal_a_binario(10)
    assert resultado == "1010", f"""❌ decimal_a_binario(10) debería ser '1010', se obtuvo '{resultado}'"""

def test_salida_completa_10():
    """Verifica salida completa con n=10"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("10")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "La representación binaria de 10 es 1010", f"""❌ Formato incorrecto
    Se esperaba: 'La representación binaria de 10 es 1010'
    Se obtuvo: '{output}'"""
