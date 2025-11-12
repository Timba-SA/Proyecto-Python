import importlib.util
import os

spec = importlib.util.spec_from_file_location('student_code', os.path.join(os.getcwd(), 'student_code.py'))
student = importlib.util.module_from_spec(spec)
spec.loader.exec_module(student)

def test_1800_segundos():
    resultado = student.segundos_a_horas(1800)
    assert resultado == 0.5, f"❌ 1800 segundos debe dar 0.5 horas, obtuvo: {resultado}"

def test_devuelve_numero():
    resultado = student.segundos_a_horas(3600)
    assert isinstance(resultado, (int, float)), "❌ La función debe devolver un número"
