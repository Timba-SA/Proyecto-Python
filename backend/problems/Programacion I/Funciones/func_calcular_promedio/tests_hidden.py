import importlib.util
import os

spec = importlib.util.spec_from_file_location('student_code', os.path.join(os.getcwd(), 'student_code.py'))
student = importlib.util.module_from_spec(spec)
spec.loader.exec_module(student)

def test_promedio_10_10_10():
    resultado = student.calcular_promedio(10, 10, 10)
    assert abs(resultado - 10.0) < 0.01, f"❌ Promedio de 10, 10, 10 debe ser 10.0, obtuvo: {resultado}"

def test_devuelve_numero():
    resultado = student.calcular_promedio(5, 7, 9)
    assert isinstance(resultado, (int, float)), "❌ La función debe devolver un número"
