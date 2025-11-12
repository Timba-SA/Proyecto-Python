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

def test_diccionario_inicial():
    """Verifica que contiene las frutas iniciales"""
    old_stdout = sys.stdout
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdout = old_stdout

    assert 'Banana' in output and '1200' in output, "Debe contener Banana con precio 1200"
    assert 'Ananá' in output and '2500' in output, "Debe contener Ananá con precio 2500"

def test_frutas_agregadas():
    """Verifica que se agregaron las tres frutas nuevas"""
    old_stdout = sys.stdout
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdout = old_stdout

    assert 'Naranja' in output, f"""❌ Falta agregar Naranja
   💡 Pista: Usa precios_frutas['Naranja'] = 1200"""
    
    assert 'Manzana' in output, f"""❌ Falta agregar Manzana
   💡 Pista: Usa precios_frutas['Manzana'] = 1500"""
    
    assert 'Pera' in output, f"""❌ Falta agregar Pera
   💡 Pista: Usa precios_frutas['Pera'] = 2300"""
