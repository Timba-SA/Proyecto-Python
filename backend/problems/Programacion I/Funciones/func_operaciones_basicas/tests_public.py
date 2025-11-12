import importlib.util
import os

spec = importlib.util.spec_from_file_location('student_code', os.path.join(os.getcwd(), 'student_code.py'))
student = importlib.util.module_from_spec(spec)
spec.loader.exec_module(student)

def test_existe_funcion():
    assert hasattr(student, 'operaciones_basicas'), 'Debe existir la función operaciones_basicas'

def test_operaciones_10_2():
    resultado = student.operaciones_basicas(10, 2)
    assert resultado == (12, 8, 20, 5.0), f"❌ Con a=10 y b=2 esperado (12, 8, 20, 5.0), obtuvo: {resultado}"

def test_devuelve_tupla():
    resultado = student.operaciones_basicas(10, 2)
    assert isinstance(resultado, tuple), "❌ La función debe devolver una tupla"
    assert len(resultado) == 4, "❌ La tupla debe tener 4 elementos"
