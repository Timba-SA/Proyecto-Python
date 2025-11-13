"""
Tests para: Edc Agregar Frutas
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

def test_precios_correctos():
    """Verifica que los precios de las frutas nuevas sean correctos"""
    old_stdout = sys.stdout
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdout = old_stdout

    # Verificar que los precios están en el output
    assert "'Naranja': 1200" in output or '"Naranja": 1200' in output, "Naranja debe tener precio 1200"
    assert "'Manzana': 1500" in output or '"Manzana": 1500' in output, "Manzana debe tener precio 1500"
    assert "'Pera': 2300" in output or '"Pera": 2300' in output, "Pera debe tener precio 2300"
