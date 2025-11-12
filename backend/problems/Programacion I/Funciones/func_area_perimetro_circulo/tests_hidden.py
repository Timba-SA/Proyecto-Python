import importlib.util
import os
import math

spec = importlib.util.spec_from_file_location('student_code', os.path.join(os.getcwd(), 'student_code.py'))
student = importlib.util.module_from_spec(spec)
spec.loader.exec_module(student)

def test_area_radio_10():
    area = student.calcular_area_circulo(10)
    esperado = math.pi * 100
    assert abs(area - esperado) < 0.01, f"❌ Área incorrecta para radio=10"

def test_perimetro_radio_10():
    perimetro = student.calcular_perimetro_circulo(10)
    esperado = 2 * math.pi * 10
    assert abs(perimetro - esperado) < 0.01, f"❌ Perímetro incorrecto para radio=10"

def test_funciones_devuelven_numero():
    area = student.calcular_area_circulo(5)
    perimetro = student.calcular_perimetro_circulo(5)
    assert isinstance(area, (int, float)), "❌ El área debe ser un número"
    assert isinstance(perimetro, (int, float)), "❌ El perímetro debe ser un número"
