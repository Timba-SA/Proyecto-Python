"""
Tests para: Func Operaciones Basicas
Tema: Funciones

Este archivo contiene tests públicos que el estudiante puede ver.
Los tests verifican que la solución cumpla con todos los requisitos.
"""

import importlib.util
import os

spec = importlib.util.spec_from_file_location('student_code', os.path.join(os.getcwd(), 'student_code.py'))
student = importlib.util.module_from_spec(spec)
spec.loader.exec_module(student)

def test_operaciones_20_4():
    resultado = student.operaciones_basicas(20, 4)
    assert resultado == (24, 16, 80, 5.0), f"❌ Con a=20 y b=4 esperado (24, 16, 80, 5.0), obtuvo: {resultado}"

def test_orden_correcto():
    resultado = student.operaciones_basicas(10, 2)
    assert resultado[0] == 12, "❌ El primer elemento debe ser la suma"
    assert resultado[1] == 8, "❌ El segundo elemento debe ser la resta"
    assert resultado[2] == 20, "❌ El tercer elemento debe ser la multiplicación"
    assert resultado[3] == 5.0, "❌ El cuarto elemento debe ser la división"
