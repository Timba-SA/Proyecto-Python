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

def test_existe_funcion():
    assert hasattr(student, 'celsius_a_fahrenheit'), 'Debe existir la función celsius_a_fahrenheit'

def test_cero_grados():
    resultado = student.celsius_a_fahrenheit(0)
    assert resultado == 32.0, f"❌ 0°C debe ser 32°F, obtuvo: {resultado}"

def test_100_grados():
    resultado = student.celsius_a_fahrenheit(100)
    assert resultado == 212.0, f"❌ 100°C debe ser 212°F, obtuvo: {resultado}"
