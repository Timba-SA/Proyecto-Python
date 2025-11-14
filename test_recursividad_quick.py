"""
Test rápido para verificar que rec_contar_digito falla con starter vacío
"""
import sys
import os

# Cambiar al directorio del ejercicio
os.chdir("backend/problems/Programacion I/Recursividad/rec_contar_digito")

# Copiar starter.py a student_code.py
import shutil
shutil.copy("starter.py", "student_code.py")

# Importar y ejecutar tests
import importlib.util

spec = importlib.util.spec_from_file_location('tests', 'tests_public.py')
tests_module = importlib.util.module_from_spec(spec)

try:
    spec.loader.exec_module(tests_module)
    
    # Intentar ejecutar un test
    print("🧪 Ejecutando test_contar_digito_basico...")
    try:
        tests_module.test_contar_digito_basico()
        print("❌ El test PASÓ (no debería)")
    except Exception as e:
        print(f"✅ El test FALLÓ como se esperaba: {str(e)[:100]}")
        
except Exception as e:
    print(f"✅ Error al cargar tests (esperado con starter vacío): {str(e)[:200]}")
