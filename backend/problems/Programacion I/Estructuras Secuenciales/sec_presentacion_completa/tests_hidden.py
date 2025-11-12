import importlib.util
import os
from io import StringIO
import sys

spec = importlib.util.spec_from_file_location('student_code', os.path.join(os.getcwd(), 'student_code.py'))
student = importlib.util.module_from_spec(spec)
spec.loader.exec_module(student)

def test_formato_exacto():
    """Verifica formato exacto"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("Ana\nLópez\n22\nRosario")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    expected = "Soy Ana López, tengo 22 años y vivo en Rosario"
    assert output == expected, f"""❌ Formato exacto incorrecto
   Para Ana/López/22/Rosario: se esperaba '{expected}', se obtuvo '{output}'
   💡 Pista: Verifica espacios exactos después de comas y en la conjunción 'y'"""

def test_con_tildes():
    """Test con tildes"""
    old_stdin = sys.stdin
    old_stdout = sys.stdout
    sys.stdin = StringIO("José\nRodríguez\n28\nTucumán")
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdin = old_stdin
    sys.stdout = old_stdout

    expected = "Soy José Rodríguez, tengo 28 años y vivo en Tucumán"
    assert output == expected, f"""❌ Error con caracteres especiales
   Para José/Rodríguez/28/Tucumán: se esperaba '{expected}', se obtuvo '{output}'
   💡 Pista: Verifica que se mantengan los acentos (José, Rodríguez, Tucumán)"""

