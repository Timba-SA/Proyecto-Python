"""
Tests para: Func Celsius A Fahrenheit
Tema: Funciones

Este archivo contiene tests públicos que el estudiante puede ver.
Los tests verifican que la solución cumpla con todos los requisitos.
"""

import importlib.util
import os

spec = importlib.util.spec_from_file_location('student_code', os.path.join(os.getcwd(), 'student_code.py'))
student = importlib.util.module_from_spec(spec)
spec.loader.exec_module(student)

def test_25_grados():
    resultado = student.celsius_a_fahrenheit(25)
    assert resultado == 77.0, f"❌ 25°C debe ser 77°F, obtuvo: {resultado}"

def test_devuelve_numero():
    resultado = student.celsius_a_fahrenheit(0)
    assert isinstance(resultado, (int, float)), "❌ La función debe devolver un número"
