import importlib.util
import os
from io import StringIO
import sys
import inspect

spec = importlib.util.spec_from_file_location('student_code', os.path.join(os.getcwd(), 'student_code.py'))
student = importlib.util.module_from_spec(spec)
spec.loader.exec_module(student)

def test_formato_exacto():
    """Verifica el formato exacto del mensaje"""
    old_stdout = sys.stdout
    sys.stdout = StringIO()
    
    student.imprimir_hola_mundo()
    
    output = sys.stdout.getvalue()
    sys.stdout = old_stdout
    
    assert "Hola Mundo!" in output, "❌ El mensaje debe contener 'Hola Mundo!' con mayúsculas"
    assert output.strip() == "Hola Mundo!", "❌ No debe haber texto adicional"

def test_funcion_sin_parametros():
    """Verifica que la función no recibe parámetros"""
    sig = inspect.signature(student.imprimir_hola_mundo)
    assert len(sig.parameters) == 0, "❌ La función no debe recibir parámetros"
