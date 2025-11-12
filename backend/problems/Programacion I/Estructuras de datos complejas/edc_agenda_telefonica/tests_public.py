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

def test_contacto_encontrado():
    """Verifica que encuentra un contacto existente"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("Juan\n123456\nAna\n987654\nPedro\n555111\nMaria\n444222\nLuis\n333999\nJuan")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert "123456" in output, "Debe mostrar el número de Juan"
    assert "Juan" in output, "Debe mencionar el nombre Juan"

def test_contacto_no_encontrado():
    """Verifica el mensaje cuando no encuentra un contacto"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("Juan\n123456\nAna\n987654\nPedro\n555111\nMaria\n444222\nLuis\n333999\nCarlos")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    assert "no encontrado" in output.lower() or "no existe" in output.lower(), "Debe indicar que el contacto no fue encontrado"
