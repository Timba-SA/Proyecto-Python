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

def test_termina_vocal_minuscula():
    """Verifica string que termina en vocal minúscula"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("casa")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "casa!", f"""❌ No agregó signo de exclamación
   Para palabra='casa' (termina en 'a'): se esperaba 'casa!', se obtuvo '{output}'
   💡 Pista: Usa palabra[-1] para obtener el último carácter y verifica si está en 'aeiouAEIOU'"""

def test_no_termina_vocal():
    """Verifica string que NO termina en vocal"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("papel")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "papel", f"""❌ Error con consonante
   Para palabra='papel' (termina en 'l'): se esperaba 'papel' (sin !), se obtuvo '{output}'
   💡 Pista: Si NO termina en vocal, devuelve la palabra sin cambios"""

def test_termina_vocal_mayuscula():
    """Verifica string que termina en vocal mayúscula"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("Chile")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "Chile!", f"""❌ No detectó vocal mayúscula
   Para palabra='Chile' (termina en 'e' mayúscula): se esperaba 'Chile!', se obtuvo '{output}'
   💡 Pista: Debes verificar vocales minúsculas Y mayúsculas: 'aeiouAEIOU'"""
