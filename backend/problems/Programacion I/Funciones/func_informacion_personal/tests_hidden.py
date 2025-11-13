"""
Tests para: Func Informacion Personal
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

def test_cuatro_parametros():
    sig = inspect.signature(student.informacion_personal)
    assert len(sig.parameters) == 4, "❌ La función debe recibir 4 parámetros"

def test_formato_exacto():
    from io import StringIO
    import sys
    old_stdout = sys.stdout
    sys.stdout = StringIO()
    student.informacion_personal("Test", "User", 20, "Ciudad")
    output = sys.stdout.getvalue().strip()
    sys.stdout = old_stdout
    assert "Soy" in output and "tengo" in output and "años" in output and "vivo en" in output, "❌ Formato incorrecto"
