"""
Tests para: Edc Actualizar Precios
Tema: Estructuras de datos complejas

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
    """Verifica que existe la función main"""
    assert hasattr(student, 'main'), 'Debe existir la función main'

def test_precios_actualizados():
    """Verifica que los precios fueron actualizados correctamente"""
    old_stdout = sys.stdout
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdout = old_stdout

    assert "'Banana': 1330" in output or '"Banana": 1330' in output, "Banana debe tener precio 1330"
    assert "'Manzana': 1700" in output or '"Manzana": 1700' in output, "Manzana debe tener precio 1700"
    assert "'Melón': 2800" in output or '"Melón": 2800' in output, "Melón debe tener precio 2800"
