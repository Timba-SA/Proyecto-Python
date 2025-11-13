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

def test_limite_muy_leve_leve_inferior():
    """Verifica límite entre Muy leve y Leve (2.9)"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("2.9")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "Muy leve", f"""❌ Error en límite inferior
   Para magnitud=2.9: se esperaba 'Muy leve', se obtuvo '{output}'
   💡 Pista: 2.9 < 3, por lo tanto es 'Muy leve'"""

def test_limite_muy_leve_leve_superior():
    """Verifica límite entre Muy leve y Leve (3.0)"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("3.0")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "Leve", f"""❌ Error en caso límite
   Para magnitud=3.0 (exacto): se esperaba 'Leve', se obtuvo '{output}'
   💡 Pista: 3.0 >= 3 y 3.0 < 4, por lo tanto es 'Leve'"""

def test_limite_fuerte_muy_fuerte_superior():
    """Verifica límite entre Fuerte y Muy Fuerte (6.0)"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("6.0")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "Muy Fuerte", f"Se esperaba 'Muy Fuerte', se obtuvo '{output}'"

def test_limite_muy_fuerte_extremo_inferior():
    """Verifica límite entre Muy Fuerte y Extremo (6.99)"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("6.99")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "Muy Fuerte", f"""❌ Error en límite superior
   Para magnitud=6.99: se esperaba 'Muy Fuerte', se obtuvo '{output}'
   💡 Pista: 6.99 < 7, por lo tanto todavía es 'Muy Fuerte'"""

def test_limite_muy_fuerte_extremo_superior():
    """Verifica límite entre Muy Fuerte y Extremo (7.0)"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("7.0")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "Extremo", f"""❌ Error en caso límite crítico
   Para magnitud=7.0 (exacto): se esperaba 'Extremo', se obtuvo '{output}'
   💡 Pista: 7.0 >= 7, por lo tanto es 'Extremo'"""

def test_magnitud_muy_alta():
    """Verifica magnitud muy alta (9.5)"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("9.5")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "Extremo", f"""❌ Error con magnitud muy alta
   Para magnitud=9.5: se esperaba 'Extremo', se obtuvo '{output}'
   💡 Pista: 9.5 >= 7, es 'Extremo' (terremoto de Valdivia 1960 fue 9.5)"""
