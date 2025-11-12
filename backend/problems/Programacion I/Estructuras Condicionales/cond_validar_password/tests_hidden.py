import importlib.util
import os
from io import StringIO
import sys

spec = importlib.util.spec_from_file_location('student_code', os.path.join(os.getcwd(), 'student_code.py'))
student = importlib.util.module_from_spec(spec)
spec.loader.exec_module(student)

def test_password_valida_10():
    """Verifica contraseña válida de 10 caracteres"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("mypass1234")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "Ha ingresado una contraseña correcta", f"""❌ Validación incorrecta
   Para contraseña='mypass1234' (10 caracteres): se esperaba 'Ha ingresado una contraseña correcta', se obtuvo '{output}'
   💡 Pista: 10 está dentro del rango válido [8-14]"""

def test_password_vacia():
    """Verifica contraseña vacía"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "Por favor, ingrese una contraseña de entre 8 y 14 caracteres", f"""❌ No detectó contraseña vacía
   Para contraseña='' (0 caracteres): se esperaba mensaje de error, se obtuvo '{output}'
   💡 Pista: len('') == 0, que es menor a 8"""

def test_password_limite_inferior():
    """Verifica límite inferior (7 caracteres)"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("pass123")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "Por favor, ingrese una contraseña de entre 8 y 14 caracteres", f"""❌ No detectó contraseña en límite inferior
   Para contraseña='pass123' (7 caracteres): se esperaba mensaje de error, se obtuvo '{output}'
   💡 Pista: 7 < 8, por lo tanto es muy corta"""

def test_password_con_espacios():
    """Verifica contraseña con espacios (caso borde - válido según enunciado)"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("pass word")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "Ha ingresado una contraseña correcta", f"""❌ Validación incorrecta con espacios
   Para contraseña='pass word' (9 caracteres): se esperaba 'Ha ingresado una contraseña correcta', se obtuvo '{output}'
   💡 Pista: Solo importa la longitud total, espacios cuentan como caracteres"""

def test_password_con_caracteres_especiales():
    """Verifica contraseña con caracteres especiales (caso borde - válido)"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("pass!@#$")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "Ha ingresado una contraseña correcta", f"""❌ Validación incorrecta con caracteres especiales
   Para contraseña='pass!@#$' (8 caracteres): se esperaba 'Ha ingresado una contraseña correcta', se obtuvo '{output}'
   💡 Pista: Caracteres especiales son válidos, solo importa len() [8-14]"""

def test_password_limite_superior():
    """Verifica límite superior (15 caracteres)"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("password1234567")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert output == "Por favor, ingrese una contraseña de entre 8 y 14 caracteres", f"""❌ No detectó contraseña en límite superior
   Para contraseña='password1234567' (15 caracteres): se esperaba mensaje de error, se obtuvo '{output}'
   💡 Pista: 15 > 14, por lo tanto es muy larga"""

