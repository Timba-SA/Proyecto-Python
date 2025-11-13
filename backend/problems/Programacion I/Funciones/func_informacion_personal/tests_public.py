"""
Tests para: Func Informacion Personal
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

def test_existe_funcion():
    assert hasattr(student, 'informacion_personal'), 'Debe existir la función informacion_personal'

def test_salida_correcta():
    old_stdout = sys.stdout
    sys.stdout = StringIO()
    student.informacion_personal("Juan", "Pérez", 25, "Buenos Aires")
    output = sys.stdout.getvalue().strip()
    sys.stdout = old_stdout
    assert output == "Soy Juan Pérez, tengo 25 años y vivo en Buenos Aires", f"❌ Salida incorrecta: '{output}'"

def test_otro_caso():
    old_stdout = sys.stdout
    sys.stdout = StringIO()
    student.informacion_personal("Ana", "García", 30, "Córdoba")
    output = sys.stdout.getvalue().strip()
    sys.stdout = old_stdout
    assert output == "Soy Ana García, tengo 30 años y vivo en Córdoba", f"❌ Salida incorrecta: '{output}'"
