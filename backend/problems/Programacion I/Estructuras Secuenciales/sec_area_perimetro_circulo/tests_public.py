import importlib.util
import os
from io import StringIO
import sys
import math

spec = importlib.util.spec_from_file_location('student_code', os.path.join(os.getcwd(), 'student_code.py'))
student = importlib.util.module_from_spec(spec)
spec.loader.exec_module(student)

def test_existe_funcion():
    """Verifica que existe la función main"""
    assert hasattr(student, 'main'), 'Debe existir la función main'

def test_radio_5():
    """Test con radio 5"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("5")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    lines = output.split('\n')
    assert len(lines) == 2, f"Se esperaban 2 líneas (área y perímetro), se obtuvieron {len(lines)}"
    
    # Calcular valores esperados
    radio = 5
    area_esperada = math.pi * radio ** 2
    perimetro_esperado = 2 * math.pi * radio
    
    area_obtenida = float(lines[0])
    perimetro_obtenido = float(lines[1])
    
    assert abs(area_obtenida - area_esperada) < 0.0001, f"""❌ Área incorrecta
   Para radio=5: se esperaba {area_esperada}, se obtuvo {area_obtenida}
   💡 Pista: Área = π × radio²"""
    assert abs(perimetro_obtenido - perimetro_esperado) < 0.0001, f"""❌ Perímetro incorrecto
   Para radio=5: se esperaba {perimetro_esperado}, se obtuvo {perimetro_obtenido}
   💡 Pista: Perímetro = 2 × π × radio"""

def test_radio_1():
    """Test con radio 1"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("1")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    lines = output.split('\n')
    assert len(lines) == 2, f"Se esperaban 2 líneas (área y perímetro), se obtuvieron {len(lines)}"
    
    radio = 1
    area_esperada = math.pi * radio ** 2
    perimetro_esperado = 2 * math.pi * radio
    
    area_obtenida = float(lines[0])
    perimetro_obtenido = float(lines[1])
    
    assert abs(area_obtenida - area_esperada) < 0.0001, f"""❌ Área incorrecta
   Para radio=1: se esperaba {area_esperada}, se obtuvo {area_obtenida}
   💡 Pista: Con radio=1, área = π"""
    assert abs(perimetro_obtenido - perimetro_esperado) < 0.0001, f"""❌ Perímetro incorrecto
   Para radio=1: se esperaba {perimetro_esperado}, se obtuvo {perimetro_obtenido}
   💡 Pista: Con radio=1, perímetro = 2π"""

def test_radio_10():
    """Test con radio 10"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("10")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    lines = output.split('\n')
    assert len(lines) == 2, f"Se esperaban 2 líneas (área y perímetro), se obtuvieron {len(lines)}"
    
    radio = 10
    area_esperada = math.pi * radio ** 2
    perimetro_esperado = 2 * math.pi * radio
    
    area_obtenida = float(lines[0])
    perimetro_obtenido = float(lines[1])
    
    assert abs(area_obtenida - area_esperada) < 0.0001, f"""❌ Área incorrecta
   Para radio=10: se esperaba {area_esperada}, se obtuvo {area_obtenida}
   💡 Pista: Área = π × 10²"""
    assert abs(perimetro_obtenido - perimetro_esperado) < 0.0001, f"""❌ Perímetro incorrecto
   Para radio=10: se esperaba {perimetro_esperado}, se obtuvo {perimetro_obtenido}
   💡 Pista: Perímetro = 2 × π × 10"""

def test_radio_1000():
    """Test con radio 1000 (caso borde - número grande)"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("1000")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    lines = output.split('\n')
    assert len(lines) == 2, f"Se esperaban 2 líneas (área y perímetro), se obtuvieron {len(lines)}"
    
    radio = 1000
    area_esperada = math.pi * radio ** 2
    perimetro_esperado = 2 * math.pi * radio
    
    area_obtenida = float(lines[0])
    perimetro_obtenido = float(lines[1])
    
    assert abs(area_obtenida - area_esperada) < 0.01, f"""❌ Área incorrecta
   Para radio=1000: se esperaba {area_esperada}, se obtuvo {area_obtenida}
   💡 Pista: Área = π × 1000² = π × 1,000,000"""
    assert abs(perimetro_obtenido - perimetro_esperado) < 0.01, f"""❌ Perímetro incorrecto
   Para radio=1000: se esperaba {perimetro_esperado}, se obtuvo {perimetro_obtenido}
   💡 Pista: Perímetro = 2 × π × 1000"""


