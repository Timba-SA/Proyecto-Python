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

def test_existe_funcion_contar_bloques():
    """Verifica que existe la función contar_bloques"""
    assert hasattr(student, 'contar_bloques'), 'Debe existir la función contar_bloques'

def test_contar_bloques_es_recursiva():
    """Verifica que la función es recursiva"""
    source = inspect.getsource(student.contar_bloques)
    assert 'contar_bloques(' in source and 'def contar_bloques' in source, """❌ La función debe ser recursiva
    💡 Pista: Debe llamarse a sí misma"""
    assert '*' not in source or 'contar_bloques' in source.split('*')[0], """❌ No debe usar la fórmula n*(n+1)/2
    💡 Pista: Usa recursión: n + contar_bloques(n-1)"""
    assert 'sum(' not in source and 'while' not in source and 'for' not in source, """❌ No debe usar sum(), while ni for
    💡 Pista: Solo recursión"""

def test_contar_bloques_1():
    """Verifica contar_bloques(1)"""
    resultado = student.contar_bloques(1)
    assert resultado == 1, f"""❌ contar_bloques(1) debería ser 1, se obtuvo {resultado}"""

def test_contar_bloques_2():
    """Verifica contar_bloques(2)"""
    resultado = student.contar_bloques(2)
    assert resultado == 3, f"""❌ contar_bloques(2) debería ser 3, se obtuvo {resultado}
    💡 Pista: 2 + 1 = 3"""

def test_contar_bloques_4():
    """Verifica contar_bloques(4)"""
    resultado = student.contar_bloques(4)
    assert resultado == 10, f"""❌ contar_bloques(4) debería ser 10, se obtuvo {resultado}
    💡 Pista: 4 + 3 + 2 + 1 = 10"""

def test_salida_completa():
    """Verifica salida completa con n=4"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("4")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "Para una piramide de 4 niveles se necesitan 10 bloques", f"""❌ Formato incorrecto
    Se esperaba: 'Para una piramide de 4 niveles se necesitan 10 bloques'
    Se obtuvo: '{output}'"""
