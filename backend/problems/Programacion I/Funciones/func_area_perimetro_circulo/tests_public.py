import importlib.util
import os
import math

spec = importlib.util.spec_from_file_location('student_code', os.path.join(os.getcwd(), 'student_code.py'))
student = importlib.util.module_from_spec(spec)
spec.loader.exec_module(student)

def test_existen_funciones():
    assert hasattr(student, 'calcular_area_circulo'), 'Debe existir calcular_area_circulo'
    assert hasattr(student, 'calcular_perimetro_circulo'), 'Debe existir calcular_perimetro_circulo'

def test_area_radio_5():
    area = student.calcular_area_circulo(5)
    esperado = math.pi * 25
    assert abs(area - esperado) < 0.01, f"❌ Área incorrecta para radio=5"

def test_perimetro_radio_5():
    perimetro = student.calcular_perimetro_circulo(5)
    esperado = 2 * math.pi * 5
    assert abs(perimetro - esperado) < 0.01, f"❌ Perímetro incorrecto para radio=5"
