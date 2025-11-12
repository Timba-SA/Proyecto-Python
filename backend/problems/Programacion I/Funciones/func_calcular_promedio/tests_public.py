import importlib.util
import os

spec = importlib.util.spec_from_file_location('student_code', os.path.join(os.getcwd(), 'student_code.py'))
student = importlib.util.module_from_spec(spec)
spec.loader.exec_module(student)

def test_existe_funcion():
    assert hasattr(student, 'calcular_promedio'), 'Debe existir la función calcular_promedio'

def test_promedio_8_9_10():
    resultado = student.calcular_promedio(8, 9, 10)
    assert abs(resultado - 9.0) < 0.01, f"❌ Promedio de 8, 9, 10 debe ser 9.0, obtuvo: {resultado}"

def test_promedio_5_7_9():
    resultado = student.calcular_promedio(5, 7, 9)
    assert abs(resultado - 7.0) < 0.01, f"❌ Promedio de 5, 7, 9 debe ser 7.0, obtuvo: {resultado}"
