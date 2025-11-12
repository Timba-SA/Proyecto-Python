import importlib.util
import os
from io import StringIO
import sys

spec = importlib.util.spec_from_file_location('student_code', os.path.join(os.getcwd(), 'student_code.py'))
student = importlib.util.module_from_spec(spec)
spec.loader.exec_module(student)

def test_25_celsius():
    """Test 25°C"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("25")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    expected = "77.0"
    assert output == expected, f"""❌ Conversión incorrecta
   Para 25°C: se esperaba '{expected}°F', se obtuvo '{output}'
   💡 Pista: Fórmula: °F = °C × 9/5 + 32"""

def test_negativo():
    """Test temperatura negativa (-40°C, punto donde coinciden las escalas)"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("-40")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    expected = "-40.0"
    assert output == expected, f"❌ Conversión incorrecta para -40°C\n   Se esperaba '{expected}', se obtuvo '{output}'\n   💡 Dato curioso: -40°C = -40°F (único punto donde coinciden)"

def test_temperatura_corporal():
    """Test 37°C (temperatura corporal normal)"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("37")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    # 37°C × 9/5 + 32 = 66.6 + 32 = 98.6°F
    expected = "98.6"
    assert output == expected, f"❌ Conversión incorrecta para 37°C\n   Se esperaba '{expected}°F' (temperatura corporal), se obtuvo '{output}'\n   💡 Fórmula: °F = °C × 9/5 + 32"

