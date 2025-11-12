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

def test_tabla_del_5():
    """Test tabla del 5"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("5")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    lines = output.split('\n')
    assert len(lines) == 10, f"Debe imprimir exactamente 10 líneas (del 1 al 10), se obtuvieron {len(lines)}"
    
    expected = [
        "5 x 1 = 5",
        "5 x 2 = 10",
        "5 x 3 = 15",
        "5 x 4 = 20",
        "5 x 5 = 25",
        "5 x 6 = 30",
        "5 x 7 = 35",
        "5 x 8 = 40",
        "5 x 9 = 45",
        "5 x 10 = 50"
    ]
    
    for i, (expected_line, actual_line) in enumerate(zip(expected, lines), 1):
        assert actual_line == expected_line, f"Línea {i} incorrecta. Esperado: '{expected_line}', Obtenido: '{actual_line}'"

def test_tabla_del_1():
    """Test tabla del 1"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("1")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    lines = output.split('\n')
    assert len(lines) == 10, f"Debe imprimir exactamente 10 líneas (del 1 al 10), se obtuvieron {len(lines)}"
    
    expected = [
        "1 x 1 = 1",
        "1 x 2 = 2",
        "1 x 3 = 3",
        "1 x 4 = 4",
        "1 x 5 = 5",
        "1 x 6 = 6",
        "1 x 7 = 7",
        "1 x 8 = 8",
        "1 x 9 = 9",
        "1 x 10 = 10"
    ]
    
    for i, (expected_line, actual_line) in enumerate(zip(expected, lines), 1):
        assert actual_line == expected_line, f"Línea {i} incorrecta. Esperado: '{expected_line}', Obtenido: '{actual_line}'"

def test_tabla_del_10():
    """Test tabla del 10"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("10")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    lines = output.split('\n')
    assert len(lines) == 10, f"Debe imprimir exactamente 10 líneas (del 1 al 10), se obtuvieron {len(lines)}"
    
    expected = [
        "10 x 1 = 10",
        "10 x 2 = 20",
        "10 x 3 = 30",
        "10 x 4 = 40",
        "10 x 5 = 50",
        "10 x 6 = 60",
        "10 x 7 = 70",
        "10 x 8 = 80",
        "10 x 9 = 90",
        "10 x 10 = 100"
    ]
    
    for i, (expected_line, actual_line) in enumerate(zip(expected, lines), 1):
        assert actual_line == expected_line, f"Línea {i} incorrecta. Esperado: '{expected_line}', Obtenido: '{actual_line}'"

def test_tabla_del_0():
    """Test tabla del 0 (caso borde)"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("0")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    lines = output.split('\n')
    assert len(lines) == 10, f"""❌ Número incorrecto de líneas
   Se esperaban 10 líneas (del 1 al 10), se obtuvieron {len(lines)}
   💡 Pista: Aunque el número sea 0, debe mostrar 10 líneas"""
    
    expected = [
        "0 x 1 = 0",
        "0 x 2 = 0",
        "0 x 3 = 0",
        "0 x 4 = 0",
        "0 x 5 = 0",
        "0 x 6 = 0",
        "0 x 7 = 0",
        "0 x 8 = 0",
        "0 x 9 = 0",
        "0 x 10 = 0"
    ]
    
    for i, (expected_line, actual_line) in enumerate(zip(expected, lines), 1):
        assert actual_line == expected_line, f"""❌ Línea {i} incorrecta
   Esperado: '{expected_line}', Obtenido: '{actual_line}'
   💡 Pista: 0 multiplicado por cualquier número es siempre 0"""


