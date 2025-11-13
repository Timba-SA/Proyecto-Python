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

def test_imc_85_180():
    resultado = student.calcular_imc(85, 1.80)
    esperado = 26.23
    assert abs(resultado - esperado) < 0.01, f"❌ Con peso=85 y altura=1.80 esperado {esperado}, obtuvo: {resultado}"

def test_redondeo_correcto():
    resultado = student.calcular_imc(70, 1.75)
    # Verificar que tiene máximo 2 decimales
    resultado_str = str(resultado)
    if '.' in resultado_str:
        decimales = len(resultado_str.split('.')[1])
        assert decimales <= 2, f"❌ El resultado debe tener máximo 2 decimales, tiene {decimales}"
