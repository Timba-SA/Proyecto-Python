"""
Tests para: Sec Presentacion Completa
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

def test_existe_funcion():
    """Verifica que existe la función main"""
    assert hasattr(student, 'main'), 'Debe existir la función main'

def test_presentacion_basica():
    """Test básico"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("Juan\nPérez\n25\nBuenos Aires")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    expected = "Soy Juan Pérez, tengo 25 años y vivo en Buenos Aires"
    assert output == expected, f"""❌ Presentación incorrecta
   Para Juan/Pérez/25/Buenos Aires: se esperaba '{expected}', se obtuvo '{output}'
   💡 Pista: Formato: "Soy {{nombre}} {{apellido}}, tengo {{edad}} años y vivo en {{ciudad}}" """

def test_presentacion_otra():
    """Test con otros datos"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("María\nGómez\n30\nCórdoba")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    expected = "Soy María Gómez, tengo 30 años y vivo en Córdoba"
    assert output == expected, f"""❌ Presentación incorrecta
   Para María/Gómez/30/Córdoba: se esperaba '{expected}', se obtuvo '{output}'
   💡 Pista: Revisa comas, espacios y tildes en la palabra años"""

