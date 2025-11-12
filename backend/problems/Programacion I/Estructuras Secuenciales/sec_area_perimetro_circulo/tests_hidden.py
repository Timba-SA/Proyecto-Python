import importlib.util
import os
from io import StringIO
import sys
import math

spec = importlib.util.spec_from_file_location('student_code', os.path.join(os.getcwd(), 'student_code.py'))
student = importlib.util.module_from_spec(spec)
spec.loader.exec_module(student)

def test_radio_0():
    """Test con radio 0 (área y perímetro deben ser 0)"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("0")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    lines = output.split('\n')
    assert len(lines) == 2, f"Se esperaban 2 líneas (área y perímetro), se obtuvieron {len(lines)}"
    
    area_obtenida = float(lines[0])
    perimetro_obtenido = float(lines[1])
    
    assert abs(area_obtenida - 0) < 0.0001, f"""❌ Área con radio 0 debe ser 0
   Se obtuvo {area_obtenida}
   💡 Pista: Cualquier número multiplicado por 0 da 0"""
    assert abs(perimetro_obtenido - 0) < 0.0001, f"""❌ Perímetro con radio 0 debe ser 0
   Se obtuvo {perimetro_obtenido}
   💡 Pista: Cualquier número multiplicado por 0 da 0"""

def test_radio_2_5_decimal():
    """Test con radio decimal 2.5"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("2.5")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    lines = output.split('\n')
    assert len(lines) == 2, f"Se esperaban 2 líneas (área y perímetro), se obtuvieron {len(lines)}"
    
    radio = 2.5
    area_esperada = math.pi * radio ** 2  # 19.634954084936208
    perimetro_esperado = 2 * math.pi * radio  # 15.707963267948966
    
    area_obtenida = float(lines[0])
    perimetro_obtenido = float(lines[1])
    
    assert abs(area_obtenida - area_esperada) < 0.0001, f"""❌ Área incorrecta
   Para radio=2.5: se esperaba {area_esperada}, se obtuvo {area_obtenida}
   💡 Pista: Área = π × radio² = π × 2.5²"""
    assert abs(perimetro_obtenido - perimetro_esperado) < 0.0001, f"""❌ Perímetro incorrecto
   Para radio=2.5: se esperaba {perimetro_esperado}, se obtuvo {perimetro_obtenido}
   💡 Pista: Perímetro = 2 × π × radio"""

def test_radio_3_7_decimal():
    """Test con radio decimal 3.7"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("3.7")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    lines = output.split('\n')
    assert len(lines) == 2, f"Se esperaban 2 líneas (área y perímetro), se obtuvieron {len(lines)}"
    
    radio = 3.7
    area_esperada = math.pi * radio ** 2  # 43.00884539611191
    perimetro_esperado = 2 * math.pi * radio  # 23.24778563015053
    
    area_obtenida = float(lines[0])
    perimetro_obtenido = float(lines[1])
    
    assert abs(area_obtenida - area_esperada) < 0.0001, f"""❌ Área incorrecta
   Para radio=3.7: se esperaba {area_esperada}, se obtuvo {area_obtenida}
   💡 Pista: Área = π × radio² = π × 3.7²"""
    assert abs(perimetro_obtenido - perimetro_esperado) < 0.0001, f"""❌ Perímetro incorrecto
   Para radio=3.7: se esperaba {perimetro_esperado}, se obtuvo {perimetro_obtenido}
   💡 Pista: Perímetro = 2 × π × radio"""

def test_precision_pi():
    """Verifica que se use math.pi (no aproximación como 3.14)"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("1")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    lines = output.split('\n')
    area_obtenida = float(lines[0])
    
    # Si usan 3.14 en lugar de math.pi, el área con radio 1 sería 3.14 en vez de 3.141592...
    assert area_obtenida > 3.14, f"""❌ Precisión insuficiente
   Parece que no estás usando math.pi (área obtenida: {area_obtenida})
   💡 Pista: Debes importar math y usar math.pi en lugar de 3.14"""
    assert area_obtenida < 3.15, f"""❌ Área incorrecta
   Para radio=1 el área debe ser π ≈ 3.14159... (obtuviste {area_obtenida})
   💡 Pista: Área = π × radio² = π × 1² = π"""

