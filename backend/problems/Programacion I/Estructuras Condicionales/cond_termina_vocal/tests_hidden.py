"""
Tests para: Cond Termina Vocal
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

def test_vocal_o_minuscula():
    """Verifica vocal 'o' minúscula"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("perro")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "perro!", f"""❌ No detectó vocal 'o'
   Para palabra='perro': se esperaba 'perro!', se obtuvo '{output}'
   💡 Pista: La 'o' también es vocal"""

def test_vocal_i_minuscula():
    """Verifica vocal 'i' minúscula"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("kiwi")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "kiwi!", f"""❌ No detectó vocal 'i'
   Para palabra='kiwi': se esperaba 'kiwi!', se obtuvo '{output}'
   💡 Pista: Todas las vocales son: a, e, i, o, u"""

def test_vocal_A_mayuscula():
    """Verifica vocal 'A' mayúscula"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("CASA")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "CASA!", f"""❌ No detectó vocal 'A' mayúscula
   Para palabra='CASA': se esperaba 'CASA!', se obtuvo '{output}'
   💡 Pista: Incluye mayúsculas en la verificación: 'aeiouAEIOU'"""

def test_consonante_r():
    """Verifica string que termina en 'r'"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("amor")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "amor", f"""❌ Agregó ! cuando no debía
   Para palabra='amor' (termina en 'r'): se esperaba 'amor' (sin !), se obtuvo '{output}'
   💡 Pista: Solo agrega ! si termina en vocal"""

def test_consonante_l():
    """Verifica string que termina en 'l'"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("sol")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "sol", f"""❌ Agregó ! cuando no debía
   Para palabra='sol' (termina en 'l'): se esperaba 'sol' (sin !), se obtuvo '{output}'
   💡 Pista: 'l' es una consonante, no una vocal"""
    sys.stdout = old_stdout

    assert output == "sol", f"Se esperaba 'sol', se obtuvo '{output}'"
