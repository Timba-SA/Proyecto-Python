"""
Tests para: Cond Transformar Nombre
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

def test_nombre_completo_mayusculas():
    """Verifica opción 1 con nombre completo"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("Ana Maria Lopez\n1")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "ANA MARIA LOPEZ", f"""❌ Transformación incorrecta
   Para nombre='Ana Maria Lopez' y opción=1: se esperaba 'ANA MARIA LOPEZ', se obtuvo '{output}'
   💡 Pista: .upper() funciona con nombres completos también"""

def test_nombre_completo_minusculas():
    """Verifica opción 2 con nombre completo"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("CARLOS RODRIGUEZ\n2")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "carlos rodriguez", f"""❌ Transformación incorrecta
   Para nombre='CARLOS RODRIGUEZ' y opción=2: se esperaba 'carlos rodriguez', se obtuvo '{output}'
   💡 Pista: .lower() convierte todo el texto a minúsculas"""

def test_nombre_completo_title():
    """Verifica opción 3 con nombre completo"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("jose garcia\n3")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "Jose Garcia", f"""❌ Transformación incorrecta
   Para nombre='jose garcia' y opción=3: se esperaba 'Jose Garcia', se obtuvo '{output}'
   💡 Pista: .title() capitaliza la primera letra de cada palabra"""

def test_opcion_cero():
    """Verifica opción 0 (inválida)"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("test\n0")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "Opción inválida", f"""❌ No validó opción 0
   Para opción=0: se esperaba 'Opción inválida', se obtuvo '{output}'
   💡 Pista: Solo 1, 2 y 3 son opciones válidas"""

def test_opcion_negativa():
    """Verifica opción negativa (inválida)"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("test\n-1")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "Opción inválida", f"""❌ No validó opción negativa
   Para opción=-1: se esperaba 'Opción inválida', se obtuvo '{output}'
   💡 Pista: Verifica que la opción esté en el rango válido [1,2,3]"""
