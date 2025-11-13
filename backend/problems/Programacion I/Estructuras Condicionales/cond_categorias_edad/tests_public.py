"""
Tests para: Cond Categorias Edad
Tema: Estructuras Condicionales

Este archivo contiene tests públicos que el estudiante puede ver.
Los tests verifican que la solución cumpla con todos los requisitos.
"""

import importlib.util
import os

spec = importlib.util.spec_from_file_location('student_code', os.path.join(os.getcwd(), 'student_code.py'))
student = importlib.util.module_from_spec(spec)
spec.loader.exec_module(student)

def test_existe_funcion():
    """Verifica que existe la función categoria_edad"""
    assert hasattr(student, 'categoria_edad'), 'Debe existir la función categoria_edad'

def test_categoria_nino():
    """Verifica categoría Niño/a"""
    assert student.categoria_edad(8) == "Niño/a", f"""❌ Categoría incorrecta
   Para edad=8: se esperaba 'Niño/a', se obtuvo '{student.categoria_edad(8)}'
   💡 Pista: Si edad < 13, es Niño/a"""

def test_categoria_adolescente():
    """Verifica categoría Adolescente"""
    assert student.categoria_edad(15) == "Adolescente", f"""❌ Categoría incorrecta
   Para edad=15: se esperaba 'Adolescente', se obtuvo '{student.categoria_edad(15)}'
   💡 Pista: Si 13 <= edad < 18, es Adolescente"""

def test_categoria_adulto_joven():
    """Verifica categoría Adulto/a joven"""
    assert student.categoria_edad(25) == "Adulto/a joven", f"""❌ Categoría incorrecta
   Para edad=25: se esperaba 'Adulto/a joven', se obtuvo '{student.categoria_edad(25)}'
   💡 Pista: Si 18 <= edad < 35, es Adulto/a joven"""

def test_categoria_adulto():
    """Verifica categoría Adulto/a"""
    assert student.categoria_edad(40) == "Adulto/a", f"""❌ Categoría incorrecta
   Para edad=40: se esperaba 'Adulto/a', se obtuvo '{student.categoria_edad(40)}'
   💡 Pista: Si 35 <= edad < 60, es Adulto/a"""
