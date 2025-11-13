"""
Tests para: Sec Tabla Multiplicar
Tema: Estructuras Secuenciales

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
    """Test tabla del 7"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("7")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    lines = output.split('\n')
    assert len(lines) == 10, f"Debe imprimir exactamente 10 líneas (del 1 al 10), se obtuvieron {len(lines)}"
    
    expected = [
        "7 x 1 = 7",
        "7 x 2 = 14",
        "7 x 3 = 21",
        "7 x 4 = 28",
        "7 x 5 = 35",
        "7 x 6 = 42",
        "7 x 7 = 49",
        "7 x 8 = 56",
        "7 x 9 = 63",
        "7 x 10 = 70"
    ]
    
    for i, (expected_line, actual_line) in enumerate(zip(expected, lines), 1):
        assert actual_line == expected_line, f"Línea {i} incorrecta. Esperado: '{expected_line}', Obtenido: '{actual_line}'"

def test_tabla_negativa():
    """Test tabla de número negativo (-3)"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("-3")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    lines = output.split('\n')
    assert len(lines) == 10, f"Debe imprimir exactamente 10 líneas (del 1 al 10), se obtuvieron {len(lines)}"
    
    expected = [
        "-3 x 1 = -3",
        "-3 x 2 = -6",
        "-3 x 3 = -9",
        "-3 x 4 = -12",
        "-3 x 5 = -15",
        "-3 x 6 = -18",
        "-3 x 7 = -21",
        "-3 x 8 = -24",
        "-3 x 9 = -27",
        "-3 x 10 = -30"
    ]
    
    for i, (expected_line, actual_line) in enumerate(zip(expected, lines), 1):
        assert actual_line == expected_line, f"Línea {i} incorrecta. Esperado: '{expected_line}', Obtenido: '{actual_line}'"

def test_formato_exacto():
    """Verifica que el formato sea exactamente '{n} x {i} = {resultado}' (con espacios)"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("3")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    lines = output.split('\n')
    
    # Verificar que cada línea contenga ' x ' y ' = '
    for i, line in enumerate(lines, 1):
        assert ' x ' in line, f"Línea {i} debe contener ' x ' (x minúscula con espacios): '{line}'"
        assert ' = ' in line, f"Línea {i} debe contener ' = ' (igual con espacios): '{line}'"
        
        # Verificar formato exacto para la primera línea
        if i == 1:
            assert line == "3 x 1 = 3", f"Formato incorrecto. Debe ser '3 x 1 = 3', se obtuvo '{line}'"

