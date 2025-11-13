"""
Tests para: Func Calcular Imc
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
    assert hasattr(student, 'calcular_imc'), 'Debe existir la función calcular_imc'

def test_imc_70_175():
    resultado = student.calcular_imc(70, 1.75)
    esperado = 22.86
    assert abs(resultado - esperado) < 0.01, f"❌ Con peso=70 y altura=1.75 esperado {esperado}, obtuvo: {resultado}"
