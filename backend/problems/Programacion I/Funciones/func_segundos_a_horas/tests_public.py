import importlib.util
import os

spec = importlib.util.spec_from_file_location('student_code', os.path.join(os.getcwd(), 'student_code.py'))
student = importlib.util.module_from_spec(spec)
spec.loader.exec_module(student)

def test_existe_funcion():
    assert hasattr(student, 'segundos_a_horas'), 'Debe existir la función segundos_a_horas'

def test_7200_segundos():
    resultado = student.segundos_a_horas(7200)
    assert resultado == 2.0, f"❌ 7200 segundos debe dar 2.0 horas, obtuvo: {resultado}"

def test_3600_segundos():
    resultado = student.segundos_a_horas(3600)
    assert resultado == 1.0, f"❌ 3600 segundos debe dar 1.0 hora, obtuvo: {resultado}"
