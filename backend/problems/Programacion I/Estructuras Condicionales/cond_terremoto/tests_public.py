"""
Tests para: Cond Terremoto
Tema: Estructuras Condicionales

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

def test_muy_leve():
    """Verifica clasificación Muy leve (magnitud < 3)"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("2.5")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "Muy leve", f"""❌ Clasificación incorrecta
   Para magnitud=2.5: se esperaba 'Muy leve', se obtuvo '{output}'
   💡 Pista: Si magnitud < 3, es 'Muy leve'"""

def test_leve():
    """Verifica clasificación Leve (3 ≤ magnitud < 4)"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("3.7")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "Leve", f"""❌ Clasificación incorrecta
   Para magnitud=3.7: se esperaba 'Leve', se obtuvo '{output}'
   💡 Pista: Si 3 ≤ magnitud < 4, es 'Leve'"""

def test_moderado():
    """Verifica clasificación Moderado (4 ≤ magnitud < 5)"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("4.8")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "Moderado", f"""❌ Clasificación incorrecta
   Para magnitud=4.8: se esperaba 'Moderado', se obtuvo '{output}'
   💡 Pista: Si 4 ≤ magnitud < 5, es 'Moderado'"""

def test_fuerte():
    """Verifica clasificación Fuerte (5 ≤ magnitud < 6)"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("5.5")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "Fuerte", f"""❌ Clasificación incorrecta
   Para magnitud=5.5: se esperaba 'Fuerte', se obtuvo '{output}'
   💡 Pista: Si 5 ≤ magnitud < 6, es 'Fuerte'"""

def test_muy_fuerte():
    """Verifica clasificación Muy Fuerte (6 ≤ magnitud < 7)"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("6.3")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "Muy Fuerte", f"""❌ Clasificación incorrecta
   Para magnitud=6.3: se esperaba 'Muy Fuerte', se obtuvo '{output}'
   💡 Pista: Si 6 ≤ magnitud < 7, es 'Muy Fuerte'"""

def test_extremo():
    """Verifica clasificación Extremo (magnitud ≥ 7)"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("8.0")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "Extremo", f"""❌ Clasificación incorrecta
   Para magnitud=8.0: se esperaba 'Extremo', se obtuvo '{output}'
   💡 Pista: Si magnitud ≥ 7, es 'Extremo' (ej: terremoto de Chile 2010 fue 8.8)"""
