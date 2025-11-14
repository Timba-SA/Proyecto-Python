#!/usr/bin/env python3
"""
Script para corregir errores de encoding en archivos hints.json y metadata.json
de los ejercicios de Programación I - Versión 2 con manejo de bytes.
"""

import json
import os
from pathlib import Path

def fix_file_encoding(file_path):
    """Lee y corrige el encoding de un archivo JSON."""
    try:
        # Leer el archivo como bytes
        with open(file_path, 'rb') as f:
            content_bytes = f.read()
        
        # Intentar decodificar con UTF-8, si falla usar latin-1
        try:
            content_str = content_bytes.decode('utf-8')
        except UnicodeDecodeError:
            content_str = content_bytes.decode('latin-1')
        
        original_content = content_str
        
        # Aplicar correcciones de caracteres específicos
        # Emojis mal codificados (secuencias de bytes específicas)
        replacements = {
            # Bombilla 💡
            '\xc3\xb0\xc5\xb8\xe2\x80\x99\xc2\xa1': '💡',
            # Fuego 🔥
            '\xc3\xb0\xc5\xb8\xe2\x80\x9c\xc2\xa5': '🔥',
            # Letras 🔤
            '\xc3\xb0\xc5\xb8\xe2\x80\x9c\xc2\xa4': '🔤',
            # Bug 🐛
            '\xc3\xb0\xc5\xb8\xc2\x90\xc2\x9b': '🐛',
            # Números 🔢
            '\xc3\xb0\xc5\xb8\xe2\x80\x9c\xc2\xa2': '🔢',
            # Gráfico 📊
            '\xc3\xb0\xc5\xb8\xe2\x80\x9c\xc5\xa0': '📊',
            # Ciclo 🔄
            '\xc3\xb0\xc5\xb8\xe2\x80\x9c\xe2\x80\x9e': '🔄',
            # Nota 📝
            '\xc3\xb0\xc5\xb8\xe2\x80\x9d\xc5\x93': '📝',
            # Stop 🛑
            '\xc3\xb0\xc5\xb8\xe2\x80\xba\xe2\x80\x98': '🛑',
            
            # Acentos mal codificados
            '\xc3\xa1': 'á',
            '\xc3\xa9': 'é',
            '\xc3\xad': 'í',
            '\xc3\xb3': 'ó',
            '\xc3\xba': 'ú',
            '\xc3\xb1': 'ñ',
            '\xc3\x81': 'Á',
            '\xc3\x89': 'É',
            '\xc3\x8d': 'Í',
            '\xc3\x93': 'Ó',
            '\xc3\x9a': 'Ú',
            '\xc3\x91': 'Ñ',
        }
        
        # Aplicar reemplazos
        for wrong, correct in replacements.items():
            content_str = content_str.replace(wrong, correct)
        
        # Verificar si hubo cambios
        if content_str == original_content:
            print(f"⚪ Sin cambios: {file_path.name}")
            return False
        
        # Validar que sea JSON válido
        try:
            json.loads(content_str)
        except json.JSONDecodeError as e:
            print(f"❌ Error de JSON en {file_path.name}: {e}")
            return False
        
        # Guardar con UTF-8
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content_str)
        
        print(f"✅ Corregido: {file_path.name}")
        return True
        
    except Exception as e:
        print(f"❌ Error procesando {file_path.name}: {e}")
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
    unchanged_count = 0
    error_count = 0
    
    for file_path in sorted(all_files):
        result = fix_file_encoding(file_path)
        if result is True:
            fixed_count += 1
        elif result is False:
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
