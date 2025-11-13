"""
Tests para: Rec Contar Digito
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

def test_existe_funcion_contar_digito():
    """Verifica que existe la función contar_digito"""
    assert hasattr(student, 'contar_digito'), 'Debe existir la función contar_digito'

def test_contar_digito_es_recursiva():
    """Verifica que la función es recursiva"""
    source = inspect.getsource(student.contar_digito)
    assert 'contar_digito(' in source and 'def contar_digito' in source, """❌ La función debe ser recursiva
    💡 Pista: Debe llamarse a sí misma"""
    assert 'str(' not in source and 'count(' not in source, """❌ No debe usar str() ni count()
    💡 Pista: Usa solo operaciones matemáticas"""
    assert 'while' not in source and 'for' not in source, """❌ No debe usar while ni for
    💡 Pista: Solo recursión"""

def test_contar_digito_basico():
    """Verifica contar_digito(12233421, 2)"""
    resultado = student.contar_digito(12233421, 2)
    assert resultado == 3, f"""❌ contar_digito(12233421, 2) debería ser 3, se obtuvo {resultado}
    💡 Pista: En 12233421, el 2 aparece 3 veces"""

def test_contar_digito_repetido():
    """Verifica contar_digito(5555, 5)"""
    resultado = student.contar_digito(5555, 5)
    assert resultado == 4, f"""❌ contar_digito(5555, 5) debería ser 4, se obtuvo {resultado}"""

def test_contar_digito_no_existe():
    """Verifica contar_digito(123456, 7)"""
    resultado = student.contar_digito(123456, 7)
    assert resultado == 0, f"""❌ contar_digito(123456, 7) debería ser 0, se obtuvo {resultado}"""

def test_contar_digito_ceros():
    """Verifica contar_digito(100200, 0)"""
    resultado = student.contar_digito(100200, 0)
    assert resultado == 4, f"""❌ contar_digito(100200, 0) debería ser 4, se obtuvo {resultado}
    💡 Pista: En 100200 hay cuatro ceros"""

def test_salida_completa():
    """Verifica salida completa"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("12233421\n2")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "El digito 2 aparece 3 veces en el numero 12233421", f"""❌ Formato incorrecto
    Se esperaba: 'El digito 2 aparece 3 veces en el numero 12233421'
    Se obtuvo: '{output}'"""
