"""
Tests para: Func Tabla Multiplicar
Tema: Funciones

Este archivo contiene tests públicos que el estudiante puede ver.
Los tests verifican que la solución cumpla con todos los requisitos.
"""

import importlib.util
import os
from io import StringIO
import sys

spec = importlib.util.spec_from_file_location('student_code', os.path.join(os.getcwd(), 'student_code.py'))
student = importlib.util.module_from_spec(spec)
spec.loader.exec_module(student)

def test_tabla_del_7():
    captured_output = StringIO()
    sys.stdout = captured_output
    student.tabla_multiplicar(7)
    sys.stdout = sys.__stdout__
    
    output = captured_output.getvalue()
    assert "7 x 1 = 7" in output, "❌ Debe imprimir 7 x 1 = 7"
    assert "7 x 10 = 70" in output, "❌ Debe imprimir hasta 7 x 10 = 70"

def test_formato_correcto():
    captured_output = StringIO()
    sys.stdout = captured_output
    student.tabla_multiplicar(3)
    sys.stdout = sys.__stdout__
    
    output = captured_output.getvalue()
    assert "x" in output and "=" in output, "❌ El formato debe incluir 'x' y '='"
