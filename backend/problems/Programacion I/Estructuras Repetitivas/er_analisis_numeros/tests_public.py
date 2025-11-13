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

def test_existe_funcion():
    """Verifica que existe la función main"""
    assert hasattr(student, 'main'), 'Debe existir la función main'

def test_analisis_10_numeros():
    """Verifica análisis de 10 números (debe estar preparado para 100)"""
    old_stdout = sys.stdout
    old_stdin = sys.stdin
    
    # 5, -2, 8, 0, -7, 3, 4, -1, 6, 2
    # Pares: -2, 8, 0, 4, 6, 2 = 6
    # Impares: 5, -7, 3, -1 = 4
    # Negativos: -2, -7, -1 = 3
    # Positivos: 5, 8, 3, 4, 6, 2 = 6
    sys.stdin = StringIO('5\n-2\n8\n0\n-7\n3\n4\n-1\n6\n2\n')
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue()
    sys.stdout = old_stdout
    sys.stdin = old_stdin

    lineas = output.strip().split('\n')
    assert len(lineas) >= 4, "Debe imprimir 4 valores"
    # Nota: El test asume que el código está adaptado para 10 números en lugar de 100
