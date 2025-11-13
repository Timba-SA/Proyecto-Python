"""
Tests para: Func Saludar Usuario
Tema: Funciones

Este archivo contiene tests públicos que el estudiante puede ver.
Los tests verifican que la solución cumpla con todos los requisitos.
"""

import importlib.util
import os
import inspect

spec = importlib.util.spec_from_file_location('student_code', os.path.join(os.getcwd(), 'student_code.py'))
student = importlib.util.module_from_spec(spec)
spec.loader.exec_module(student)

def test_devuelve_string():
    resultado = student.saludar_usuario("Test")
    assert isinstance(resultado, str), "❌ La función debe devolver un string"

def test_formato_correcto():
    resultado = student.saludar_usuario("Pedro")
    assert resultado.startswith("Hola "), "❌ El saludo debe comenzar con 'Hola '"
    assert resultado.endswith("!"), "❌ El saludo debe terminar con '!'"

def test_un_parametro():
    sig = inspect.signature(student.saludar_usuario)
    assert len(sig.parameters) == 1, "❌ La función debe recibir exactamente 1 parámetro"
