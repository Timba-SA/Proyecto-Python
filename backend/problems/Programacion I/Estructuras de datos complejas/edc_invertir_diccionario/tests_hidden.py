import importlib.util
import os
from io import StringIO
import sys

spec = importlib.util.spec_from_file_location('student_code', os.path.join(os.getcwd(), 'student_code.py'))
student = importlib.util.module_from_spec(spec)
spec.loader.exec_module(student)

def test_todos_pares_invertidos():
    """Verifica que todos los pares fueron invertidos"""
    old_stdout = sys.stdout
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue()
    sys.stdout = old_stdout

    # Verificar que todas las capitales son claves
    assert "'Brasilia'" in output or '"Brasilia"' in output, "Brasilia debe estar como clave"
    assert "'Montevideo'" in output or '"Montevideo"' in output, "Montevideo debe estar como clave"
    
    # Verificar que los países están como valores
    assert "'Brasil'" in output or '"Brasil"' in output, "Brasil debe estar como valor"
    assert "'Uruguay'" in output or '"Uruguay"' in output, "Uruguay debe estar como valor"
