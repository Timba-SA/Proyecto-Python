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

def test_password_valida_8():
    """Verifica contraseña válida de 8 caracteres"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("abc12345")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "Ha ingresado una contraseña correcta", f"""❌ Validación incorrecta
   Para contraseña='abc12345' (8 caracteres): se esperaba 'Ha ingresado una contraseña correcta', se obtuvo '{output}'
   💡 Pista: len(password) debe estar entre 8 y 14 (inclusive)"""

def test_password_valida_14():
    """Verifica contraseña válida de 14 caracteres"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("password123456")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "Ha ingresado una contraseña correcta", f"""❌ Validación incorrecta
   Para contraseña='password123456' (14 caracteres): se esperaba 'Ha ingresado una contraseña correcta', se obtuvo '{output}'
   💡 Pista: 14 es el máximo permitido (8 <= len <= 14)"""

def test_password_muy_corta():
    """Verifica contraseña muy corta"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("abc123")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "Por favor, ingrese una contraseña de entre 8 y 14 caracteres", f"""❌ No detectó contraseña corta
   Para contraseña='abc123' (6 caracteres): se esperaba mensaje de error, se obtuvo '{output}'
   💡 Pista: Si len(password) < 8, es muy corta"""

def test_password_muy_larga():
    """Verifica contraseña muy larga"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("password12345678")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "Por favor, ingrese una contraseña de entre 8 y 14 caracteres", f"""❌ No detectó contraseña larga
   Para contraseña='password12345678' (16 caracteres): se esperaba mensaje de error, se obtuvo '{output}'
   💡 Pista: Si len(password) > 14, es muy larga"""
