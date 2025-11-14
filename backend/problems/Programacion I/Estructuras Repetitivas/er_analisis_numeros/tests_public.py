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

def test_analisis_100_numeros():
    """Verifica análisis de 100 números"""
    old_stdout = sys.stdout
    old_stdin = sys.stdin
    
    # Crear 100 números: 25 pares positivos, 25 impares positivos, 25 pares negativos, 25 impares negativos
    numeros = []
    # 25 pares positivos (2, 4, 6, ..., 50)
    numeros.extend([str(i) for i in range(2, 52, 2)])
    # 25 impares positivos (1, 3, 5, ..., 49)
    numeros.extend([str(i) for i in range(1, 50, 2)])
    # 25 pares negativos (-2, -4, -6, ..., -50)
    numeros.extend([str(-i) for i in range(2, 52, 2)])
    # 25 impares negativos (-1, -3, -5, ..., -49)
    numeros.extend([str(-i) for i in range(1, 50, 2)])
    
    sys.stdin = StringIO('\n'.join(numeros) + '\n')
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue()
    sys.stdout = old_stdout
    sys.stdin = old_stdin

    lineas = output.strip().split('\n')
    assert len(lineas) >= 4, "Debe imprimir 4 valores"
    # Pares: 50, Impares: 50, Negativos: 50, Positivos: 50
    assert lineas[0].strip() == '50', f"Cantidad de pares debe ser 50, se obtuvo {lineas[0]}"
    assert lineas[1].strip() == '50', f"Cantidad de impares debe ser 50, se obtuvo {lineas[1]}"
    assert lineas[2].strip() == '50', f"Cantidad de negativos debe ser 50, se obtuvo {lineas[2]}"
    assert lineas[3].strip() == '50', f"Cantidad de positivos debe ser 50, se obtuvo {lineas[3]}"
