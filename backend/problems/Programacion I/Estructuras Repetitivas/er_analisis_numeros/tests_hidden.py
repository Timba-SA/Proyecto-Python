"""
Tests para: Er Analisis Numeros
Tema: Estructuras Repetitivas

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

def test_solo_ceros():
    """Verifica análisis cuando todos son ceros"""
    old_stdout = sys.stdout
    old_stdin = sys.stdin
    
    # 100 ceros: todos pares, ninguno positivo ni negativo
    sys.stdin = StringIO('0\n' * 100)
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue()
    sys.stdout = old_stdout
    sys.stdin = old_stdin

    lineas = output.strip().split('\n')
    # Pares: 100, Impares: 0, Negativos: 0, Positivos: 0
    assert lineas[0].strip() == '100', f"Todos los ceros son pares, debe ser 100, se obtuvo {lineas[0]}"
    assert lineas[1].strip() == '0', f"No hay impares, debe ser 0, se obtuvo {lineas[1]}"
    assert lineas[2].strip() == '0', f"No hay negativos, debe ser 0, se obtuvo {lineas[2]}"
    assert lineas[3].strip() == '0', f"No hay positivos, debe ser 0, se obtuvo {lineas[3]}"
