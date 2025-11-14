#!/usr/bin/env python3
"""
Script para corregir errores de encoding en archivos hints.json y metadata.json
de los ejercicios de Programación I.
"""

import json
import os
from pathlib import Path

def fix_encoding_errors(text):
    """Corrige errores comunes de encoding mal interpretado."""
    # Lista de reemplazos (patrón incorrecto, patrón correcto)
    replacements = [
        # Emojis específicos con secuencias de bytes mal interpretadas
        ('ðŸ'¡', '💡'),  # Bombilla
        ('ðŸ"¥', '🔥'),  # Fuego
        ('ðŸ"¤', '🔤'),  # Letras
        ('ðŸ›', '🐛'),   # Bug
        ('ðŸ"¢', '🔢'),  # Números
        ('ðŸ"Š', '📊'),  # Gráfico
        ('ðŸ"„', '🔄'),  # Ciclo
        ('ðŸ"', '🔍'),   # Lupa
        ('ðŸ"', '📝'),   # Nota
        ('ðŸ"š', '📚'),  # Libros
        ('ðŸš€', '🚀'),  # Cohete
        ('âœ…', '✅'),  # Check
        ('â�', '❌'),   # X
        # Secuencias alternativas de emojis
        ('Ã°Å¸â€™Â¡', '💡'),
        ('Ã°Å¸â€ºâ€˜', '🛑'),
        ('Ã°Å¸â€â€ž', '🔄'),
        ('Ã°Å¸Ââ€º', '🐛'),
        ('Ã°Å¸â€œÅ¡', '📝'),
        ('Á°Å¸â€â€ž', '🔄'),
        ('Á°Å¸Ââ€º', '🐛'),
        # Codificación UTF-8 doble
        ('ÃƒÂ³', 'ó'),
        ('ÃƒÂ­', 'í'),
        ('ÃƒÂ¡', 'á'),
        ('ÃƒÂ©', 'é'),
        ('ÃƒÂº', 'ú'),
        ('ÃƒÂ±', 'ñ'),
        ('ÃƒÅ¡', 'Ú'),
        # Vocales acentuadas mal codificadas
        ('Ã¡', 'á'),
        ('Ã©', 'é'),
        ('Ã­', 'í'),
        ('Ã³', 'ó'),
        ('Ãº', 'ú'),
        ('Ã±', 'ñ'),
        ('Ã', 'Á'),
        ('Ã‰', 'É'),
        ('Ã', 'Í'),
        ('Ã"', 'Ó'),
        ('Ãš', 'Ú'),
        ('Ã'', 'Ñ'),
        # Casos específicos encontrados
        ('Ãšsalas', 'Úsalas'),
        ('Ášsalas', 'Úsalas'),
        ('Ãºltimo', 'último'),
        ('Ã­ndice', 'índice'),
        ('Ã­ndices', 'índices'),
    ]
    
    result = text
    for wrong, correct in replacements:
        result = result.replace(wrong, correct)
    
    return result

def fix_json_file(file_path):
    """Corrige el encoding de un archivo JSON."""
    try:
        # Intentar leer con diferentes encodings
        content = None
        for encoding in ['utf-8', 'latin-1', 'cp1252']:
            try:
                with open(file_path, 'r', encoding=encoding) as f:
                    content = f.read()
                break
            except UnicodeDecodeError:
                continue
        
        if content is None:
            print(f"❌ No se pudo leer: {file_path}")
            return False
        
        # Aplicar correcciones
        original_content = content
        fixed_content = fix_encoding_errors(content)
        
        if original_content != fixed_content:
            # Verificar que sigue siendo JSON válido
            try:
                json.loads(fixed_content)
            except json.JSONDecodeError as e:
                print(f"❌ Error de JSON en {file_path}: {e}")
                return False
            
            # Guardar con UTF-8
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(fixed_content)
            
            print(f"✅ Corregido: {file_path}")
            return True
        else:
            print(f"⚪ Sin cambios: {file_path}")
            return False
    
    except Exception as e:
        print(f"❌ Error procesando {file_path}: {e}")
        return False

def main():
    """Procesa todos los archivos hints.json y metadata.json de Programación I."""
    base_path = Path(__file__).parent / 'backend' / 'problems' / 'Programacion I'
    
    if not base_path.exists():
        print(f"❌ No se encontró el directorio: {base_path}")
        return
    
    print(f"🔍 Buscando archivos en: {base_path}")
    
    # Buscar todos los archivos hints.json y metadata.json
    hints_files = list(base_path.glob('**/hints.json'))
    metadata_files = list(base_path.glob('**/metadata.json'))
    
    all_files = hints_files + metadata_files
    
    print(f"\n📊 Encontrados {len(all_files)} archivos:")
    print(f"   - {len(hints_files)} hints.json")
    print(f"   - {len(metadata_files)} metadata.json")
    print()
    
    fixed_count = 0
    error_count = 0
    unchanged_count = 0
    
    for file_path in sorted(all_files):
        result = fix_json_file(file_path)
        if result is True:
            fixed_count += 1
        elif result is False and "Sin cambios" in str(result):
            unchanged_count += 1
        else:
            error_count += 1
    
    print(f"\n📈 Resumen:")
    print(f"   ✅ Corregidos: {fixed_count}")
    print(f"   ⚪ Sin cambios: {unchanged_count}")
    print(f"   ❌ Errores: {error_count}")
    print(f"   📊 Total: {len(all_files)}")

if __name__ == '__main__':
    main()
