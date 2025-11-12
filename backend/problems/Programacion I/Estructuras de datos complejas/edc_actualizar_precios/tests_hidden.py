import importlib.util
import os
from io import StringIO
import sys

spec = importlib.util.spec_from_file_location('student_code', os.path.join(os.getcwd(), 'student_code.py'))
student = importlib.util.module_from_spec(spec)
spec.loader.exec_module(student)

def test_otras_frutas_intactas():
    """Verifica que las otras frutas mantienen sus precios originales"""
    old_stdout = sys.stdout
    sys.stdout = StringIO()

    student.main()

    output = sys.stdout.getvalue().strip()
    sys.stdout = old_stdout

    assert "'Ananá': 2500" in output or '"Ananá": 2500' in output, "Ananá debe mantener precio 2500"
    assert "'Uva': 1450" in output or '"Uva": 1450' in output, "Uva debe mantener precio 1450"
    assert "'Pera': 2300" in output or '"Pera": 2300' in output, "Pera debe mantener precio 2300"
