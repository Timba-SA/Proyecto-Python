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

def test_existe_funcion_potencia():
    """Verifica que existe la función potencia"""
    assert hasattr(student, 'potencia'), 'Debe existir la función potencia'

def test_potencia_es_recursiva():
    """Verifica que la función potencia es recursiva"""
    source = inspect.getsource(student.potencia)
    assert 'potencia(' in source and 'def potencia' in source, """❌ La función potencia debe ser recursiva
    💡 Pista: Una función recursiva se llama a sí misma"""
    assert '**' not in source and 'pow(' not in source, """❌ No debe usar el operador ** ni pow()
    💡 Pista: Usa multiplicación recursiva"""

def test_potencia_caso_base():
    """Verifica el caso base (exponente 0)"""
    resultado = student.potencia(5, 0)
    assert resultado == 1, f"""❌ potencia(5, 0) debería ser 1, se obtuvo {resultado}
    💡 Pista: Cualquier número elevado a 0 es 1"""

def test_potencia_2_3():
    """Verifica 2 elevado a 3"""
    resultado = student.potencia(2, 3)
    assert resultado == 8, f"""❌ potencia(2, 3) debería ser 8, se obtuvo {resultado}
    💡 Pista: 2^3 = 2 × 2 × 2 = 8"""

def test_potencia_3_4():
    """Verifica 3 elevado a 4"""
    resultado = student.potencia(3, 4)
    assert resultado == 81, f"""❌ potencia(3, 4) debería ser 81, se obtuvo {resultado}
    💡 Pista: 3^4 = 3 × 3 × 3 × 3 = 81"""

def test_salida_completa():
    """Verifica salida completa con base=2, exponente=3"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("2\n3")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "El resultado de 2 elevado a 3 es 8", f"""❌ Se esperaba 'El resultado de 2 elevado a 3 es 8'
    Se obtuvo: '{output}'"""
