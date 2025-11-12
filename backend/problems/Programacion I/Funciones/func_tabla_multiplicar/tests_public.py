import importlib.util
import os
from io import StringIO
import sys

spec = importlib.util.spec_from_file_location('student_code', os.path.join(os.getcwd(), 'student_code.py'))
student = importlib.util.module_from_spec(spec)
spec.loader.exec_module(student)

def test_existe_funcion():
    assert hasattr(student, 'tabla_multiplicar'), 'Debe existir la función tabla_multiplicar'

def test_tabla_del_5():
    captured_output = StringIO()
    sys.stdout = captured_output
    student.tabla_multiplicar(5)
    sys.stdout = sys.__stdout__
    
    output = captured_output.getvalue()
    assert "5 x 1 = 5" in output, "❌ Debe imprimir 5 x 1 = 5"
    assert "5 x 10 = 50" in output, "❌ Debe imprimir hasta 5 x 10 = 50"
    assert output.count('\n') == 10, "❌ Debe imprimir 10 líneas"
