import importlib.util
import os
import sys

spec = importlib.util.spec_from_file_location('student_code', os.path.join(os.getcwd(), 'student_code.py'))
student = importlib.util.module_from_spec(spec)
spec.loader.exec_module(student)

def test_existe_funcion():
    assert hasattr(student, 'saludar_usuario'), 'Debe existir la función saludar_usuario'
    assert callable(student.saludar_usuario), 'saludar_usuario debe ser una función'

def test_saludo_marcos():
    resultado = student.saludar_usuario("Marcos")
    assert resultado == "Hola Marcos!", f"❌ Para 'Marcos': esperaba 'Hola Marcos!', obtuve '{resultado}'"

def test_saludo_ana():
    resultado = student.saludar_usuario("Ana")
    assert resultado == "Hola Ana!", f"❌ Para 'Ana': esperaba 'Hola Ana!', obtuve '{resultado}'"
