import importlib.util
import os
from io import StringIO
import sys

spec = importlib.util.spec_from_file_location('student_code', os.path.join(os.getcwd(), 'student_code.py'))
student = importlib.util.module_from_spec(spec)
spec.loader.exec_module(student)

def test_existe_funcion():
    """Verifica que existe la función imprimir_hola_mundo"""
    assert hasattr(student, 'imprimir_hola_mundo'), 'Debe existir la función imprimir_hola_mundo'
    assert callable(student.imprimir_hola_mundo), 'imprimir_hola_mundo debe ser una función'

def test_salida_correcta():
    """Verifica que la función imprime el mensaje correcto"""
    old_stdout = sys.stdout
    sys.stdout = StringIO()
    
    student.imprimir_hola_mundo()
    
    output = sys.stdout.getvalue().strip()
    sys.stdout = old_stdout
    
    assert output == "Hola Mundo!", f"❌ Se esperaba 'Hola Mundo!', se obtuvo '{output}'"
